nome = input("Qual é o seu nome? ")
print("Olá " + nome + "! Eu gosto de conversar com humanos.")
idade = int(input("Qual é a sua idade? "))
print ('Hmmmmmm.... ', idade, 'anos!')
if idade <= 12:
    print("Você ainda é uma criança!")
else:
    if idade >= 13 and idade <= 19:
        print("Você ainda é um adolescente!")
    else:
        if idade >= 20 and idade <=59:
            print("Você é um adulto de mochila!")
        if idade >= 59 and idade <=99:
            print("Você é um véio coroca!")
        if idade >= 100:
            print("Caraca, você está vivo ainda???!!!")
