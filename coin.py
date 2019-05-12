import dao


class CoinHandler:

    def __init__(self):
        lst_data = dao.get_coins().split("\r\n")
        self.listCoins = list(filter(lambda s: s and ':' not in s, lst_data))
        self.categories = list(filter(lambda s: s and ':' in s, lst_data))

    def contains(self, value):
        return value in self.listCoins
