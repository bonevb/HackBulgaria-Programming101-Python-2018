import sys

filename = sys.argv[2]
mode = sys.argv[1]

# print(filename)


def number_of_chars(mode, filename):
    counter = 0
    if mode == 'char':
        with open(filename, 'r') as f:
            a = f.read()
            for i in a:
                counter += 1

    elif mode == 'words':
        with open(filename, 'r') as f:
            a = f.read()
            a = list(a.split(' '))
            print(a)
            for i in a:
                counter += 1
    return counter


def main():
    print(number_of_chars(mode, filename))


if __name__ == '__main__':
    main()
