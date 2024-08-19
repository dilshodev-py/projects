current_user  = None
def login():
    global current_user
    current_user = "response"

login()
print(current_user)