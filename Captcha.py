import random
import string


def runCaptcha():
    print('Realize o Captcha abaixo para prosseguir\n')

    n = random.randint(0, 26)
    a = list(string.ascii_letters)
    c = ""
    r = 0
    while r != 1:
        for i in range(2):
            for y in range(4):
                n = random.randint(0,len(a))
                c += a[n-1]
                
            c += ' '
        c = c[:-1]
        print(c)
        userInput = input('\nDigite o captcha EXATAMENTE como acima:\n')

        if userInput == c:
            r = 1
            print('\nCaptcha CORRETO!\n')
        else:
            r = 0
            print('\nCaptcha INCORRETO!\n')
            c = ''
