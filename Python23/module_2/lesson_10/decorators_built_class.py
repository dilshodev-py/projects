class Student:
    def __init__(self, name, score, total):
        self.name = name
        self.__score = score
        self.total = total

    @classmethod
    def from_str(cls, str_arg: str):
        name, score, total = str_arg.split(",")
        return cls(name, score, total)

    @classmethod
    def from_tuple(cls, tuple_arg: tuple):
        name, score, total = tuple_arg
        return cls(name, score, total)

    @staticmethod
    def get_percent(score, total):
        return score / total * 100

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @property
    def info(self):
        return f"{self.name} {self.__score} {self.total}"


