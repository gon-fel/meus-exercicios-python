"""Exercício - Coerção de Tipos
Enunciado:
Crie um programa que:
Pergunte ao usuário:
    Seu ano de nascimento (como string)
    Converta esse ano para inteiro.

Calcule e mostre a idade atual da pessoa (assuma que o ano atual é 2025)."""

#Declaração das Variáveis

ano_nascimento = input ('Qual seu ano de nascimento? ')
ano_nascimento = int(ano_nascimento)
idade_atual = 2025 - ano_nascimento
 
#Exibição das Informações

print(ano_nascimento)
print(f'Portanto você tem', idade_atual, 'anos')