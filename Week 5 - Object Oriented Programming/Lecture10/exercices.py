def genPrimes():
    possiblePrime = 2

    while True:
        isPrimeNumber = True

        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrimeNumber = False
                break

        if (isPrimeNumber == True):
            yield possiblePrime

        possiblePrime += 1
