from dataclasses import dataclass
import smtplib, ssl

from project.ToDo_ORM.DB.main import DB


class User(DB):
    def __init__(self,
                 *param,
                 first_name: str = None,
                 last_name: str = None,
                 email: str = None):
        self.param = param
        self.first_name = first_name
        self.last_name = last_name
        self.email = email










