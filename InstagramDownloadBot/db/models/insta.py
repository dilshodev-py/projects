from sqlalchemy import BigInteger, VARCHAR, select
from sqlalchemy.orm import Mapped, mapped_column, selectinload

from db.models.base import Base, AbstractClass, db


class Insta(Base, AbstractClass):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    shortcode: Mapped[str] = mapped_column(VARCHAR(255), nullable=True, index=True)
    file_id: Mapped[str] = mapped_column(VARCHAR(255))

    @classmethod
    async def get_by_shortcode(cls, shortcode):
        query = select(cls).where(cls.shortcode == shortcode)

        return (await db.execute(query)).scalar()

