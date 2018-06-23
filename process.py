import functools

@functools.singledispatch
def getName(a):
    type_name = type(a).__name__
    assert False, "Unsupported type : " + type_name

@getName.register(int)
def _(a):
    if (a == 0):
        return 'Ноль'
    elif (a == 1):
        return 'Один'
    elif (a == 2):
        return 'Два'
    elif (a == 3):
        return 'Три'
    elif (a == 4):
        return 'Четыре'
    elif (a == 5):
        return 'Пять'
    elif (a == 6):
        return 'Шесть'
    elif (a == 7):
        return 'Семь'
    elif (a == 8):
        return 'Восемь'
    elif (a == 9):
        return 'Девять'

@getName.register(str)
def _(a):
    return a