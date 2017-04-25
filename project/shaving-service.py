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

