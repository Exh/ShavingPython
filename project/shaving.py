class OnceAMonth(object):
    def __init__(self, day):
        self._days = [day]

    @property
    def days(self):
        return self._days


class User(object):
    def __init__(self):
        self._spendCash = 0

    @property
    def spendCash(self):
        return self._spendCash

    def addSpendCash(self, cash):
        self._spendCash += cash


class Product(object):
    def __init__(self, title, price):
        self._title = title
        self._price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, v):
        self._title = v

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v):
        self._price = v


class Subscribing(object):
    def __init__(self, user, product, interval, start_date):
        self._user = user
        self._product = product
        self._interval = interval
        self._startDate = start_date

    def calculatePayment(self):
        self._user.addSpendCash(self._product.price)