#  Exercise: simple divide
def fancy_divide(list_of_numbers, index):
    '''
    list_of_numbers: list of numbers
    index: integer positive number
    returns: the division on each item of the list
    '''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

def simple_divide(item, denom):
    '''
    item: integer number
    denom: integer positive number

    returns: the division between item and denom
    '''
    try:
        return abs(item) / abs(denom)
    except ZeroDivisionError:
        return denom
    

#  Test case:
print(fancy_divide([0, 2, 4], 1))
