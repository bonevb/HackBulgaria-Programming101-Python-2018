#first task

import sys
from datetime import datetime



def return_sum():
    print('Input your data and press Ctrl + D')
    data = sys.stdin.readlines()
    data = list(data)
    today = data.pop()
    data.pop()
    day, month, year = today.split('/')
    sum = 0

    date1 = datetime(int(year), int(month), int(day))

    for line in data:
        amount, den = line.split(',')
        day, month, year = den.split('/')
        date2 = datetime(int(year), int(month), int(day))
        if date1 >= date2:
            sum += int(amount)
        result = 0

    if sum > 0:
        result = '+{}'.format(sum)
        return result
    elif sum < 0:
        result = '={}'.format(sum)
        return result
    else:
        return sum



#print(return_sum())
