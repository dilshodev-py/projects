from datetime import datetime
from enum import Enum
from sqlalchemy import Integer, Enum as AsEnum, BigInteger, VARCHAR, ForeignKey, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped

from db.models.base import CreatedModel, Base, AbstractClass


class User(CreatedModel):
    class LangEnum(Enum):
        EN = "en"
        UZ = "uz"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    lang: Mapped[str] = mapped_column(AsEnum(LangEnum, values_callable=lambda i: [field.value for field in i]),
                                      default=LangEnum.EN, nullable=True)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)


    def __str__(self):
        return f"{self.full_name}"



class Referal(CreatedModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    link: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
