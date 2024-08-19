# id
# name
# number
# place
# user_id
# join_at
import datetime
import json


class File:
    def __init__(self , file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path , 'r') as f:
            data = json.load(f)
        return data

    def write(self , data):
        with open(self.file_path , 'w') as f:
            json.dump(data , f , indent=3)

class Car:
    def __init__(self,id = None,
                    name = None,
                    number = None,
                    place = None,
                    user_id = None,
                    join_at = None):
        self.id = id
        self.name = name
        self.number = number
        self.place = place
        self.user_id = user_id
        self.join_at = join_at

    def save(self):
        f = File('cars.json')
        cars : list[dict] = f.read()
        cars.append(self.__dict__)
        f.write(cars)

    def placement(self):
        f_car = File("cars.json")
        cars = f_car.read()
        is_valid_car = True
        is_valid_parking = True
        message = "Successful"
        for car in cars:
            if car.get("id") == self.id:
                if not car.get("place") is None:
                    is_valid_car = False
                    message = "Bunday aftomabil joyashtirilgan"
                car['place'] = self.place

        f_parking = File('parking.json')
        map: list[list] = f_parking.read()
        i = 1
        for row in range(len(map)):
            for col in range(len(map[0])):
                if i == self.place:
                    if isinstance(map[row][col] , list):
                        is_valid_parking = False
                        message = "Bu joyda aftomabil joylashtirilgan !"

                    map[row][col] = [self.place , '🚘']
                    break
                i += 1
            else:
                continue
            break

        if is_valid_parking and is_valid_car:
            f_car.write(cars)
            f_parking.write(map)
        return message

    def take_away(self):
        """id , place , user_id"""
        f = File("cars.json")
        cars = f.read()
        for car in cars:
            if car.get("id") == self.id:
                if car.get("user_id") == self.user_id:
                    if car.get("place") is None:
                        return "Bu aftomabil uji olib chiqilgan !"
                    car['place'] = None
                else:
                    return "Bu aftomabil sizga tegishli emas !"
        f.write(cars)

        f = File('parking.json')
        map: list[list] = f.read()
        i = 1
        for row in range(len(map)):
            for col in range(len(map[0])):
                if i == self.place:
                    if isinstance(map[row][col], list):
                        map[row][col] = self.place
                        break
                    else:
                        return "Bu joyda aftomabil mavjud emas !"

                i += 1
            else:
                continue
            break
        f.write(map)



# c = Car(2 , "Nexia 3" , '01A222AA', user_id=2 , join_at=str(datetime.datetime.now()))
# c.save()


c = Car(1 , place=5)
print(c.placement())

# c = Car(1 , place=9 , user_id=1)
# print(c.take_away())

#
# f = File("parking.json")
# print(f.read())






