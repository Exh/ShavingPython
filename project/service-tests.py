import unittest

from shaving import User
from shaving import Subscribing
from shaving import OnceAMonth
from shaving import OnceTwoMonth
from shaving import TwiceAMonth
from shaving import Product
from datetime import date
from shaving import ProductBuilder


class ShavingAccessoriesTest(unittest.TestCase):
    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 1, 14))

        self.assertEqual(user.spendCash, 1)

    def test_UserSpendMoneyReturn9USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = ProductBuilder().withTitle("Shave+Gel").withPrice(9).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 1, 14))

        self.assertEqual(user.spendCash, 9)

    def test_UserSpendMoneyReturn2USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 2)

    def test_UserSpendMoneyReturn12USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 12)

    def test_UserSpendMoneyReturn108USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = ProductBuilder().withTitle("Shave+Gel").withPrice(9).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 108)

    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 1)

    def test_UserSpendMoneyReturn54USD_When_SubscribingConsistOf_ShaveAndGelAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Jan2017_Today13Jan2018(self):
        product = ProductBuilder().withTitle("Shave+Gel").withPrice(9).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 13))

        self.assertEqual(user.spendCash, 54)

    def test_UserSpendMoneyReturn3USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = TwiceAMonth(14, 25)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 3)

    def test_UserSpendMoneyReturn0USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_ShippingDay28_StartDate14Jan2017_Today26Jan2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(1)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 1, 26))

        self.assertEqual(user.spendCash, 0)

    def test_UserSpendMoneyReturn7USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Feb2017_Today15Feb2018(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 2, 14))

        subscribing.calculatePaymentTo(date(2018, 2, 15))

        self.assertEqual(user.spendCash, 7)


    def test_UserSpendMoneyReturn7USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Feb2017_Today15Apr2018_StopSubscribing_25Mar2018(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 2, 14))

        subscribing.calculatePaymentTo(date(2018, 3, 25))
        subscribing.stop()
        subscribing.calculatePaymentTo(date(2018, 4, 15))

        self.assertEqual(user.spendCash, 7)

    def test_UserSpendMoneyReturn6USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Feb2017_Today25Jan2018(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 2, 14))

        subscribing.calculatePaymentTo(date(2018, 1, 25))

        self.assertEqual(user.spendCash, 6)

    def test_UserSpendMoneyReturn8USD_When_SubscribingConsistOf_ShaveAsProduct_OnceTwoMonthAsShippingInterval_StartDate14Feb2017_Today15May2018_StopSubscribing_25Mar2018_StartDate15Apr2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceTwoMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 2, 14))

        subscribing.calculatePaymentTo(date(2018, 3, 25))
        subscribing.stop()
        subscribing.start(date(2018, 4, 15))
        subscribing.calculatePaymentTo(date(2018, 5, 15))

        self.assertEqual(user.spendCash, 8)

    def test_UserSpendMoneyReturn10USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsShippingInterval_StartDate14Jan2017_Today15Feb2017_ChangeProductTo_ShaveAndGel_StartDate_1Feb2017(self):
        product = ProductBuilder().withTitle("Shave").withPrice(1).create()
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePaymentTo(date(2017, 2, 1))
        subscribing.setProduct(ProductBuilder().withTitle("Shave+Gel").withPrice(9).create())
        subscribing.calculatePaymentTo(date(2017, 2, 15))

        self.assertEqual(user.spendCash, 10)

if __name__ == '__main__':
    unittest.main()
