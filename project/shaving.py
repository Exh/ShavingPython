import copy
from datetime import timedelta
from datetime import date

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
        self.start(start_date)
        self._lastSettlementDate = copy.deepcopy(start_date)


    def calculatePaymentTo(self, day):
        if not self._active or day < self._lastSettlementDate:
            return

        result = 0
        for intervalDay in self._interval.days:
            current_date = copy.deepcopy(self._lastSettlementDate)
            if current_date.day > intervalDay:
                newMonth = current_date.month + 1
                if newMonth > 12:
                    current_date = self.last_day_of_month(current_date.replace(year=current_date.year+1, month=1, day=28))
                    if current_date.day > intervalDay:
                       current_date = date(current_date.year, current_date.month, intervalDay)
                else:
                    current_date = self.last_day_of_month(current_date.replace(month=current_date.month + 1, day=28))
                    if current_date.day > intervalDay:
                        current_date = date(current_date.year, current_date.month, intervalDay)
            else:
                current_date = self.last_day_of_month(current_date.replace(day=28))
                if current_date.day > intervalDay:
                   current_date = date(current_date.year, current_date.month, intervalDay)
            result += self.__getCostForPeriod(current_date, day)
        self._user.addSpendCash(result)
        self._lastSettlementDate = day + timedelta(days=1)


    def stop(self):
        self._active = False


    def start(self, start_date):
        self._startDate = start_date
        self._active = True


    def __getCostForPeriod(self, start, finish):
        current_date = copy.deepcopy(start)
        result = 0

        offset = self._interval.offset

        while current_date <= finish:            
            result += self._product.price
            if current_date.month >= (13 - offset):
                newMonth = offset - (12 - current_date.month)
                current_date = self.last_day_of_month(current_date.replace(year=current_date.year+1, month=newMonth, day=28))

                if current_date.day > start.day:
                    current_date = date(current_date.year, current_date.month, start.day)
            else:                
                tMonth = current_date.month + offset
                current_date = self.last_day_of_month(current_date.replace(month=tMonth, day=28))

                if current_date.day > start.day:
                    current_date = date(current_date.year, current_date.month, start.day)

        return result


    def setProduct(self, product):
        self._product = product


    def setInterval(self, interval):
        self._interval = interval

    def last_day_of_month(self, any_day):
        next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
        return next_month - timedelta(days=next_month.day)

    @property
    def active(self):
        return self._active

    @property
    def last_payment_date(self):
        return self._lastSettlementDate

class ProductBuilder(object):
    def __init__(self):
        self._title = ""
        self._price = 0

    def create(self):
        return Product(self._title, self._price)

    def withTitle(self, title):
        self._title = title
        return self

    def withPrice(self, price):
        self._price = price
        return self


def getProducts():
    getProducts.products = []
    getProducts.products.append(ProductBuilder().withTitle("Shave").withPrice(1).create())
    getProducts.products.append(ProductBuilder().withTitle("Shave+Gel").withPrice(9).create())
    getProducts.products.append(ProductBuilder().withTitle("Shave+Gel+Balm").withPrice(19).create())
    return getProducts.products


