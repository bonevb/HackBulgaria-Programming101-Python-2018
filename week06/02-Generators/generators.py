
from os import listdir
from os.path import isfile, join
from string import ascii_lowercase, ascii_uppercase
import random

def chain(iterable_one, iterable_two):
    return list(iterable_one).extend(list(iterable_two))


def compress(iterable, mask):
    combinet = zip(iterable, mask)
    result = []
    for i in combinet:
        if True in i:
            result.append(i[0])
    return result


# print(list(compress(["Ivo", "Rado", "Panda"], [True, False, True])))


def cycle(iterable):
    while True:
        yield from iterable


endless = cycle(range(0,10))

#for i in endless:
#    print(i)

def get_next_row(path):
    for file_ in listdir(path):
        if isfile(join(path, file_)):
            file_path = '{}/{}'.format(path, file_)

            with open(file_path) as f:
                for line in f:
                    yield line


def format_chapter(lines_list):
    return ''.join(lines_list)


def get_chapters():
    initial = True
    result = []

    for row in get_next_row('Book'):
        if row.startswith('# Chapter'):
            if initial:
                initial = False
                result.append(row)
                continue

            yield format_chapter(result)
            result = []

        result.append(row)

    yield format_chapter(result)


def main():
    generator = get_chapters()

    while True:
        if ord(msvcrt.getch()) == 32:
            try:
                print(next(generator))
            except StopIteration:
                print('That\'s all folks.')
                break


punctuation = ['.', '?', '!']


def generate_random_words():
    word = ''.join([random.choice(ascii_lowercase) for i in range(random.randint(1, 20))])
    return word


def generage_row_chapter(chap_len):
    chapter = []
    for i in range(chap_len - 1):
        chapter.append(generate_random_words())
    chapter.append(generate_random_words() + random.choice(punctoation))
    chapter[0] = '# Chapter'
    yield chapter


def generate_book(chapter_count, chapter_length):
    with open('D:/Python/notesbook1.txt', 'w') as f:
        for i in range(chapter_count):
            generator = generage_row_chapter(chapter_length)
            result = next(generator)
            result[0] = result[0] + str(i + 1) + '\n'
            result[1] = result[1][:1].upper() + result[1][1:]
            f.write(' '.join(result) + '\n')

# print(generage_row_chapter(50))
# print(generate_book(20,10000000))


# print(book('/home/dux/Python101/week6/Book'))
