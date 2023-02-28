import Login
import Captcha

print('-'*100,'\n\nBem-vindo ao Sistema Aleatório de Chat Ordinário (S.A.C.O.)\n\n','-'*100)
print('\nFaça Login para entrar no sistema. Caso não tenha acesso, realize um Cadastro\n')

Login.runLogin()
Captcha.runCaptcha()
print('\n\nS.A.C.O: Olá,',Login.userLoggedName,'!')

userInput = ""

while userInput != "sair":
    userInput = input(Login.userLoggedName+':').lower()
    if userInput != "sair":
        if "tudo bem?" in userInput or "td bem?" in userInput:
            print('S.A.C.O.: Tudo, e com você?')
        elif "oi" in userInput or "oie" in userInput or "eae" in userInput or "ola" in userInput or 'eai' in userInput:
            print('S.A.C.O.: Oláa, '+ Login.userLoggedName) 