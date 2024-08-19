from dataclasses import dataclass

from tabulate import tabulate

#
# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
#          ["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))
# D = [
#     {"pos": 1,
#      "value": "Login"},
#     {"pos": 2,
#      "value": "Register                   ."},
#     {"pos": 3,
#      "value": "Exit"}
# ]
# print(tabulate(D, tablefmt='rounded_grid'))


from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator


class Delivery(BaseModel):
    a: int
    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if not v.endswith('@gmail.com'):
            raise ValueError('Email must end with @gmail.com')
        return v



m = Delivery(a=1, email="test")
