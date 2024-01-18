from fastapi import FastAPI

import uvicorn

from app.api.meeting_room import router
from app.core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, )
