import unittest

from shaving import User
from shaving import Subscribing
from shaving import OnceAMonth
from shaving import OnceTwoMonth
from shaving import TwiceAMonth
from shaving import Product
from datetime import date


class ShavingAccessoriesTest(unittest.TestCase):
    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = Product("Shave", 1)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 1, 14))

        self.assertEqual(user.spendCash, 1)

    def test_UserSpendMoneyReturn9USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = Product("Shave+Gel", 9)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 1, 14))

        self.assertEqual(user.spendCash, 9)

    def test_UserSpendMoneyReturn2USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = Product("Shave", 1)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 2)

    def test_UserSpendMoneyReturn12USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = Product("Shave", 1)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 12)

    def test_UserSpendMoneyReturn108USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = Product("Shave+Gel", 9)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 108)

    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = Product("Shave", 1)
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 1)

    def test_UserSpendMoneyReturn54USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = Product("Shave+Gel", 9)
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 54)

    def test_UserSpendMoneyReturn3USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = Product("Shave", 1)
        interval = TwiceAMonth(14, 25)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 3)

if __name__ == '__main__':
    unittest.main()
