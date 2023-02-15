import random
import string



print('Realize o Captcha abaixo para prosseguir')

n = random.randint(0, 26)
a = list(string.ascii_letters)
c = ""
r = 0
while r != 1:
    for i in range(2):
        for y in range(4):
            n = random.randint(0,len(a))
            c += a[n]
        c += ' '
    c = c[:-1]
    print(c)
    userInput = input('Digite o captcha EXATAMENTE como acima:\n')

    if userInput == c:
        r = 1
        print('Captcha CORRETO!')
    else:
        r = 0
        print('Captcha INCORRETO!')
        c = ''
print('BEM-VINDO ao Sistema!')
