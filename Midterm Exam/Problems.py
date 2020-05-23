#  Problem 3
def count7(N):
    '''
    N: a non-negative integer
    return: the number of occurrences of the digit 7 in N
    '''
    #  Base case
    if (N < 10):
        if (N % 10 == 7):
            return 1
        else:
            return 0

    #  Default case
    if (N % 10 == 7):
        return 1 + count7(N // 10)
    else:
        return count7(N // 10)

#  Test cases:
#  print('---------------------------')
#  print(count7(779230))


#  Problem 4
def lessThan4(aList):
    '''
    aList: a list of strings
    return: the sublist of strings in aList that contain fewer than 4 characters.
    '''
    sublist = []

    for n in aList:
        if (len(n) < 4):
            sublist.append(n)

    return sublist


#  Test cases:
#  print('---------------------------')
#  print(lessThan4(['1234', '12345', '12', '1', '123']))


#  Problem 5
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    return: a list of keys in aDict that map to integer values that are unique
    '''
    uniqueKeys = []

    for key, value in aDict.items():
        if (list(aDict.values()).count(value) == 1):
            uniqueKeys.append(key)

    return sorted(uniqueKeys)


#  Test cases:
#  print('---------------------------')
#  print(uniqueValues({'5': 1, '24': 2, '343': 3, '4': 1, '0': 1}))
#  print(uniqueValues({'1': 1, '5': 2, '2': 2, '3': 3}))


#  Problem 6
def flatten(aList):
    ''' 
    aList: a list 
    return: a copy of aList, which is a flattened version of aList 
    '''
    #  Base case:
    if (len(aList) == 0):
        return []
    # Default case:
    else:
        for n in aList:
            aList.remove(n)

            if (isinstance(n, list)):
                return flatten(n) + flatten(aList)
            else:
                return [n] + flatten(aList)


#  Test cases:
#  print('---------------------------')
#  print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
#  print(flatten([1, 2, 3, [4, 5, 6], 7, 8, [9, 10], '11', '12', [[13, 14, [15, 16]]]]))



# Problem 7
def applyF_filterG(L, f, g):
    '''
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    '''
    for i in L[:]:
        if not g(f(i)):
            L.remove(i)

    if not len(L):
        return -1
    else:
        return max(L)

def f(i):
    return i + 2

def g(i):
    return i > 10

L = [0, 1, 22, 3, -4, 55, -6, 7, 8, 9]

#  Test cases:
print('---------------------------')
print(applyF_filterG(L, f, g))
print(L)


