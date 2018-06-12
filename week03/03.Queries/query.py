from csv import reader
from operator import itemgetter
from copy import deepcopy

filename = 'example_data.csv'


def open_file(filename):
    if isinstance(filename, str):
        with open(filename, 'r') as f:
            headers = next(f)
            data = reader(f, delimiter=',')
            result = []
            for i in data:
                result.append(i)
        return result, headers
    else:
        return filename


def filter(filename, **kwargs):
    try:
        data, headers = open_file(filename)
    except ValueError:
        headers = 'full_name favourite_color company_name email phone_number salary'
        data = filename
    # print(type(headers))
    values = []
    result = []
    rows = []
    headers = headers.split(' ')


    for i in headers[0].split(','):
        if '\n' in i:
            i = i.strip('\n')
        result.append(i)


    isThere = False

    for i in result:
        if i in kwargs.keys():
            values.append(kwargs[i])

    for i in data:
        for j in values:
            if j in i:
                isThere = True
            else:
                isThere = False
                break
        if isThere:

            rows.append(i)

    special_cases_value = ['full_name__starswith', 'email__contains', 'salary__gt', 'salary__lt', 'order__by']

    if len(rows) == 0:
        rows = data

    matrix = deepcopy(rows)

    special_headers = []


    for i in kwargs.keys():
        if i in special_cases_value:
            special_headers.append(i)


    for i in special_headers:
        if i == 'full_name__starswith':
            for row in rows:
                if not row[0].startswith(kwargs[i]):
                    if row in matrix:
                        matrix.remove(row)
                    else:
                        continue

    for i in special_headers:
        if i == 'salary__gt':
            for row in rows:
                if int(row[5]) < int(kwargs[i]):
                    if row in matrix:
                        matrix.remove(row)
                    else:
                        continue

    for i in special_headers:
        if i == 'email__contains':
            for row in rows:
                if kwargs[i] not in row[3]:
                    if row in matrix:
                        matrix.remove(row)
                    else:
                        continue

    for i in special_headers:
        if i == 'salary__gt':
                for row in rows:
                    if int(row[5]) < int(kwargs[i]):
                        if row in matrix:
                            matrix.remove(row)
                        else:
                            continue
    for i in special_headers:
        if i == 'salary__lt':
                for row in rows:
                    if int(row[5]) > int(kwargs[i]):
                        if row in matrix:
                            matrix.remove(row)
                        else:
                            continue

    for i in special_headers:
        if i == 'order__by':
            # print(i)
            # print(result.index(kwargs['order__by']))
            return sorted(matrix,key=itemgetter(result.index(kwargs['order__by'])))



    return matrix


def count(filename, **kwargs):
    data = filter(filename, **kwargs)
    return len(data)

def first(filename, **kwargs):
    data = filter(filename, **kwargs)
    return data[0]

def last(filename, **kwargs):
    data = filter(filename, **kwargs)
    return data[-1]


def test(func = filter):
   data = func(filename)
   return data


# print((filter(filename,order__by='favourite_color')))
# print(count(filename,salary__gt=5000, salary__lt=5500, email_contains='@gmail'))
# print(first(filename,salary__gt=5000, salary__lt=5500, email__contains='@gmail'))
# print(last(filename,salary__gt=5000, salary__lt=5500, email__contains='@gmail'))
# print((filter(filename,salary__gt=8000,email_contains='@gmail')))
