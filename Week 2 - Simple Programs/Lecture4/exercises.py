def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    result = 1
    divisor = max(a, b)

    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            result = divisor
            break

        divisor -= 1

    return result


#  print(gcdIter(17, 12))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

#  print(gcdRecur(17, 12))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    #  Base case
    if aStr == '':
        return False

    # Base case
    if len(aStr) == 1:
        return aStr == char

    # Base case
    middleIndex = len(aStr) // 2
    middleChar = aStr[middleIndex]

    if char == middleChar:
        return True

    # Recursive cases
    elif char < middleChar:
        return isIn(char, aStr[:middleIndex])
    else:
        return isIn(char, aStr[middleIndex + 1:])

#  print(isIn('a', 'a'))

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

import math

def polysum(n, s):
    '''
    n: positive integer number of sides of a regular polygon
    s: positive integer or float side length of a regular polygon

    return: sum of the area and square of the
            perimeter of the regular polygon
    '''
    if isinstance(n, int) and isinstance(s, (int, float)):
        area = (0.25 * n * s**2) / (math.tan(math.pi / n))
        perimeter = s * n

        result = area + perimeter ** 2

        return round(result, 4)
    else:
        return print('Please, enter a valid number for calculation')

print(polysum(2, 1))
