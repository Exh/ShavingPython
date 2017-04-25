import unittest

from shaving-service import User
from shaving-service import Subscribing
from shaving-service import OnceAMonth
from shaving-service import Product
from datetime import date

class ShavingAccessoriesTest(unittest.TestCase):
    def test_UserSpendMoneyReturn1USD_When_SubscribingConsistOf_ShaveAsProduct_OnceAMonthAsAhippingInterval_StartDate14Jan2017_Today14Jan2017(self):
        product = Product("Shave", 1)
        interval = OnceAMonth(14)
        user = User()
        subscribing = Subscribing(user, product, interval, date(2017, 1, 14))

        subscribing.calculatePayment()

        self.assertEqual(user.spendMoney, 1)

if __name__ == '__main__':
    unittest.main()
