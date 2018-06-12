def is_credit_card_valid(number):
    str_number = str(number)
    if len(str_number) % 2 == 0:
        return False

    first_odd = str_number[-3]
    second_odd = str_number[-5]

    odd_positions = str_number[::-2]
    odd_positions = odd_positions[1::]
    isOK = False

    if odd_positions[0] == first_odd:
        isOK = True

    for i in range(1,len(odd_positions)):
        if i % 2 == 0:
            if odd_positions[i] == second_odd:
                return False
            else:
                isOK = True
        if int(i) % 2 != 0:
            if odd_positions[i] == first_odd:
                return False
            else:
                isOK = True

    result = []
    result.append(int(str_number[0]))
    for index, i in enumerate(str_number[1::]):
        if index % 2 == 0:
            result.append(int(i) *2)
        else:
            result.append(int(i))

    a = ''.join([str(i) for i in result])
    sum_of_digits = sum([int(i) for i in a])


    if sum_of_digits % 10 == 0:
        isOK = True
    else:
        return False

    return True


print(is_credit_card_valid(79927398715))




