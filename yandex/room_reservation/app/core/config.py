from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    database_url: str

    class Config:
        # env_file = '/home/cloudy/yandex/room_reservation/.env'
        env_file = 'C:/Dev/20_sprint/yandex/projects/yandex/room_reservation/.env'

settings = Settings()
