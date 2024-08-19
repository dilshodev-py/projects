# decorator


def decorator(num):
    def inner(func_name):
        def wrapper(*args):
            return func_name(*args)

        return wrapper
    return inner


@decorator(1)
def add(*args):
    pass

add(1, 2)
