
users: list['User'] = []
class User:
    def __init__(self ,
                 id : int,
                 fullname: str ,
                 phone : str,
                 email : str ,
                 role : str ,
                 join_at : str):
        self.id = id
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.role = role
        self.join_at = join_at
    def save(self):
        users.append(self)

    def delete(self):
        for user in users:
            if user.id == self.id:
                users.remove(user)
    def update(self , field , new_val):
        for user in users:
            if user.id == self.id:
                if field == "fullname":
                    user.fullname = new_val
                if field == "phone":
                    user.phone = new_val
                if field == 'email':
                    user.email = new_val
                if field == 'role':
                    user.role = new_val

    def get(self):
        for user in users:
            if user.id == self.id:
                return user
        else:
            return "Not Found !"

# C - create
# R - read
# U - update
# D - delete
user1  = {
    "id" : 1,
    "fullname" : "Botir",
    "phone" : "+998991234567",
    "email" : "botir@gmail.com",
    "role" : "ADMIN",
    "join_at" : "2024-02-12 18:17:56",
}
u1 = User(**user1)
u1.save()
u1.update("role" , "USER")
print(u1.get().role)
print(users[0].role)




