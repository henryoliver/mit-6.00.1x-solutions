x = 100
low = 0
high = x
epsilon = 0.01
ans = int((high + low) / 2.0)

print('Please think of a number between ' + str(low) + ' and ' + str(high))

while abs(ans ** 2 - x) >= epsilon:
    print('\n\nIs your secret number ' + str(ans) + '?\n\n')

    clue = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly: ')

    if clue == 'h':
        high = ans
    elif clue == 'l':
        low = ans
    elif clue == 'c':
        print('\n\nGame over. Your secret number was: ' + str(ans))
        break
    else:
        print('\n\nSorry, I did not understand your input.')

    ans = int((high + low) / 2.0)
