"""
 python class + postgresql    sqlalchemy
"""
from sqlalchemy import create_engine, TEXT, BigInteger, ForeignKey, insert, column, select, desc, delete, and_, or_, \
    update
from sqlalchemy.orm import declarative_base, DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.sql.functions import count

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/factor_db")
session = Session(bind=engine)



class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column("firstname" ,TEXT)
    last_name: Mapped[str]
    addresses : Mapped[list['Address']] = relationship('Address', back_populates="user")


class Address(Base):
    __tablename__ = "addresses"

    id : Mapped[int] = mapped_column(__type_pos=BigInteger,primary_key=True , autoincrement=True)
    region : Mapped[str]
    district : Mapped[str]
    home_number : Mapped[int]
    user_id : Mapped[int] = mapped_column("user_id", BigInteger , ForeignKey("users.id"))
    user : Mapped['User'] = relationship('User', back_populates="addresses")


query = select(User)
users: list[tuple[User]] = session.execute(query).fetchall()
for user in users:
    user = user[0]
    for address in user.addresses:
        print(f"{user.first_name} : {address.region}")





# =========================================================


# query = insert(User).values(first_name = "Kamol" , last_name = "Qodirov").returning(column("id"))
# query = select(count()).select_from(User).where(User.id == 1)
# query = select(User.first_name , User.last_name).select_from(User).where(User.id == 1)
# query = delete(User).where(and_(User.id == 2 , User.first_name == "Kamol"))
# query = update(User).values(first_name = "Botir").where(User.id == 3)

# session.execute(query)
# session.commit()

# users: list[tuple[User]] = session.execute(query).scalar()
# print(users)
# for user in users:
#     print(user[0].id)
# session.commit()




# Base.metadata.create_all(engine)

# class Base(DeclarativeBase):
#     pass

"""
User:
    id
    name
    fullname

Address: 
    id
    region
    district
    home_number
        
"""

"""task"""
# DJANGO jinja , drf , FASTAPI
"""
Students
    id
    name
    age
    ball

course
    id
    name
    
courses_students
    id
    student_id
    course_id
"""

