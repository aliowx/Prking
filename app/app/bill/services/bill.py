from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.bill.schemas import bill as billSchemas
from app.bill.repo import bill_repo
from app.core.exceptions import ServiceFailure
from app.utils import MessageCodes
from app.parking.repo import zone_repo
import pytz
import math
import re


def validate_iran_phone_number(phone_number: str):
    iran_phone_pattern = r"^(09\d{9}|(\+98)9\d{9})$"
    if not re.match(iran_phone_pattern, phone_number):
        raise ServiceFailure(
            detail="phone number incorrect",
            msg_code=MessageCodes.not_found,
        )


def validate_iran_plate(plate: str):
    iran_plate = r"[0-9?]{9}"
    if not re.match(iran_plate, plate):
        raise ServiceFailure(
            detail="plate incorrect",
            msg_code=MessageCodes.not_found,
        )


def convert_to_timezone_iran(time: datetime):
    if isinstance(time, str):
        time = datetime.fromisoformat(time)
    # Define Iran Standard Time timezone
    iran_timezone = pytz.timezone("Asia/Tehran")
    # If value is naive (no timezone), localize it to UTC
    if time.tzinfo is None:
        # Localize the naive datetime to UTC
        utc_time = pytz.utc.localize(time)
    else:
        # If it's already timezone aware, convert to UTC
        utc_time = time.astimezone(pytz.utc)
    # Convert to Iran Standard Time
    return utc_time.astimezone(iran_timezone)


def convert_time_to_hour_and_ceil(start_time, end_time):
    if start_time > end_time:
        return 0

    time_diff = end_time - start_time

    convert_time_to_hours = time_diff.total_seconds() / 3600

    ciel_hours = math.ceil(convert_time_to_hours)

    return ciel_hours


async def calculate_price_async(
    db: AsyncSession,
    *,
    zone_id: int,
    start_time_in: datetime,
    end_time_in: datetime,
) -> float:

    get_price = await zone_repo.get_price_zone_async(db, zone_id=zone_id)
    if not get_price:
        raise ServiceFailure(
            detail="not set model price for this zone",
            msg_code=MessageCodes.not_found,
        )

    duration_time = convert_time_to_hour_and_ceil(start_time_in, end_time_in)
    price = get_price.entrance_fee + (duration_time * get_price.hourly_fee)

    return price, get_price


def calculate_price(
    db: Session,
    *,
    zone_id: int,
    start_time_in: datetime,
    end_time_in: datetime,
) -> float:

    get_price = zone_repo.get_price_zone(db, zone_id=zone_id)

    if not get_price:
        raise ServiceFailure(
            detail="not set model price for this zone",
            msg_code=MessageCodes.not_found,
        )

    duration_time = convert_time_to_hour_and_ceil(start_time_in, end_time_in)

    price = get_price.entrance_fee + (duration_time * get_price.hourly_fee)

    return price, get_price


async def set_detail(db: AsyncSession, bill: billSchemas.Bill):

    bill.time_park = round(
        (bill.end_time - bill.start_time).total_seconds() / 60
    )
    if bill.zone_id:
        zone = await zone_repo.get(db, id=bill.zone_id)
        bill.zone_name = zone.name

    if bill.img_entrance_id:
        bill.camera_entrance = await bill_repo.get_camera_by_image_id(
            db, img_id=bill.img_entrance_id
        )

    if bill.img_exit_id:
        bill.camera_exit = await bill_repo.get_camera_by_image_id(
            db, img_id=bill.img_exit_id
        )

    return bill


async def get_paid_unpaid_bills(db: AsyncSession, *, plate: str):
    bill_unpaid = await bill_repo.get_bills_by_plate(
        db,
        plate=plate,
        bill_status=billSchemas.StatusBill.unpaid.value,
    )
    bills_unpaid = [
        billSchemas.BillUnpaidShow(**unpaid.__dict__) for unpaid in bill_unpaid
    ]
    bill_paid = await bill_repo.get_bills_by_plate(
        db, plate=plate, bill_status=billSchemas.StatusBill.paid.value
    )
    bills_paid = [
        billSchemas.BillPaidShow(**paid.__dict__) for paid in bill_paid
    ]
    return bills_paid, bills_unpaid


async def update_multi_bill(
    db: AsyncSession, bills_update: list[billSchemas.BillUpdate]
):
    resualt = {}

    list_bills_update = []
    list_bills_not_update = []
    msg_code = 0
    for bill_in in bills_update:
        bill = await bill_repo.get(db, id=bill_in.id, for_update=True)
        if bill:
            if bill.rrn_number is not None:
                msg_code = 14
                list_bills_not_update.append(bill)
            if bill.rrn_number is None:
                bill_update = await bill_repo.update(
                    db, db_obj=bill, obj_in=bill_in.model_dump()
                )
                await db.commit()
                list_bills_update.append(bill_update)

        if not bill:
            list_bills_not_update.append(
                {"bill by this id not found": bill_in.id}
            )
    resualt.update({"list_bills_update": list_bills_update})
    if list_bills_not_update != []:
        resualt.update({"list_bills_not_update": list_bills_not_update})
    return resualt, msg_code