import unittest
from query import filter


class QueryTest(unittest.TestCase):

    test_data = [['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
                ['Deborah Lopez', 'blue', 'Henson-Pearson', 'mclaughlintony@gmail.com', '(783)023-6489', '5067'],
                ['Deborah Lopez', 'silver', 'Willis Inc', 'stricklandjessica@gmail.com', '422.395.8104', '5090'],
                ['Todd Delacruz', 'teal', 'Peterson-Kennedy', 'joseph42@gmail.com', '871.611.2902x818', '5216'],
                ['John Horn', 'lime', 'Ochoa, Hayes and Jackson', 'reyesglenn@yahoo.com', '(563)552-6476x2328', '5321'],
                ['Barbara Odonnell', 'gray', 'Meyer-Walters', 'craigdebra@gmail.com', '468-236-7320x1322', '5253'],
                ['Megan Taylor', 'fuchsia', 'Henderson LLC', 'barrymeredith@hotmail.com', '(864)796-1576x58695', '5442'],
                ['Kevin Burns', 'lime', 'Jackson-Harrison', 'joshua56@gmail.com', '1-004-688-3856x1145', '5395'],
                ['Angela Jenkins', 'gray', 'Bates-Hoffman', 'aliciaglass@gmail.com', '(132)955-1528', '5001']
                 ]

    def test_filter_one_name(self):
        self.assertEqual(filter(self.test_data, full_name='Diana Harris'),[['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354']])

    def test_filter_two_names(self):
        self.assertEqual(filter(self.test_data, full_name='Deborah Lopez'),[['Deborah Lopez', 'blue', 'Henson-Pearson', 'mclaughlintony@gmail.com', '(783)023-6489', '5067'],['Deborah Lopez', 'silver', 'Willis Inc', 'stricklandjessica@gmail.com', '422.395.8104', '5090']])

    def test_salary_gt(self):
        self.assertEqual(filter(self.test_data,salary__gt=5400),[['Megan Taylor', 'fuchsia', 'Henderson LLC', 'barrymeredith@hotmail.com', '(864)796-1576x58695', '5442']])


    def test_salay_gt_salary_lt(self):
        self.assertEqual(filter(self.test_data, salary__gt=5000, salary__lt=5005),[['Angela Jenkins', 'gray', 'Bates-Hoffman', 'aliciaglass@gmail.com', '(132)955-1528', '5001']])


    def test_filter_name_starts_with(self):
        self.assertEqual(filter(self.test_data, full_name__starswith='Deborah Lopez'),[['Deborah Lopez', 'blue', 'Henson-Pearson', 'mclaughlintony@gmail.com', '(783)023-6489', '5067'],['Deborah Lopez', 'silver', 'Willis Inc', 'stricklandjessica@gmail.com', '422.395.8104', '5090']])

    def test_email_contains(self):
        self.assertEqual(filter(self.test_data, email__contains='@hotmail'),[['Megan Taylor', 'fuchsia', 'Henderson LLC', 'barrymeredith@hotmail.com', '(864)796-1576x58695', '5442']])


if __name__ == '__main__':
    unittest.main()

