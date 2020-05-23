#  Problem 1 - Paying Debt off in a Year

def calculateBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Input: 
        balance: integer or float - the outstanding balance on the credit card
        annualInterestRate: float - annual interest rate as a decimal
        monthlyPaymentRate: float - minimum monthly payment rate as a decimal

    returns: calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
    '''
    i = 0
    totalMonths = 12
    monthlyInterestRate = annualInterestRate / totalMonths

    while i < totalMonths:
        i += 1

        minMonthlyPayment = monthlyPaymentRate * balance
        balance = (balance - minMonthlyPayment) * (1 + monthlyInterestRate)

        print('Month ' + str(i) + ' Remaining balance: ' + str(round(balance, 2)))

    print('Remaining balance: ' + str(round(balance, 2)))

#  calculateBalance(42, 0.2, 0.04)


#  Problem 2 - Paying Debt Off in a Year
balance = 3926
annualInterestRate = 0.2

totalMonths = 12
initialBalance = balance

monthlyPaymentRate = 0
monthlyInterestRate = annualInterestRate / totalMonths

while balance > 0:
    for i in range(totalMonths):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = initialBalance
    elif balance <= 0:
        break

#  print('Lowest Payment: ', str(monthlyPaymentRate))


#  Problem 3 - Using Bisection Search to Make the Program Faster

def calcfixedamort(balance, annualinterestrate):
    '''
    balance: integer or float that represents the outstanding balance on the credit card
    annualinterestrate: float number that represents the annual interest rate as a decimal

    returns: float - find the smallest fixed monthly payment
    '''
    totalmonths = 12
    initialbalance = balance

    monthlypayment = 0
    monthlyinterestrate = annualinterestrate / totalmonths

    epsilon = 0.01

    lowerbound = initialbalance / totalmonths
    upperbound = (initialbalance * (1 + monthlyinterestrate) ** totalmonths) / totalmonths

    while abs(balance) >= epsilon:
        balance = initialbalance
        monthlypayment = (upperbound + lowerbound) / 2

        for i in range(totalmonths):
            balance = balance - monthlypayment + ((balance - monthlypayment) * monthlyinterestrate)

        if balance < epsilon:
            upperbound = monthlypayment
        elif balance > epsilon:
            lowerbound = monthlypayment
        else:
            break

    print('lowest payment: ' + str(round(monthlypayment, 2)))

def recursiveCalcfixedamort(balance, annualinterestrate):
    '''
    balance: integer or float that represents the outstanding balance on the credit card
    annualinterestrate: float number that represents the annual interest rate as a decimal

    returns: float - find the smallest fixed monthly payment
    '''
    totalmonths = 12
    initialbalance = balance

    monthlypayment = 0
    monthlyinterestrate = annualinterestrate / totalmonths

    epsilon = 0.01

    lowerbound = initialbalance / totalmonths
    upperbound = (initialbalance * (1 + monthlyinterestrate) ** totalmonths) / totalmonths

    #  Base case
    if abs(balance) >= epsilon:
        return monthlypayment
    else:
        balance = initialbalance
        monthlypayment = (upperbound + lowerbound) / 2

        for i in range(totalmonths):
            balance = balance - monthlypayment + ((balance - monthlypayment) * monthlyinterestrate)

        if balance < epsilon:
            upperbound = monthlypayment
        elif balance > epsilon:
            lowerbound = monthlypayment



    while abs(balance) >= epsilon:

        if balance < epsilon:
            upperbound = monthlypayment
        elif balance > epsilon:
            lowerbound = monthlypayment
        else:
            break

    print('lowest payment: ' + str(round(monthlypayment, 2)))

calcFixedAmort(320000, 0.2)
calcFixedAmort(999999, 0.18)
