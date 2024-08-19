from sqlalchemy.orm import Mapped, mapped_column

from db.utils import Base, DB


class User(Base):
    id : Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    fullname : Mapped[str]



Base.metadata.create_all(DB.engine)


