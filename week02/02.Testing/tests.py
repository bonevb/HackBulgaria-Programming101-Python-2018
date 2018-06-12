from fractions import Fraction
from operator import itemgetter 


def simplify_fraction(fraction):
    return Fraction(fraction)


# print(simplify_fraction((3,9))


def collect_fractions(fractions):
    result = 0
    for i in fractions:
        a, b = i
        result += Fraction(a, b)
    return result


def sort_fractions(fractions):
    def sort():
        a, b = x
        return Fraction(a, b)
    return sorted(fractions, key = lambda x: x[1]/x[0], reverse=True)


#print(sort_fractions([(2, 3), (1, 2)]))
#print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
#print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))



#print(collect_fractions([(1, 4), (1, 2)]))
#print(collect_fractions([(1, 7), (2, 6)]))
