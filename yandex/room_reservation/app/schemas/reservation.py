from datetime import datetime

from pydantic import BaseModel, root_validator, validator, Extra


class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'from_time': '2028-04-24T11:00',
                'to_time': '2028-04-24T12:00'
            }
        }


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value: datetime):
        if value <= datetime.now():
            raise ValueError(
                'Прошу прощения, но вряд ли '
                'у вас в гараже "DeLorean DMC-12"'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values: dict[str, datetime]):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int

    class Config:
        orm_mode = True
