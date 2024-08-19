class User:
    def __init__(self, fullname: str = None, email: str = None, phone: str = None, mobile: str = None,
                 address: str = None):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.address = address


class Job:
    def __init__(self, job_name: str = None, address: str = None, country: str = None):
        self.job_name = job_name
        self.address = address
        self.country = country


# obj = Job("Web Designer" , "Bootdey.com LLC." , "Uzbekistan")
# obj2 = Job("Web Developer" , "Bootdey.com LLC." , "USA")
# obj3 = Job("Fronted Developer" , "Bootdey.com LLC." , "Africa")
# obj4 = Job("Web Designer" , "Bootdey.com LLC." , "Mongoliya")
# obj5 = Job("Web Designer" , "Bootdey.com LLC." , "Uzbekistan")
# obj6 = Job("Web Designer" , "Bootdey.com LLC." , "Uzbekistan")


# class Task:
#     def __init__(self , name : str = None , progress : str = None , due_date : str = None ):
#         self.name = name
#         self.progress = progress
#         self.due_date = due_date


# obj = Task("Exommerce website" , '70 %' , '2018-01-20')
# obj2 = Task("Android app" , '30 %' , '2018-09-11')
# obj3 = Task("Logo Design" , '40 %' , '2018-04-12')
# obj4 = Task("Java Project" , '35 %' , '2018-01-20')

class Card:
    def __init__(self, card_holder: str, card_number: int, exprition_date: str, cvs: int):
        self.card_holder = card_holder
        self.card_number = card_number
        self.exprition_date = exprition_date
        self.cvs = cvs


# obj = Card("card_holder" , 860054125689654 , "2024-05-09"  , 456)
# obj2 = Card("card_owner" , 860054328974562 , "2024-05-09"  , 427)

class Contact:
    def __init__(self, full_name: str,
                 job_name: str,
                 email: str, phone: str,
                 link_facebook: str,
                 link_twitter: str,
                 link_scype: str,
                 photo: str):
        self.full_name = full_name
        self.job_name = job_name
        self.email = email
        self.phone = phone
        self.link_scype = link_scype
        self.link_twitter = link_twitter
        self.link_facebook = link_facebook
        self.photo = photo


obj = Contact('Emma A Main',
              'Graphis Design',
              'paul@gmail.com',
              "+99899583234",
              'asfdasd',
              'asfasf',
              'sadfasf',
              'afsa',)



# ============================================

class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products : list[Product] = []
product1 = Product("Iphone 15 Pro Max" , "1300" , 50)
product2 = Product("Iphone 14 Pro Max" , "1000" , 20)

products.append(product1)
products.append(product2)

for product in products:
    print(f"""
    name : {product.name}
    price : {product.price}
    """)
