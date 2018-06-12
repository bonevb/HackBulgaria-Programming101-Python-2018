def is_number_balanced(number):
    number = list(str(number))
    if len(number) == 1:
        return True

    if (len(number) // 2) % 2 == 0:
        mid = len(number) // 2
        return sum([int(i) for i in number[:mid]]) == sum([int(i) for i in number[mid:]])

    elif (len(number) // 2) % 2 != 0:
        mid = len(number) // 2
        return sum([int(i) for i in number[:mid]]) == sum([int(i) for i in number[(mid + 1):]])


# print(is_number_balanced(121))


def increasing_or_decreasing(n):
    isUp = False
    isDown = False
    for i in range(1, len(n)):
        if n[i - 1] < n[i]:
            isUp = True
        else:
            isUp = False
            break

    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            isDown = True
        else:
            isDown = False
            break

    if isUp:
        return 'UP!'
    elif isDown:
        return 'DOWN!'
    else:
        return False


# print(increasing_or_decreasing([9,8,7,6]))


def palindrome(n):
    a = str(n)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


def get_largest_palindrome(n):
    a = [i for i in range(n)]
    b = a[::-1]
    for i in b:
        if palindrome(i):
            return i

# print(get_largest_palindrome(994687))


def sum_of_numbers(n):
    if n.isdigit():
        return int(n)

    a = list(n)
    temp = []
    result = []
    isDig = True
    for i in n:
        if i.isdigit():
            temp.append(i)
        else:
            result.append(''.join(temp))
            temp = []
    if len(temp) > 0:
        result.extend(temp)

    print('Result', result)

    return sum([int(i) for i in result if i.isdigit()])


# print(sum_of_numbers("ab125cd3"))


def birthday_ranges(birthdays, ranges):
    result = []
    counter = 0
    for i in ranges:
        a = [i for i in range(i[0], i[1] + 1)]
        b = set(a)
        c = set(birthdays).intersection(b)
        result.append(len(c))

    return result


#print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))


from itertools import groupby


def numbers_to_message(pressed_sequence):

    groups = []
    keys = []

    for key, group in groupby(pressed_sequence):
        groups.append(list(group))
        keys.append(key)

    print(groups)

    my_dict = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']

    }
    message = ''

    isUpper = False

#    [[2], [-1], [2, 2], [-1], [2, 2, 2]]

    for i in groups:
        if i[0] == -1:
            continue
        elif i[0] == 0:
            message += ' '
        elif i[0] == 1:
            isUpper = True
        else:
            len_i = len(i)
            if len_i > len(my_dict[i[0]]):
                position = len_i % len(my_dict[i[0]]) - 1
                d = my_dict[i[0]][position]
                if isUpper:
                    message += d.upper()
                    isUpper = False
                else:
                    message += d
            else:
                if isUpper:
                    message += (my_dict[i[0]][len_i - 1]).upper()
                    isUpper = False
                else:
                    message += my_dict[i[0]][len_i - 1]

    return message


#print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    result = []

    for i in message:
        if i == ' ':
            result.append([0])
        else:
            if i == i.upper():
                result.append([1])
                i = i.lower()
                result.append(find_letter(i))
            else:
                result.append(find_letter(i))
    print(result)

    final = []
    if len(result[0]) == 1:
        final.append(result[0][0])
    else:
        for j in result[0]:
            final.append(j)

    for i in range(1, len(result)):
        if len(result[i]) > 1 and result[i - 1][0] == result[i][0] or result[i - 1][0] == result[i][0]:
            final.append(-1)
            for j in result[i]:
                final.append(j)

    return final
