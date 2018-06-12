from string import ascii_lowercase


def sum_of_digits(n):
    n = abs(n)
    return sum([int(i) for i in str(n)])


# print(sum_of_digits(-12))

def to_digits(n):
    return [int(i) for i in str(n)]

# print(to_digits(123456))


def to_number(digits):
    a = [str(i) for i in digits]
    b = ''.join(a)
    return int(b)


#print(to_number([9, 9, 9, 9, 9]))


def factorial(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i - 1)


def fact_digits(n):
    a = [int(i) for i in str(n)]
    return sum([factorial(i) for i in a])
#    return a

# print(factorial(5))


#print(fact_digits(111))
def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    a, b = 1, 1
    c = []
    c.append(a)
    c.append(b)
    i = 1
    while i < n - 1:
        a, b = b, a + b
        c.append(b)
        i += 1
    return c

#print(fibonacci(10))


def fib_number(n):
    c = fibonacci(n)
    return to_number(c)


#print(fib_number(3))


def palindrome(n):
    a = str(n)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

# print(palindrome("baba"))


vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']


def count_vowels(str):
    counter = 0
    for i in str:
        if i in vowels:
            counter += 1
    return counter


#print( count_vowels("Theistareykjarbunga"))


lower_alphabet = 'bcdfghjklmnpqrstvwxz'

upper_alphabet = lower_alphabet.upper()


up_and_low_alphabet = lower_alphabet + upper_alphabet


def count_consonants(str):
    counter = 0
    for i in str:
        if i in up_and_low_alphabet:
            counter += 1
    return counter

#print(count_consonants("Python"))


a = ascii_lowercase
b = a.upper()
c = a + b


#print (c)


def count(a, str):
    counter = 0
    for i in str:
        if a == i:
            counter += 1
    return counter


def char_histogram(string):
    a = dict()

    for i in string:
        a[i] = count(i, string)
    return a


#print (char_histogram("AAAAaaa!!!"))
