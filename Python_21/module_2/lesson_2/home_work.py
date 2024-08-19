
users = []

class User:
    def __init__(self, id ,
                 fullname ,
                 phone,
                 email ,
                 role ,
                 join_at):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.role = role
        self.join_at = join_at


    def check_email(self):
        if not ("@" in self.email and self.email.endswith(".com")):
            return False,"Invalid email"
        return True,"Correct email"

    def save(self):
        res: tuple = self.check_email()
        if not res[0]:
            return res[1]
        users.append(self)
        return res[1]

    def delete(self, user_id):
        for user in users:
            if user.id == user_id:
                users.remove(user)

    def update(self , field , new_val):
        for user in users:
            if user.id == self.id:
                if field == "fullname":
                    user.fullname = new_val
                if field == "phone":
                    user.phone = new_val
                if field == "email":
                    user.email = new_val
                if field == "role":
                    user.role = new_val

    def get_user(self, user_id):
        for user in users:
            if user_id == user.id:
                return user.__dict__
    def __repr__(self):
        return f"{self.role}"



# user1 = User(1 , "Karl" , "+98994567890" , "karl@gmail.com" , "ADMIN" , "2024-01-20")

# print(user1.save())
# print(user1.get_user(1))
# user1.update("role" , "USER")
# print(user1.get_user(1))




# class A:
#     def __init__(self , a  , b):
#         self.a = a
#         self.b = b
#
# a = A(1,2)
# l = [a]
# print(id(a))
# # l[0].b = 10
# print(id(l[0]))






