from datetime import datetime
import pytz

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation

from typing import Optional


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
            self,
            *,
            from_reserve: datetime,
            to_reserve: datetime,
            meetingroom_id: int,
            reservation_id: Optional[int] = None,
            session: AsyncSession,
    ) -> list[Reservation]:

        select_stmt = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            and_(
                from_reserve <= Reservation.to_reserve,
                to_reserve >= Reservation.from_reserve
            )
        )

        if reservation_id is not None:
            select_stmt = select_stmt.where(
                Reservation.id != reservation_id
            )

        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations


    async def get_future_reservations_for_room(
            self,
            room_id: int,
            session: AsyncSession
    ):
        tz = pytz.timezone('Europe/Moscow')
        time_now = datetime.now(tz=tz)
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.meetingroom_id == room_id,
                Reservation.to_reserve > time_now
                ))
        reservations = reservations.scalars().all()
        return reservations


    async def get_by_user(
        self,
        user_id: int,
        session: AsyncSession
    ) -> list[Reservation]:
        
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.user_id == user_id))
        reservations = reservations.scalars().all()

        return reservations


reservation_crud = CRUDReservation(Reservation)


    # async def get_reservations_at_the_same_time(
    #     self,
    #     from_reserve: datetime,
    #     to_reserve: datetime,
    #     meetingroom_id: int,
    #     session: AsyncSession
    # ) -> list[Reservation]:
    #     reservations = await session.execute(
    #         select(Reservation).where(
    #             (Reservation.from_reserve
    #              <= from_reserve < Reservation.to_reserve)
    #             or (Reservation.from_reserve
    #                 < to_reserve <= Reservation.to_reserve)
    #             and Reservation.meetingroom_id == meetingroom_id)
    #     )
    #     reservations = reservations.scalars().all()
    #     return reservations
    #
    #   ^^^^^^^^^^^^^^^^^^^^^^^^
    #   ||||||||||||||||||||||||
    #
    #   данная схема select не работает.
    #   поэтому необходимо разобраться
    #   с логикой написания запросов
    #   в SQL таблицах

