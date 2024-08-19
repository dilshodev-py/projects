from datetime import datetime

from apps import Product, Category
from apps.models import User


session_user : User | None = None
class UI:
    def main(self):
        menu = """
        1) Register
        2) Login
        3) Exit
        >>>"""
        key = input(menu)
        match key:
            case  "1" :
                self.register()
            case '2':
                self.login()
            case "3":
                print("Sog' bo'lasiz !")
                return
    def register(self):

        user = {"id" : User().sequence_id(),
                "name" : input("Name : "),
                "email" : input("email : "),
                "password" : input('Password : '),
                "join_at" : str(datetime.now())
                }
        user = User(**user)
        try:
            code = user.is_valid()
            user_code = input("Email ga yuborilgan codeni kiriting : ")
            if str(code) != user_code:
                raise Exception("Kiritilgan code xatto !")
            user.save()
            print("Success register !")
        except Exception as e:
            print(e)
        self.main()


    def login(self):
        global session_user
        user = {
            "email" : input("Email : "),
            "password": input("password : ")
        }
        try:
            session_user = User(**user).is_login()
            if session_user.get("role") == "ADMIN":
                self.admin_menu()
            else:
                self.user_menu()

        except Exception as e:
            print(e)
            self.main()
    def admin_menu(self):
        products: list = Product().process_product()
        menu = f"""
        1) category
        2) give admin
        3) new product(+{len(products)})
        0) log out
        >>>"""
        key = input(menu)
        match key:
            case "1":
                self.category()
            case "2":
                user_email = input("User email : ")
                user = User(email=user_email)
                try:
                    user.give_admin()
                    self.admin_menu()
                except Exception as e:
                    print(e)
                    self.admin_menu()
            case "3":
                self.new_products(products)
            case "0":
                self.main()

    def new_products(self , products: list):
        for place , product in enumerate(products,1):
            print(f"{place}) {product.get('name')}")
        index = int(input(">>>")) - 1
        choose_product=products[index]
        for key , value in choose_product.items():
            print(f"{key} : {value}")
        answer = input("yes/No : ")
        if answer == "yes":
            Product(**choose_product).update('is_active' , 'ACCEPTED')
        else:
            Product(**choose_product).update('is_active' , 'DENIED')

        self.admin_menu()



    def category(self):
        menu = """
        1) add
        2) update
        3) view
        4) delete
        0) <- back
        >>>"""
        key = input(menu)
        for id , category in Category().get_all().items():
            print(f"{id}) {category.get('name')}")
        match key: # TODO delete
            case "1":
                new_category = {
                    "id" : Category().sequence_id(),
                    "name" : input("Yangi kategoriya nomini kiriting : ")
                }
                Category(**new_category).save()
                print("Success create !")
                self.category()
            case "2":
                id = input(">>>")
                new_name = input("New name : ")
                Category(id = int(id)).update("name" , new_name)
                print("Success edit !")
                self.category()
            case "4":
                pass
            case "0":
                self.admin_menu()
                return
        self.category()

    def user_menu(self):
        print("Accountga hush kelibsiz")