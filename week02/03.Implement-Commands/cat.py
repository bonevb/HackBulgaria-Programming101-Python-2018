# cat.py
import sys

arguments = sys.argv[1]
# print(arguments)


def cat(arguments):
    filename = arguments
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
        	print(line)


def main():
    cat(arguments)


if __name__ == '__main__':
    main()
