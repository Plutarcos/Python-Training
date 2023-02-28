usernames = ["admin"]
passwords = ["admin"]
userLoggedName = 'user'
haslogged = 0

def save_to_txt(usernamedata, passworddata):
    with open('data\logindata.txt', 'w') as file:
        file.write(','.join(usernamedata) + '\n')
        file.write(','.join(passworddata))

def read_from_txt():
    with open('data\logindata.txt', 'r') as file:
        lines = file.readlines()
    usernamedata = lines[0].rstrip('\n')
    passworddata = lines[1]
    list1 = usernamedata.split(',')
    list2 = passworddata.split(',')
    return list1, list2

def runLogin():
    while haslogged !=1:
        print("1-Fazer Login")
        print("2-Cadastrar")
        choice = int(input(''))


        def login():
            usernames, passwords = read_from_txt()
            loggedin = 0
            while loggedin != 2:
                loggedin = 0
                username = input('Digite o nome de usuário:\n')
                password = input('Digite a senha:\n')
                if usernames.count(username):
                    loggedin = 1
                    if passwords.count(password) and passwords.index(password) == usernames.index(username):
                        loggedin = 2
                        
                if loggedin ==1:
                    print('\nSenha INCORRETA!\nPor favor, tente novamente\n')
                if loggedin ==0:
                    print('\nUsuário NÃO EXISTE\nPor favor, tente novamente\n')
            print('\n\nLOGIN REALIZADO COM SUCESSO!\n')
            global haslogged 
            global userLoggedName
            userLoggedName = username
            haslogged += 1
            


        def signup():
            inputUser = input('Por favor, digite o nome de usuário:\n')
            inputPass = input('Digite a senha:\n')

            print('\n\nCadastro realizado com sucesso\n\n')
            usernames.append(inputUser)
            passwords.append(inputPass)

            save_to_txt(usernames,passwords)

        if choice == 1:
            login()
            choice = 0
        elif choice == 2:
            signup()
            choice = 0
        else:
            choice = 0


