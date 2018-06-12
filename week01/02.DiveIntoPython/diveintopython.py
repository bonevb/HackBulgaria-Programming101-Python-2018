from math import sqrt

def count_substrings(haystack, needle):
    a = haystack.split(' ')
    counter = 0
    for i in a:
        if needle in i:
            step = len(i) - len(needle)
            if len(i) > len(needle):
                for j in range(0, len(i), step):
                    if needle in i[j:step + j]:
                        counter += 1
            else:
                counter += 1

    return counter

#print(count_substrings("babababa", "baba"))


m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


def sum_of_matrix(n):
    return sum([j for i in n for j in i])


#print(sum_of_matrix(m))


def nan_expand(n):
    result = 'Not a '
    if n == 0:
        return ""
    else:
        return result * n + 'NaN'

#print(nan_expand(3))


items = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]


def max_consecutive(items):

    max_counter = 0
    for i in range(len(items)):
        counter = 0
        j = i
        for p in range(j, len(items)):
            if items[i] == items[p]:
                counter += 1
            else:
                break
        if counter > max_counter:
            max_counter = counter

    return max_counter


#print(max_consecutive(items))


from itertools import groupby


n = [1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 3, 3, 3, 3]


def group(n)
    
	groups = []
	keys = []

	for key, group in groupby(n):
		groups.append(list(group))
		keys.append(key)
	return groups


print(groups)


def prime_numbers(n):
    primes = []

    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime is True:
            primes.append(i)
    return primes

def prime_factorization(n):
    prime_nums = prime_numbers(n)
    result = []
    if n in prime_nums:
        result.append((n, 1))
        return result
    for i in prime_nums:
        while n % i == 0:
            result.append(i)
            n = n / i
        if n == 1:
            break
    factors = []
    occur = set(result)
    for i in occur:
        factors.append((i, result.count(i)))
    return sorted(factors)


#print(prime_factorization(356))




def count_word():
    word = input('Write your word: ')
    rows = int(input('Enter number of rows '))
    cols = int(input('Enter number of cols '))
    diag = sqrt(rows ** 2 + cols ** 2)

    if len(word) > rows or len(word) > cols or len(word) > diag:
        print('Your word is too long')
        return None

    matrix = []
    counter = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            ch = input('Enter a char ')
            row.append(ch)
        matrix.append(row)

    for i in range(rows):
        p = []
        for j in range(cols):
            p.append(matrix[i][j])
        a = ''.join(p)
        if word in a or word in a[::-1]:
            counter += 1

    for i in range(cols):
        p = []
        for j in range(rows):
            p.append(matrix[j][i])
        a = ''.join(p)
        if word in a or word in a[::-1]:
            counter += 1

    fdiag = [[] for i in range(rows + cols - 1)]
    bdiag = [[] for i in range(len(fdiag))]
    min_bdiag = -rows + 1

    for i in range(rows):
        for j in range(cols):
            fdiag[j+i].append(matrix[i][j])
            bdiag[-min_bdiag+j-i].append(matrix[i][j])

    for i in fdiag:
        i = ''.join(i)
        if word in i or word in i[::-1]:
            counter += 1
    for i in bdiag:
        i = ''.join(i)
        if word in i or word in i[::-1]:
            counter += 1




    return counter


print(count_word())

def gas_stations(distance, tank_size, stations):
    result = []
    while tank_size < distance:
        stations.append(tank_size)
        stations = sorted(stations)
        curr_position = stations.index(tank_size) - 1
        result.append(stations[stations.index(tank_size) - 1])
        stations.remove(tank_size)
        stations = stations[curr_position:]
        tank_size = stations[0] + 90
    return result


#print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))