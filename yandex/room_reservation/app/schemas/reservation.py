from datetime import datetime
import pytz

from pydantic import BaseModel, root_validator, validator, Extra


def reservation_time():
    tz = pytz.timezone('Europe/Moscow')
    time_now = datetime.now(tz=tz)

    year_month_day_format = '%Y-%m-%d'
    hours_format = '%H'
    minutes_format = '%M'

    y_m_d = datetime.strftime(time_now, year_month_day_format)
    hours = datetime.strftime(time_now, hours_format)
    minutes = datetime.strftime(time_now, minutes_format)

    hours_from_time = int(hours)
    minutes_from_time = int(minutes) + 10
    if minutes_from_time >= 60:
        minutes_from_time = f'0{minutes_from_time - 60}'
        hours_from_time += 1
    from_time = f'{y_m_d}T{hours_from_time}:{minutes_from_time}'

    hours_to_time = int(hours) + 1
    if hours_to_time == 24:
        hours_to_time = '00'
    elif hours_to_time > 24:
        hours_to_time = '01'
    minutes_to_time = int(minutes)
    to_time = f'{y_m_d}T{hours_to_time}:{minutes_to_time}'
    result = {
        'from_time': from_time,
        'to_time': to_time
        }

    return result


class ReservationBase(BaseModel):
    from_reserve: datetime
    to_reserve: datetime

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': reservation_time()
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
