def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other/odd element of aTup
    '''
    oddTup = ()

    for n in enumerate(aTup):
        if n[0] % 2 == 0:
            oddTup = oddTup + (n[1],)

    return oddTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
