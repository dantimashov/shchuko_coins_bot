def categories_to_string(array):
    result = "Категории:\n"
    for el in array:
        result += el + "\n"
    return result


def coins_to_string(dct):
    result = ""
    for k in dct.keys():
        result += k + ": \n"
        for coin in dct.get(k):
            result += coin + "\n"
        result += "\n"
    return result
