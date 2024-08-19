# import pandas as pd
# import tabulate
#
#
# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3, 7, 2]
# }
# print(pd.__version__)
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)

"""===================================="""

# import pandas as pd

# names = ["John", "Karil", "Smith"]
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
#
# print(myvar["day1"])
# ======================================
# import pandas as pd

# df = pd.read_csv('users.csv')
# data_dict = df.to_dict(orient='records')
# data_string = df.to_string()
# print(type(data_string))

# ========================================
# import pandas as pd

# data = pd.read_json('cars.json')
# data.to_csv('cars.csv')
# data.to_excel('cars.xlsx')

# ========================================

# import pandas as pd
#
# p = pd.read_excel('cars.xlsx')
# data = p.iloc[:,[2, 3]]
# for i in data.to_dict(orient='records'):
#     print(i['make'] , i['model'])










