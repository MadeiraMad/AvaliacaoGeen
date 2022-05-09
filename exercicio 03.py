for x in  range(100):
    if x % 3 == 0 and x % 5 == 0:
        print('Fizz_Buzz')
        continue
    elif x % 3 == 0:
        print('Fizz')
        continue
    elif x % 5 == 0:
        print('Buzz')
        continue
    else:print(x)



