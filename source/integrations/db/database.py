from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import Postgres

engine = create_engine(
    f"postgresql://{Postgres.user}:{Postgres.password}@{Postgres.host}:{Postgres.port}/{Postgres.db_name}",
)

get_db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
