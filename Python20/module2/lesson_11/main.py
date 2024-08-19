# #
# # import json
# # class JsonFile:
# #     def __init__(self , file_path):
# #         self.file_path = file_path
# #
# #     def read(self):
# #         with open(self.file_path , "r") as f:
# #             data = json.load(f)
# #         return data
# #
# #     def write(self , data):
# #         with open(self.file_path ,'w') as f:
# #             json.dump(data ,  f , indent=3)
# #
# #     def clear(self):
# #         self.write([])
# #
# #
# #
# #
# #
# # class TextFile:
# #     def __init__(self, file_path):
# #         self.file_path = file_path
# #
# #     def read(self):
# #         with open(self.file_path, "r") as f:
# #             data = f.read()
# #         return data
# #
# #     def write(self, data):
# #         with open(self.file_path, 'w') as f:
# #             f.write(data)
# #
# #     def clear(self):
# #         self.write("")
# #
#
#
# with open("matem_ifoda.txt" , 'r') as f:
#     matem_ifoda = f.read()
#     print(matem_ifoda)
#     try:
#         print(eval(matem_ifoda))
#     except:
#         print("Matematika ifodada xatto bor")
#
# print(eval("10 + 20 - (90)"))
#
# i = """
# """
# exec(compile(i, " " , "exec"))
