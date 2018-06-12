import sys
import os


path = sys.argv[1]
#path = '/home/dux'


def check_size(path):
    try:
        os.path.isdir(path)
    except FileNotFoundError as e:
        print(e)
    else:
        return os.path.getsize(path)


def main():
    print(check_size(path))


if __name__ == '__main__':
    main()
