from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        # env_file = '/home/cloudy/projects/yandex/room_reservation/.env'
        env_file = 'C:/Dev/20_sprint/yandex/projects/yandex/room_reservation/.env'


settings = Settings()
