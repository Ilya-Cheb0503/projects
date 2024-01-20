from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.reservation import reservation_crud
from app.schemas.reservation import ReservationCreate, ReservationDB
from projects.yandex.room_reservation.app.api.validators import (
    check_meeting_room_exists,
    check_reservation_intersections)
from projects.yandex.room_reservation.app.core.db import get_async_session


router = APIRouter()


@router.post(
    '/',
    response_model=ReservationDB
    )
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_meeting_room_exists(
        reservation.meetingroom_id, session
        )

    await check_reservation_intersections(
        **reservation.dict(),
        session=session
    )

    new_reservation = await reservation_crud.create(
        reservation,
        session)

    return new_reservation
