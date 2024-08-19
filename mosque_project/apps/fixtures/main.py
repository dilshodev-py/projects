import datetime
import json

# =================================================================
# transaction_types = ['Болаларга ном қўйишдан', 'Никоҳдан', 'Жанозадан', 'Суннат ва никоҳ тўйидан', 'Тиловат куръондан', 'Хатми куръондан', 'Худойидан', 'Мавлуд ўтказишдан', 'Ифторликдан', 'Закот ва Фитр- садақадан', 'Рамазон ҳайитидан', 'Қурбон хайитидан', 'Келган жонликлардан ', 'Тушган тўн ва бошқа матолар', 'Иона қутилари ', 'Бошқа тушумлар (Пейми)', 'Гиламлар', 'Ҳайр-эҳсонлар', '"ВАКФ" хайрия фонди', 'Беморларга Хайрия', 'Нотўғри ўтказилган пул қайтиши', 'Намозхонлардан обуна учун']
# data = []
# for i, v in enumerate(transaction_types,1):
#     d = {
#       "model": "mosque.TransactionType",
#       "pk": i,
#       "fields": {
#          "name": v,
#          "income": True
#       }
#     }
#     data.append(d)
#
# with open("transaction_type.json", "w") as f:
#     json.dump(data , f , indent=3)
from os.path import join

from root.settings import BASE_DIR

"""-------------------------------------------------------------------------"""

# roles = ['Имом хатиб ', 'Имом ноиб', 'Отиной', 'Бош ҳисобчи ', 'Мутавали', 'Муаззин ', 'Ошпаз', 'Электрик', 'Сантехнак', 'Овоз созловчи', 'Қоровул', 'Фаррош ']
#
# data = []
# for i, role in enumerate(roles,1):
#     d = {
#       "model": "apps.UserRole",
#       "pk": i,
#       "fields": {
#          "name": role,
#       }
#     }
#     data.append(d)
#
def moliya_header() -> list:
    with open(join(BASE_DIR, 'apps', 'fixtures' , 'moliya_headers_column.json' ), "r") as f:
        data = json.load(f)
    return data




