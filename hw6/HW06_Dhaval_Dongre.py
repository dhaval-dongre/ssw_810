from string import ascii_uppercase, ascii_lowercase

def list_copy(l):
    """returns a copy of the provided list"""
    return [l[item] for item in range(0, len(l)) ]

def list_intersect(l1, l2):
    """returns the common elements between 2 lists in list format"""
    return [item for item in l1 if item in l2]

def list_difference(l1, l2):
    """returns the difference between 2 lists in list format"""
    return [item for item in l1 if item not in l2]

def remove_vowels(string):
    """removes the vowels from the given string and returns it"""
    return ''.join([item for item in list(string) if item not in ['a','e','i','o','u','A','E','I','O','U']])

def check_pwd(password):
    """verifies whether the password matches our criteria of uppercase, lowercase and digit"""
    return any(item in ascii_lowercase for item in password) and any(item in ascii_uppercase for item in password) and password[-1].isdigit()

def insertion_sort(l):
    """returns a sorted list using insertion sort"""
    nl=list()
    for x, y in enumerate(l):
        if len(nl) == 0:
            nl.append(y)
        else:
            for x2,y2 in enumerate(nl):
                if y2>y:
                    pos=x2
                    break
                else:
                    pos=x2+1
            nl.insert(pos,y)
    return nl

# if __name__ == '__main__':
#     print(list_copy([1,2,3]))
#     print(list_intersect([1,2,3,4],[1,2]))
#     print(list_difference([1,2,3,4],[1,2]))
#     print(remove_vowels('gaeioU'))
#     print(check_pwd('dhaval@4'))
#     print(insertion_sort([8,2,1,3,5,5,4]))