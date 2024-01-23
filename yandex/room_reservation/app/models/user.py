from fastapi_users_db_sqlalchemy import SQLAlchemyBaseOAuthAccountTable

from app.core.db import Base

class User(SQLAlchemyBaseOAuthAccountTable[int], Base):
    pass