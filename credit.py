from cs50 import get_string

while True:
    # prompt user for correct imput
    x = get_string("Number: ")
    # apply luhn's algrithm
    if x.isdigit() == True:
        i = len(x) - 2
        j = len(x) - 1
        sum1 = []
        sum2 = 0
        while i >= 0:
            sum1.append(int(x[i]) * 2)
            if j >= 0:
                sum2 = sum2 + int(x[j])
            i -= 2
            j -= 2
        n = 0
        sum = 0
        while n < len(sum1):
            if len(str(sum1[n])) > 1:
                sum = sum + int(str(sum1[n])[0]) + int(str(sum1[n])[1])
            else:
                sum = sum + sum1[n]
            n += 1
        sum = sum + sum2
        # determine whether it's a valid card number
        if sum % 10 == 0:
            if len(x) == 15:
                print('AMEX')
            elif x[0] == '4' and (len(x) == 13 or len(x) == 16):
                print('VISA')
            else:
                print('MASTERCARD')
        else:
            print('INVALID')
        break



