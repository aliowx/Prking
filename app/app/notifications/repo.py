from typing import Awaitable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from .models.notification import Notifications
from .schemas import (
    NotificationsCreate,
    NotificationsUpdate,
    ParamsNotifications,
)
import re
from app.plate.models import PlateList
from app import models


class CRUDNotifications(
    CRUDBase[Notifications, NotificationsCreate, NotificationsUpdate]
):
    async def get_multi_by_filter(
        self, db: Session | AsyncSession, *, params: ParamsNotifications
    ) -> list[Notifications] | Awaitable[list[Notifications]]:

        query = (
            select(
                Notifications,
                PlateList,
                models.Event,
                models.Zone.name,
                models.Equipment.tag,
                models.Record.latest_status,
            )
            .outerjoin(PlateList, Notifications.plate_list_id == PlateList.id)
            .outerjoin(models.Event, Notifications.event_id == models.Event.id)
            .outerjoin(models.Zone, models.Event.zone_id == models.Zone.id)
            .outerjoin(
                models.Equipment, models.Event.camera_id == models.Equipment.id
            )
            .outerjoin(
                models.Record, models.Event.record_id == models.Record.id
            )
        )

        filters = [Notifications.is_deleted == False]

        if params.input_read is not None:
            filters.append(Notifications.is_read == params.input_read)

        total_count = await self.count_by_filter(db, filters=filters)

        order_by = (
            Notifications.id.asc() if params.asc else Notifications.id.desc()
        )

        if params.size is None:
            resualt = (
                await db.execute(query.filter(*filters).order_by(order_by))
            ).fetchall()
            return resualt, total_count
        resualt = (
            await db.execute(
                query.filter(*filters)
                .offset(params.skip)
                .limit(params.size)
                .order_by(order_by)
            )
        ).fetchall()
        return resualt, total_count


notifications_repo = CRUDNotifications(Notifications)
