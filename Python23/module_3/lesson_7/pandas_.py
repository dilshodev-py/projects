# import pandas as pd
# import tabulate
#
# products = [{
#     "name": "Iphone 15",
#     "price": "10000$",
#     "quantity": 10
# },
#     {
#         "name": "Iphone 14",
#         "price": "1000$",
#         "quantity": 100
#     }
# ]

# myvar = pd.Series(product , dtype='str')
# print(myvar)

# myvar = pd.DataFrame(products)
# myvar.index = myvar.index + 1
# print(tabulate.tabulate(myvar, tablefmt='fancy_grid', headers=products[0].keys()))