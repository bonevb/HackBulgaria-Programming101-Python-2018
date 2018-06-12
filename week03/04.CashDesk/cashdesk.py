def count(a, str):
    counter = 0
    for i in str:
        if a == i:
            counter += 1
    return counter


class Bill():
    def __init__(self, amount):
        self.amount = amount
        if not isinstance(self.amount, int):
            raise TypeError('Inappropriate type argument')
        if self.amount < 0:
            raise ValueError

    def __int__(self):
        return int(self.amount)

    def __eq__(self, value):
        return self.amount == value

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "A {}$ bill".format(self.amount)

    def __hash__(self):
        return hash(self.amount)


class BillBatch():
    def __init__(self, bills):
        self.bills = bills
        if not isinstance(self.bills, list):
            raise TypeError

    def __len__(self):
        counter = 0
        for i in self.bills:
            counter += 1
        return counter

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


class CashDesk():

    total_money = []

    def take_money(self, value):
        if not isinstance(value, Bill) or not isinstance(value, BillBatch):
            raise TypeError
        if isinstance(value, BillBatch):
            for i in value:
                self.total_money.append(int(i))
        else:
            self.total_money.append(value)

    def __getitem__(self, index):
        return self.total_money[index]

    def total(self):
        return sum([int(bill) for bill in self.total_money])


    def inspect(self):
        self.number_of_bills = [int(i) for i in self.total_money]
        self.keys = set(self.number_of_bills)
        self.my_dict = {}
        for i in self.keys:
            self.my_dict[i] = count(i, self.total_money)
        for key, value in self.my_dict.items():
            print('{}$ bills - {}'.format(key, value))
