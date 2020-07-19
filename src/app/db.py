import json

from databases import Database
from decouple import config
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.sql import func
from src.aws_helper.aws_secrets import get_secret

account = json.loads(get_secret())

DATABASE_URL = (
    f"postgresql://{account['username']}:{account['password']}"
    f"@{account['host']}:{account['port']}/{config('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)
metadata = MetaData(schema=config("SCHEMA"))

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
