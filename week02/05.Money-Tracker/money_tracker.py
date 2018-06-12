from operator import itemgetter

import sys

name = 'Boby'
#name = sys.argv[1]
file = 'money_tracker.txt'
deposits = []
expenses = []
result = []
user_savings = []
action_per_day = []

savings = ['Deposit', 'Savings', 'Salary']
expenses = ['Eating Out', ' Clothes', 'Food',
            'House', 'Pets', 'Bills', 'Transport']


def list_user_data():
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')


def show_user_savings():
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for i in savings:
                if i in line:
                    a, b, c = line.split(',')
                    user_savings.append((a, b))

    return user_savings


def show_user_deposits():
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'Deposit' in line:
                a, b, c = line.split(',')
                deposits.append((a, b))
    return deposits


def show_user_expenses():
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'Expense' in line:
                a, b, c = line.split(',')
                expenses.append((a, b))
    return expenses


def list_user_expenses_ordered_by_categories():
    user_expenses = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'New Expense' in line:
                print(line, end='')
                a, b, c = line.split(',')
                user_expenses.append((float(a), b))
        result = sorted(user_expenses, key=itemgetter(1))

    return result


def show_user_data_per_date():
    date = input('Choose date in format dd-mm-yyyy ')
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if date in line:
                start = True
                if start:
                    index = lines.index(line)
                    for i in lines[index + 1:]:
                        if '=' not in i:
                            action_per_day.append((i.strip('\n'),))

    return action_per_day


def list_income_categories():
    print(savings)


def list_expense_categories():
    print(expenses)


def add_income(income_category, money, date):
    dateExists = False
    if income_category not in savings:
        savings.append(income_category)
    with open(file, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if date in line:
                dateExists = True
                f.writelines('{}, {}, {}'.format(
                    money, income_category, 'New Income\n'))
        if not dateExists:
            f.writelines('{}{}{}'.format('=== ', date, ' ===\n'))
            f.writelines('{}, {}, {}'.format(
                money, income_category, 'New Income\n'))


def add_expense(expense_category, money, date):
    dateExists = False
    if expense_category not in expenses:
        expenses.append(expense_category)
    with open(file, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if date in line:
                dateExists = True
                f.writelines('{}, {}, {}'.format(
                    money, expense_category, 'New Expense\n'))
        if not dateExists:
            f.writelines('{}{}{}'.format('=== ', date, ' ===\n'))
            f.writelines('{}, {}, {}'.format(
                money, expense_category, 'New Expense\n'))


def menu(name):
    print('Hello, ', name)
    while True:
        choice = int(input("""Choose one of the following options to continue:
    1 - show all data
    2 - show data for specific date
    3 - show expenses, ordered by categories
    4 - add new income
    5 - add new expense
    6 - exit
    """))
        if choice == 6:
            print('Goodbye, ', name)
            break
        elif choice == 1:
            list_user_data()
        elif choice == 2:
            a = show_user_data_per_date()
            print(a)
        elif choice == 3:
            b = list_user_expenses_ordered_by_categories()
            print(b)
        elif choice == 4:
            money = input('New income amount: ')
            income_category = input('New income type: ')
            date = input('New income date in format dd-mm-yyyy: ')
            c = add_income(income_category, money, date)
            print(c)
        elif choice == 5:
            money = input('New expense amount: ')
            income_category = input('New expense type: ')
            date = input('Enter date in format mm-dd-yyyy: ')
            d = add_expense(income_category, money, date)
            print(d)
        else:
            print('Invalid choise')


# print(show_user_data_per_date())
print(menu(name))
# print(list_income_categories())
# print(list_expense_categories())
# print(show_user_savings())
# print(show_user_deposits())
# print(show_user_expenses())
#print(add_expense('Internet', 20,'26-03-2018'))
