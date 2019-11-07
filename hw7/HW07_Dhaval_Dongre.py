from collections import defaultdict, Counter
import re


def anagram_lst(str1, str2):
    """verifies whether both the string are anagrams of each other"""
    return sorted(list(cleanString(str1))) == sorted(list(cleanString(str2)))


def cleanString(str1):
    """a method which removes whitespaces and lowers the string"""
    str1 = re.sub(r"\s+", "", str1, flags=re.UNICODE)
    str1 = str1.lower()
    return str1


def anagrams_dd(str1, str2):
    """verifies whether both string are anagrams of each other using dictinories"""
    dd = defaultdict(int)

    str1 = re.sub(r"\s+", "", str1, flags=re.UNICODE)
    str2 = re.sub(r"\s+", "", str2, flags=re.UNICODE)

    str1 = cleanString(str1)
    str2 = cleanString(str2)

    for letter in str1:
        dd[letter] = dd[letter] + 1

    for c in str2:
        if c in dd:
            dd[c] = dd[c] - 1
        else:
            return False

    for key in dd:
        if dd[key] != 0:
            return False

    return True


def anagrams_cntr(str1, str2):
    """verifies whether both the strings are anagrams of each other using counter from the collections frmework"""
    str1 = cleanString(str1)
    str2 = cleanString(str2)

    return sorted(Counter(str1).elements()) == sorted(Counter(str2).elements())


def covers_alphabet(sentence):
    """verifies whether the given sentence has all the alphabets"""
    sentence = sentence.lower()
    sentence = "".join(re.findall("[a-zA-Z]+", sentence))

    return sorted(list(set(sentence))) == list('abcdefghijklmnopqrstuvwxyz')


def book_index(words):
    """returns a list which describes where each word is located on a list of pages"""
    d = defaultdict(set)
    for k, v in sorted(words, key=lambda x: x[0]):
        d[k].add(v)

    wordList = list()

    for k, v in d.items():
        singleList = list()
        singleList.append(k)
        singleList.append(sorted(list(v)))
        wordList.append(singleList)

    return wordList
