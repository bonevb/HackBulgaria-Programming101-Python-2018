from decorators import log
from time import sleep
from datetime import date, datetime
from contextlib import contextmanager


class performance:
    def __init__(self, filename):
        self.filename = filename
        self.filehandler = None
        self.today = None

    def __enter__(self):
        self.filehandler = open(self.filename, 'w')
        self.today = datetime.now()

    def __exit__(self, *args):
        result = datetime.now() - self.today
        self.filehandler.write('Date {}. Execution time: {}'.format(
            datetime.now(), result.seconds))
        self.filehandler.close()


# with performance('log_file.txt') as f:
#    sleep(1)


class BigError(Exception):
    pass


class assertRaises():
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type=None, exc_value=None, exc_traceback=None):
        if not exc_type:
            print('Something wrong happend!')
            return False
        if self.msg:
            if self.msg == str(exc_value) and exc_type == self.exception:
                print('OK')
                return True
            elif self.msg != str(exc_value) and exc_type == self.exception:
                print('Not OK')
                return False
        if exc_type:
            if exc_type == self.exception:
                print('OK')
                return True
            if exc_type != self.exception:
                raise BigError


# with assertRaises(ValueError, 'Test'):
#    raise ValueError('Test22')

@contextmanager
def performance(filename):
    today = datetime.now()
    yield
    with open(filename, 'w') as f:
        result = datetime.now() - today
        f.write('Date {}. Execution time: {}'.format(
            datetime.now(), result.seconds))


@contextmanager
def assertRaises(exc, msg=None):
    try:
        yield
    except Exception as e:
        #print(msg, e)
        if msg:
            if msg == str(e) and exc.__name__ == e.__class__.__name__:
                print('Ok')
                return
            elif msg != str(e) and exc.__name__ == e.__class__.__name__:
                print('The message {} is different.'.format(str(e)))
                return
        if exc.__name__ == e.__class__.__name__:
            print('Everything is fine')
            return
        if exc.__name__ != e.__class__.__name__:
            print('The exceptions are different')
            return
    else:
        print('Exception is not raised')


# with performance('domefile.txt'):
#    sleep(3)

with assertRaises(ValueError, 'Test'):
    #pass
    raise ValueError
