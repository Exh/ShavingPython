import unittest

from shaving import User
from shaving import Subscribing
from shaving import OnceAMonth
from shaving import Product
from datetime import date


class ShavingAccessoriesTest(unittest.TestCase):
    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsAhippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = Product("Shave", 1)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePayment()

        self.assertEqual(user.spendCash, 1)

    def test_UserSpendMoneyReturn9USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceAMonthAsAhippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = Product("Shave+Gel", 9)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePayment()

        self.assertEqual(user.spendCash, 9)


if __name__ == '__main__':
    unittest.main()
