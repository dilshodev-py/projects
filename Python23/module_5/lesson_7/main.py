from sqlalchemy import create_engine, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, declared_attr, relationship, mapped_column, Mapped
from sqlalchemy.sql.operators import ilike_op

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/alchemy_db", echo=False)


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"


class BaseClass(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)


class Subject(BaseClass):
    name: Mapped[str] = mapped_column(unique=True)
    groups: Mapped[list['Group']] = relationship(secondary='subjectgroups', back_populates='subjects')

    def __repr__(self):
        return self.name


class SubjectGroup(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id', ondelete="CASCADE"))
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id', ondelete="CASCADE"))


class Group(BaseClass):
    name: Mapped[str] = mapped_column(unique=True)
    subjects: Mapped[list['Subject']] = relationship(secondary='subjectgroups', back_populates='groups')

    def __repr__(self):
        return self.name


Base.metadata.create_all(engine)
#
with Session(engine) as session:
    query = select(Subject).where(ilike_op(Subject.name , '%p%'))
    subjects: list[Subject] = list(session.execute(query).scalars())
    for subject in subjects:
        print(subject.name, subject.groups)

# class Category(BaseClass):
#     __tablename__ = "categories"
#     name: Mapped[str] = mapped_column(unique=True)
#     products : Mapped[list['Product']] = relationship(back_populates='category')
#
#     def __repr__(self):
#         return self.name
#
# class Product(BaseClass):
#     name: Mapped[str] = mapped_column(unique=True)
#     quantity: Mapped[str] = mapped_column(unique=True)
#     price: Mapped[str] = mapped_column(unique=True)
#     category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'))
#     category:Mapped['Category'] = relationship(back_populates='products')
#
#     def __repr__(self):
#         return self.name


# with Session(engine) as session:
#     query  = select(Product)
#     products: list[Product] = list(session.execute(query).scalars())
#     for pro in products:
#         print(pro.name,pro.category)
