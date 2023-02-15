usernames = ["admin"]
passwords = ["admin"]

print("1-Fazer Login")
print("2-Cadastrar")
choice = int(input(''))

def login():
    loggedin = 0
    while loggedin != 2:
        loggedin = 0
        username = input('Digite o nome de usuário:\n')
        password = input('Digite a senha:\n')
        if usernames.count(username):
            loggedin = 1
            if passwords.count(password):
                loggedin = 2
        if loggedin ==1:
            print('\nSenha INCORRETA!\nPor favor, tente novamente\n')
        if loggedin ==0:
            print('\nUsuário NÃO EXISTE\nPor favor, tente novamente\n')
    print('\n\nLOGIN REALIZADO COM SUCESSO!\n')


def signup():
    inputUser = input('Por favor, digite o nome de usuário:\n')
    inputPass = input('Digite a senha:\n')

    print('\n\nProssiga para o Login\n')
    usernames.append(inputUser)
    passwords.append(inputPass)

    login()

if choice == 1:
    login()
else:
    signup()


