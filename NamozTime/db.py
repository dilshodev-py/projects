from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/postgres")
Base = declarative_base()


class Namoz(Base):
    __tablename__ = "namoz"
    id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    name: Mapped[str] = mapped_column()
    time: Mapped[str] = mapped_column()


Base.metadata.create_all(engine)
