print(' Sequência de fibonacci')
x = int(input('quantos termos voce quer mostrar?'))
t1 = 0
t2 = 1
print('{} , {} '.format(t1, t2), end='')
cont = 3
while cont <= x:
    t3 = t1 + t2
    print(', {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' essa é a sequência de fibonacci na quantidade de termos que você pediu')
