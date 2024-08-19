"""
OOP tamoillari
    class
    object
    encapsulation
        public
        protected
        private
    polymorphism
        override
        overload
    inheritance
    abstraction
konstruktr
decorator : [classmethod ,
            abstractmethod ,
            property ,
            setter ,
            staticmethod ,
            dataclass]
open
    w
    r
    a
    x

with
class attribute
class instance attribute
"""

from colorama import Fore, Back


class AuthExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    raise AuthExcept("Error salom")
except AuthExcept as e:
    print("\t" * 10, Back.BLUE + Fore.RED + str(e), end="")

# with open('matn.txt' , 'r') as f:
#     txt = f.read()
# res = " ".join(map(lambda x : x[:-1], sorted(txt.split() , key=lambda x : x[-1])))
# with open('matn.txt' , 'w') as f:
#     f.write(res)
# tmp = "234565435"
# print(tmp.replace(max(tmp , key=tmp.count), ''))
# [print(tmp[i:i+2]) for i in range(0, len(tmp),2)]
"""
23
45
65
43
5
"""


class MessageWriter(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()

