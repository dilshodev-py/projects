import asyncio

from sqlalchemy import delete
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import Session
from sqlalchemy.orm.sync import update

from db import Namoz, engine
from utils import parse_time


session = Session(bind = engine)
def cron():
    data = asyncio.run(parse_time())
    session.execute(delete(Namoz))
    session.execute(insert(Namoz) , data)
    session.commit()

if __name__ == '__main__':
    cron()