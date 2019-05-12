def categories_to_string(array):
    result = "Категории:\n"
    for el in array:
        result += el + "\n"
    return result


def check_result(coin_is_contained):
    return "Монета уже есть" if coin_is_contained else "Монеты пока нету в списке. Сохраните ее, пожалуйста."
