# user = {
#     "id" : "id",
#     "fullname" : "fullname"
# }

# users.txt
# function
#     user_add(user)
#     user_delete(user_id)
#     user_update(user_id , filed , new_value)
#     user_detail(user_id)

def user_add(user: dict):
    user_str = "|".join(map(str, user.values()))
    with open("users.txt", "r") as f:
        users = f.read().split('\n') # [""]
    if "" in users:
        del users[0]
    users.append(user_str)
    data = "\n".join(users)
    with open("users.txt", "w") as f:
        f.write(data)


def user_delete(user_id):
    with open("users.txt", "r") as f:
        users = f.read().split("\n")
    for user in users:
        if int(user.split('|')[0]) == user_id:
            users.remove(user)
    data = "\n".join(users)
    with open("users.txt", "w") as f:
        f.write(data)


def user_update(user_id , filed , new_value):
    with open("users.txt", "r") as f:
        users = f.read().split("\n")
    for i , user in enumerate(users):
        user = user.split('|')
        if int(user[0]) == user_id:
            if filed == "id":
                user[0] = new_value
            if filed == "fullname":
                user[1] = new_value
            users[i] = "|".join(map(str , user))
    data = "\n".join(users)
    with open("users.txt", "w") as f:
        f.write(data)


def user_detail(user_id):
    with open("users.txt", "r") as f:
        users = f.read().split("\n")
    for user in users:
        user = user.split("|")
        if int(user[0]) == user_id:
            return user


# Leetcode -> Sunatilo

# user = {
#     "id": 10,
#     "fullname": "Po'lat",
# }

# user_add(user)
# user_delete(3)


