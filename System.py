import Login
import Captcha

print('-'*100,'\n\nBem-vindo ao Sistema Aleatório de Chat Ordinário (S.A.C.O.)\n\n','-'*100)
print('\nFaça Login para entrar no sistema. Caso não tenha acesso, realize um Cadastro\n')

Login.runLogin()

print('\n\nOlá,',Login.userLoggedName,'!')