from sqlalchemy import Column, JSON, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_USER = "postgres"
PG_PASSWORD = ""
PG_DB = "test"
PG_HOST = "127.0.0.1"
PG_PORT = 5432

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_async_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base(bind=engine)


class SwapiPeople(Base):
    __tablename__ = 'swapipeople'
    person_id = Column(String, nullable = True)
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = True)
    height = Column(String, nullable = True)
    mass = Column(String, nullable = True)
    hair_color = Column(String, nullable = True)
    skin_color = Column(String, nullable = True)
    eye_color = Column(String, nullable = True)
    birth_year = Column(String, nullable = True)
    gender = Column(String, nullable = True)
    homeworld = Column(String, nullable = True)
    films = Column(String, nullable = True)
    species = Column(String, nullable = True)
    vehicles = Column(String, nullable = True)
    starships = Column(String, nullable = True)




