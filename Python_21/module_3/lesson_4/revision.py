# try except
# logging

# try:
    # register
    #     >>>fullname
    #     >>>username
    #     >>>password 123
#     raise Exception("Hello")
# except Exception as m:
#     print(m)
#
#
# def div(num , num2):
#     return num / num2

# try:
#     result = div(10,0)
#     print(result)
# except Exception as m:
#     print(m)
# else:
#     pass
# finally:
#     pass

# ================== logging =============================

import logging

"""
level 
    debug 1
    info  2
    warning 3
    error 4
    critical 5
"""
logging.basicConfig(level=30)
logging.warning("Message warning !")






