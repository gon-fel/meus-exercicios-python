print(type("Python"))
print(type(10))
print(type(3.5))
print(type(True))

#Toda vez que eu utilizar a class= type, ele irá me informar o tipo que aquele dado pertences

"""
Exercício - Tipos de Dados
Enunciado:
Crie um pequeno programa em Python que:
Guarde em 4 variáveis os seguintes dados:
Seu nome completo (tipo string)
Sua idade (tipo inteiro)
Sua altura (tipo float)
Se você está estudando Python (tipo bool)
Depois, imprima na tela o valor de cada variável e o seu respectivo tipo usando a função type()."""

nome = 'Felipe Augusto Gonçalves'
idade = 32
altura = 1.72
python = True

print('Seu nome é:',nome, type(nome))
print('Você tem:',idade, 'anos', type(idade))
print('Sua altura é de:',altura, 'metros', type(altura))
print('Você estuda Python?',python, type(python))