from DB.config import DML, DDL


class Users(DML):
    def __init__(self , **kwargs):
        self.kwargs = kwargs

    def is_valid(self):
        user = Users(username = self.kwargs.get("username")).select()
        if user:
            raise Exception("Bunday username ishlatilgan !")
        if len(self.kwargs.get("password")) < 4:
            raise Exception("Parolda xatolik")



