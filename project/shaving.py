import copy


class OnceAMonth(object):
    def __init__(self, day):
        self._days = [day]

    @property
    def days(self):
        return self._days

    @property
    def offset(self):
        return 1


class OnceTwoMonth(object):
    def __init__(self, day):
        self._days = [day]

    @property
    def days(self):
        return self._days

    @property
    def offset(self):
        return 2


class TwiceAMonth(object):
    def __init__(self, day1, day2):
        self._days = [day1, day2]

    @property
    def days(self):
        return self._days

    @property
    def offset(self):
        return 1


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

    def calculatePaymentTo(self, day):
        result = 0
        for intervalDay in self._interval.days:
            current_date = copy.deepcopy(self._startDate)
            current_date = current_date.replace(day=intervalDay)
            result += self.__getCostForPeriod(current_date, day)
        self._user.addSpendCash(result)


    def __getCostForPeriod(self, start, finish):
        current_date = copy.deepcopy(start)
        result = 0

        offset = self._interval.offset

        while current_date <= finish:
            result += self._product.price
            if current_date.month == (13 - offset):
                current_date = current_date.replace(year=current_date.year+1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + offset)

        return result


