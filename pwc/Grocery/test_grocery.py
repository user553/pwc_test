import unittest
from grocery import Store

class TestCases(unittest.TestCase):

    def test_cases_getSubTotal(self):
        Store.cart = {'soup': 0.65, 'bread': 0.80, 'milk': 1.3, 'apple': 1}
        result = Store.checkout(self.cart)
        self.assertEqual(Store.getSubTotal(result), 3.75)

    def test_cases_getDiscount(self):
        pass

if __name__ == '__main__':
    unittest.main()