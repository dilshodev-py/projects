from sqlalchemy import insert, delete, select

from db.config import session
from db.model import Category

categories = ["IT and Programming", "SMM" , "UI/UX" , "Web Design", "Data Science"]


def add_categories():
    for i in categories:
        q = select(Category).where(i == Category.name)
        cat = session.execute(q).fetchone()
        if not cat:
            q= insert(Category).values(name = i)
            session.execute(q)
            session.commit()


