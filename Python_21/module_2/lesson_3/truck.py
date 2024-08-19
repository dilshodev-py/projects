import json
from datetime import date

# type hinting
file = open("truck.json", "r")
data: list[dict] = json.load(file)
file.close()


class Truck:
    def __init__(self,
                 id: int = None,
                 truck_name: str = None,
                 car_number: int = None,
                 status: str = None,
                 country: str = None,
                 size: str = None,
                 date: str = None
                 ) -> None:
        self.id = id
        self.truck_name = truck_name
        self.car_number = car_number
        self.status = status
        self.country = country
        self.size = size
        self.date = date

    def sequence_id(self):
        return data[-1].get("id") + 1

    def add(self) -> None:
        if self.status == "1":
            status = "START"
        if self.status == "2":
            status = "EMPTY"
        if self.status == "3":
            status = "PROCESS"
        if self.status == "4":
            status = "FINISHED"
        self.status = status
        data.append(self.__dict__)

    def filter_date(self, from_date: str, to_date: str) -> list[dict]:
        from_date = date.fromisoformat(from_date)
        to_date = date.fromisoformat(to_date)
        result = []
        for truck in data:
            truck_date = date.fromisoformat(truck.get("date"))
            if from_date <= truck_date <= to_date:
                result.append(truck)
        return result

    def car_number(self, number: int) -> dict:
        for truck in data:
            if truck.get("car_number") == number:
                return truck

    def status_search(self, status: str) -> list[dict]:
        result = []
        for truck in data:
            if truck.get("status") == status.upper():
                result.append(truck)
        return result

    def empty_truck_with_country(self, country: str) -> list[dict]:
        result = []
        for truck in data:
            if truck.get("status") == "EMPTY" and truck.get("country") == country.title():
                result.append(truck)
        return result

    def filter_size(self, size: str) -> list[dict]:
        result = []
        for truck in data:
            if size.upper() in truck.get("size"):
                result.append(truck)
        return result


status_menu = """
    1) START
    2) EMPTY
    3) PROCESS
    4) FINISHED
    >>>"""

size_menu = """
    1) S
    2) M
    3) L
    4) XS
    5) XL
    6) 2XL
    7) 3XL
    >>>"""

# truck = {
#     "id" : Truck().sequence_id(),
#     "truck_name" : input("Truck name : "),
#     "car_number" : input("Car number : "),
#     "status" : input(status_menu),
#     "country" : input("Country : "),
#     "size" : input(size_menu),
#     "date" : date.today()
# }

# print(len(data))
# Truck(**truck).add()
# print(len(data))


# print(*Truck().filter_date("2021-01-01", "2023-01-01"), sep= "\n")


# print(Truck().sequence_id())

# print(*Truck().filter_size("X"), sep = "\n")

# print(*Truck().empty_truck_with_country("Hungary") , sep = "\n")


# print(*Truck().status_search("PROCESS"), sep = "\n")
