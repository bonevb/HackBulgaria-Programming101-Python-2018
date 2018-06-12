from string import ascii_lowercase, ascii_uppercase
from copy import copy
from datetime import datetime
from functools import wraps
import time

def accepts(*args):
    def accepter(func):
        def decorated(*item):
            for i in range(len(args)):
                if not isinstance(item[i], args[i]):
                    raise TypeError('Argument {} of {} is not {}'.format(i+1, func.__name__, args[i]))
            return func(*item)
        return decorated
    return accepter

def encrypt(number):
    def accepter(func):
        @wraps(func)
        def decorated():
            lowercase = ascii_lowercase * 2
            uppercase = ascii_uppercase * 2
            result = func() 
            list_from_result = list(result)
            changed_result = []
            for i in list_from_result:
                if i in ascii_lowercase:
                    changed_result.append(lowercase[lowercase.index(i) + number])
                elif i in ascii_uppercase:
                    changed_result.append(uppercase[uppercase.index(i) + number])
                else:
                    changed_result.append(i)

            return ''.join(changed_result)
        return decorated
    return accepter


def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorated():
            with open(file_name, 'a') as f:
                today = datetime.now()
                result = '{} was called at {}'.format(func.__name__, today)
                f.writelines(result + '\n')
        return decorated
    return accepter

def performance(filename):
    def accepter(func):
        @wraps(func)
        def decorated():
            start = time.time()
            result = func()
            end = time.time()
            print(func.__name__, end-start)
            with open(filename, 'a') as f:
                f.writelines('{} was called and took {} seconds to complete\n'.format(func.__name__, end - start))
            return result
        return decorated
    return accepter


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"

print(something_heavy())



@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

#get_low()

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

#say_hello(4)

#TypeError: Argument 1 of say_hello is not str!

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

#print(say_hello("Hacker"))

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

#print(deposit("RadoRado", 10))
