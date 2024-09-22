import logging

from sqlalchemy.orm import Session
from app import crud
from app import models
from app.core.fake_data import fake_data
from app.db.session import SessionLocal
from app import schemas
import random
import string
from app.core.celery_app import celery_app
from fastapi.encoders import jsonable_encoder
from cache.redis import redis_client
import rapidjson
from datetime import datetime, timedelta, timezone
import time

from app.bill.services.bill import calculate_price
from app.bill.schemas import bill as billSchemas


logger = logging.getLogger(__name__)


def commit_to_db(db: Session, data: any, name: str):
    db.add(data)
    db.commit()
    db.refresh(data)

    logger.info(f"create {name}")

    return data


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for i in range(length))
    return random_string


def create_parking(db: Session) -> None:
    parking = db.query(models.Parking).first()

    if not parking:
        parking = fake_data.PARKING
        commit_to_db(db, data=parking, name="parking")
    return parking


def create_equipment(db: Session):
    equipment_entrance = (
        db.query(models.Equipment)
        .where(
            models.Equipment.is_deleted == False,
            models.Equipment.equipment_type == 1,
        )
        .all()
    )
    equipment_exit = (
        db.query(models.Equipment)
        .where(
            models.Equipment.is_deleted == False,
            models.Equipment.equipment_type == 2,
        )
        .all()
    )
    equipment = []
    for entrance, exit in zip(equipment_entrance, equipment_exit):
        equipment.append(entrance.id)
        equipment.append(exit.id)
    return equipment


def create_image(db: Session):
    image = db.query(models.Image).first()
    if not image:
        image = fake_data.IMAGE
        return commit_to_db(db, data=image, name="image")
    return image


def create_price(db: Session):
    price = (
        db.query(models.Price)
        .filter(
            *[models.Price.hourly_fee == 0, models.Price.entrance_fee == 20000]
        )
        .first()
    )
    if not price:
        return commit_to_db(
            db,
            data=models.Price(
                name="first simple price", entrance_fee=20000, hourly_fee=0
            ),
            name="image",
        )
    return price


def create_zone(db: Session):
    zones = db.query(models.Zone).all()
    zone_ids = []
    price = create_price(db)
    for zone in zones:
        if not zone.price_id:
            zone.price_id = price.id
        zone_ids.append(zone.id)
    if not zones:
        zone = fake_data.ZONE
        zone.zone_id = price.id
        return commit_to_db(db, data=zone, name="zone")
    return zone_ids


def create_sub_zone(db: Session):
    sub_zone = (
        db.query(models.Zone)
        .where(
            models.Zone.is_deleted == False,
            models.Zone.name == fake_data.SUB_ZONE.name,
        )
        .first()
    )
    if not sub_zone:
        sub_zone = fake_data.SUB_ZONE
        sub_zone.parent_id = create_zone(db).id
        commit_to_db(db, data=sub_zone, name="sub_zone")
    return sub_zone


def create_records(db: Session):
    records_data = [
        fake_data.RECORD1,
        fake_data.RECORD2,
    ]
    zone_ids = create_zone(db)
    image = create_image(db)
    for record in records_data:
        record.img_exit_id = image.id
        record.img_entrance_id = image.id
        record.zone_id = random.choice(zone_ids)
        db.add(record)
    db.commit()
    db.refresh(record)
    logger.info("create record")
    create_records_past(db)


list_status_record = [
    schemas.StatusRecord.finished.value,
    schemas.StatusRecord.unfinished.value,
    # schemas.StatusRecord.unknown.value,
]

status_bills = [
    billSchemas.StatusBill.unpaid.value,
    billSchemas.StatusBill.paid.value,
]


def create_records_past(db: Session):
    image = create_image(db)
    zone_ids = create_zone(db)
    latest_id_record = (
        db.query(models.Record).order_by(models.Record.id.desc()).first()
    ).id
    for i in range(1, 1000):
        record = models.Record(
            id=latest_id_record + i,
            plate=f"{random.randint(10,99)}{random.randint(10,70)}{random.randint(100,999)}{random.randint(10,99)}",
            start_time=datetime.now(timezone.utc).replace(tzinfo=None),
            end_time=datetime.now(timezone.utc).replace(tzinfo=None)
            + timedelta(hours=random.randint(1, 23)),
            img_entrance_id=None,
            img_exit_id=None,
            score=0.01,
            zone_id=random.choice(zone_ids),
            latest_status=schemas.StatusRecord.finished.value,
            created=datetime(
                year=random.randint(2023, 2024),
                month=random.randint(1, 9),
                day=random.randint(1, 20),
            ),
        )
        record.img_entrance_id = image.id
        record.img_exit_id = image.id
        db.add(record)

        if record.latest_status == schemas.StatusRecord.finished:
            bill = models.Bill(
                plate=record.plate,
                start_time=record.start_time,
                end_time=record.end_time,
                issued_by=billSchemas.Issued.exit_camera.value,
                price=calculate_price(
                    db,
                    zone_id=record.zone_id,
                    start_time_in=record.start_time,
                    end_time_in=record.end_time,
                ),
                record_id=record.id,
                zone_id=record.zone_id,
                status=random.choice(status_bills),
            )
            db.add(bill)

        redis_client.publish(
            "records:1", rapidjson.dumps(jsonable_encoder(record))
        )
        crud.record._commit_refresh(db=db, db_obj=record, commit=False)
    db.commit()


type_camera_event = [
    schemas.event.TypeCamera.entranceDoor.value,
    schemas.event.TypeCamera.exitDoor.value,
]


def create_events(db: Session):
    image = create_image(db)
    cameras = create_equipment(db)
    zone_ids = create_zone(db)
    events = []
    for _ in range(1, 50):
        event = models.Event(
            plate=f"{random.randint(10,99)}{random.randint(10,70)}{random.randint(100,999)}{random.randint(10,99)}",
            record_time=(
                datetime(
                    year=random.randint(2023, 2024),
                    month=random.randint(1, 9),
                    day=random.randint(1, 28),
                )
            ),
            plate_image_id=image.id,
            lpr_image_id=image.id,
            camera_id=random.choice(cameras),
            zone_id=random.choice(zone_ids),
            type_camera=schemas.event.TypeCamera.entranceDoor.value,
        )
        events.append(event)
        celery_app.send_task(
            "add_events",
            args=[jsonable_encoder(event)],
        )

    time.sleep(3)
    for one_event in events:
        event = models.Event(
            plate=one_event.plate,
            record_time=one_event.record_time
            + timedelta(hours=random.randint(1, 16)),
            type_camera=random.choice(type_camera_event),
            plate_image_id=image.id,
            lpr_image_id=image.id,
            camera_id=one_event.camera_id,
            zone_id=one_event.zone_id,
        )
        celery_app.send_task(
            "add_events",
            args=[jsonable_encoder(event)],
        )


def init_db_fake_data(db: Session) -> None:
    try:
        # create_parking(db)
        # create_equipment(db)
        # create_image(db)
        # create_zone(db)
        # create_sub_zone(db)
        create_records(db)
        # create_records_past(db)
        create_events(db)
    except Exception as e:
        logger.error(f"initial data creation error\n{e}")


if __name__ == "__main__":
    db = SessionLocal()
    init_db_fake_data(db)
