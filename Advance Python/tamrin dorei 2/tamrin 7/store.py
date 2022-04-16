from models import User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if not product in self.products or self.products[product] < amount:
            raise Exception("Not Enough Products")
        else:
            self.products[product] -= amount
            if self.products[product] == 0:
                del self.products[product]

    def add_user(self, username):
        for user in self.users:
            if username == user.username:
                return None
        user = User(username)
        self.users.append(user)
        return username

    def get_total_asset(self):
        sum = 0
        for key in self.products.keys():
            sum += key.price * self.products[key]
        return sum

    def get_total_profit(self):
        sum = 0
        for user in self.users:
            for product in user.bought_products:
                sum += product.price
        return sum

    def get_comments_by_user(self, user):
        comment_list = []
        for product in self.products:
            for comment in product.comments:
                if comment.user == user:
                    comment_list.append(comment.text)
        return comment_list

    def get_inflation_affected_product_names(self):
        result = []
        for product in self.products:
            for instance in self.products:
                if product.name == instance.name and product.price != instance.price:
                    result.append(product.name)
                    continue
        return list(set(result))

    def clean_old_comments(self, date):
        for product in self.products:
            result = []
            for comment in product.comments:
                if date < comment.date_added:
                    result.append(comment)
            product.comments = result

    def get_comments_by_bought_users(self, product):
        result = []
        for comment in product.comments:
            if product in comment.user.bought_products:
                result.append(comment.text)
        return result