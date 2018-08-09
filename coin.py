import dao


class CoinHandler:

    def __init__(self):
        json_data = dao.get_coins()
        self.listCoins = json_data
        self.categories = list(json_data.keys())

    def get_categories(self):
        return self.categories

    def contains(self, value):
        for k in self.categories:
            if value in self.listCoins.get(k):
                return True

    def add_coin(self, category, coin):
        for k in self.categories:
            if category == k:
                self.listCoins.get(k).append(coin)

    def add_category(self, category):
        self.listCoins.update({category : []})
        self.categories.append(category)

    def delete_coin(self, category, coin):
        self.listCoins.get(category).remove(coin)

    def delete_category(self, category):
        self.listCoins.pop(category, 'None')
        self.categories.remove(category)
