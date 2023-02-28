import Login
import Captcha
import random
import nltk
import unicodedata

nltk.download('punkt')
nltk.download('wordnet')

respostas = {
    "ola! Como posso ajudar?": ["Olá!", "Oi, como vai?", "Olá, em que posso ajudar?"],
    "qual e o seu nome?": ["Meu nome é ChatBot.", "Sou o ChatBot, e você?"],
    "qual e a sua idade?": ["Eu não tenho idade, sou um programa de computador!", "Não sou uma pessoa, então não tenho idade."],
    "qual e a sua comida favorita?": ["Como sou um programa de computador, não posso comer.", "Não tenho uma comida favorita, já que não sou uma pessoa."],
    "tchau!": ["Até mais!", "Tchau, volte sempre!"],
    "oi": ["Eae","Beleza?","Oi, Como você ta?"]
}

def responder(mensagem):
    mensagem_normalizada = unicodedata.normalize('NFKD', mensagem).encode('ASCII', 'ignore').decode('ASCII')
    mensagem_normalizada = mensagem_normalizada.lower()  # converte a mensagem normalizada para minúsculas
    # seleciona uma resposta aleatória da lista de respostas possíveis para a mensagem
    if mensagem_normalizada in respostas:
        return random.choice(respostas[mensagem_normalizada])
    else:
        return "Desculpe, eu não entendi o que você quer dizer."

print('-'*100,'\n\nBem-vindo ao Sistema Aleatório de Chat Ordinário (S.A.C.O.)\n\n','-'*100)
print('\nFaça Login para entrar no sistema. Caso não tenha acesso, realize um Cadastro\n')

Login.runLogin()
Captcha.runCaptcha()
print('\n\nS.A.C.O: Olá,',Login.userLoggedName,'!')

userInput = ""

while userInput != "sair":
    userInput = input(Login.userLoggedName+": ")
    resposta = responder(userInput)
    print("S.A.C.O.:", resposta)