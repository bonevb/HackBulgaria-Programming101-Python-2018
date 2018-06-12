def anagrams(text):
    first, second = text.split(' ')
    isAnagram = False
    if len(first) == len(second):
        for i in first:
            if i in second:
                isAnagram = True
            else:
                return 'NOT ANAGRAMS'
        for i in second:
            if i in first:
                isAnagram = True
            else:
                return 'NOT ANAGRAMS'
    else:
        return 'NOT ANAGRAMS'
    return 'ANAGRAM'

print(anagrams('BRADE BEARD'))
