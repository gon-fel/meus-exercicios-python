"""[Introdução aos Tipos de Dados - Exercício 2/5]
Desafio:
Enunciado:
Crie um pequeno formulário que:
    Pergunte o nome do usuário
    Pergunte a idade
    Pergunte se ele sabe programar (resposta deve ser True ou False)

Depois:
    Armazene essas respostas em variáveis com tipos corretos
    Mostre as informações em um único print(), usando f-string"""

# Declarando as variáveis: 
nome = str(input('Qual o seu nome? '))
idade = int(input('Agora sua idade: '))
saber_programar = bool(input('Você gosta de Programar? (A resposta deve ser: "True" ou "False") '))

#Impressão das Variáveis e dos Dados:
print (f'Seu nome é: {nome}. Sua idade é: {idade} e você sabe de programar?: {saber_programar}')

#Declarando as Classes:
print('A Classe de nome é:',type(nome),'A classe de idade é:',type(idade), 'A classe de saber programação é: ',type(saber_programar))