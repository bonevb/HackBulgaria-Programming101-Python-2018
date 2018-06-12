import unittest
from cashdesk import Bill, BillBatch, CashDesk


class TestBill(unittest.TestCase):

    def setUp(self):
        self.a = Bill(10)
        self.b = Bill(5)
        self.c = Bill(10)

    def test_create_value_error(self):
        with self.assertRaises(ValueError):
            Bill(-10)

    def test_create_type_error(self):
        with self.assertRaises(TypeError):
            Bill('asd')

    def test_a_isnot_b(self):
        self.assertFalse(self.a == self.b)

class TestBillBatch(unittest.TestCase):

    def test_create_billbatch(self):
        with self.assertRaises(TypeError):
            BillBatch('asd')

class TestCashDesk(unittest.TestCase):

    def create_cash_desc(self):
        with self.assertRaises(TypeError):
            CashDesk('asd')


if __name__ == '__main__':
    unittest.main()
