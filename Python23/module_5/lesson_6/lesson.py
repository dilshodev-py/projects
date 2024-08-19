from enum import Enum as py_enum
from typing import Optional
from sqlalchemy import create_engine, delete, and_, or_, update, select, Enum
from sqlalchemy import insert
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/alchemy_db", echo=False)


class Base(DeclarativeBase):
    pass


class BaseClass(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)



class User(BaseClass):
    __tablename__ = "users"  # noqa
    age: Mapped[int]
    fullname: Mapped[Optional[str]]

    def __repr__(self):
        return self.fullname

with Session(engine) as session:
    print(list(session.execute(query).scalars()))
    session.commit()

Base.metadata.create_all(engine)


class ChatType(py_enum):
    group = 'Group'
    channel = 'Channel'
    lichka = 'Lichka'


class Chat(Base):
    __tablename__ = "chats"  # noqa
    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('users.id', ondelete='CASCADE'))
    message: Mapped[Optional[str]] = mapped_column(TEXT)
    type: Mapped[str] = mapped_column(Enum(ChatType), default=ChatType.lichka)
    chat_id: Mapped[Optional[int]]


Enum("value1", "value2", "value3")


class Address(Base):
    __tablename__ = "address"  # noqa
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey("users.id", ondelete="CASCADE"))



    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


Base.metadata.create_all(engine)
