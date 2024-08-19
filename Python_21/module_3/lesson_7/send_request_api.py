# requests
# httpx
"""
    protocol
        get    -> olish
        post   -> data yuborish
        patch  -> qisman update
        put    -> to'liq update
        delete -> o'chirish

"""

# import httpx
# http://10.10.2.186:8000/swagger/
# response = httpx.get("http://10.10.2.186:8000/categories")
# category_id = input("Category Id : >>>")
# response = httpx.get(f"http://10.10.2.186:8000/categories/{category_id}")
# data = response.json()
# for key , value in data.items():
#     print(key , value)

# ========================= category menu ========================

"""
1) category list
2) category detail
3) exit
            -------------------- category list ---------------------------
            id) category name
            id) category name
            id) category name
            id) category name
            <-category menu
            -------------------- category detail ---------------------------
            id) category name
            id) category name
            id) category name
            id) category name
            Category Id >>>
                {"id" : Id , "name" : category_name , ....}
            <-category menu


"""
# class UI:
#     def category_list(self):
#         link = "http://10.10.2.186:8000/categories"
#         response = httpx.get(link)
#         categories = response.json()
#         for category in categories:
#             print(f"{category.get('id')}) {category.get('name')}")
#
#     def category_detail(self):
#         self.category_list()
#         id = input("ID >>>")
#         link = f"http://10.10.2.186:8000/categories/{id}"
#         response = httpx.get(link)
#         category = response.json()
#         print(category)
#
#
#     def main(self):
#         menu = """
#         1) category list
#         2) category detail
#         3) exit
#         >>>
#         """
#         key = input(menu)
#         match key:
#             case "1":
#                 self.category_list()
#                 self.main()
#             case "2":
#                 self.category_detail()
#                 self.main()
#             case "3":
#                 return
#
# UI().main()


# ===========================================

import httpx
# link = "http://10.10.2.186:8000/products/create"
#
# param = {
#   "name": "Nexia 1",
#   "price": 2000,
#   "description": "eski",
#   "is_premium": True,
#   "is_new": True,
#   "category": 7
# }
#
# data = {
# "uname": "absaitovdev3233@gmail.com",
# "pw1": 123456,
# "dosavecreate": "Create Account"
# }
#
# response = httpx.post("https://codingbat.com/pref", data=data)
# print(response.status_code)











