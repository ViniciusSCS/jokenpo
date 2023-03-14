# importando módulo random
from random import randint
# importando módulo para gerenciar o nome JOKENPÔ
from time import sleep

# definindo itens
itens = ('Pedra', 'Papel', 'Tesoura')

# jogada do computador
computador = randint(0, 2)

# apresentar as opções:
print('''
      Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      ''')

# jogada do jogador
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 11)

# apresentado o que cada um jogou...
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)

# montar estrutura de condicionais para apresentar os resultados
if computador == 0:
    if jogador == 0:
        print('EMPATOU')

    elif jogador == 1:
        print('JOGADOR VENCEU!!')

    elif jogador == 2:
        print('COMPUTADOR VENCEU!!')

    else:
        print('JOGADA INVÁLIDA!!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')

    elif jogador == 1:
        print('EMPATE!!')

    elif jogador == 2:
        print('JOGADOR VENCEU!!')

    else:
        print('JOGADA INVÁLIDA!!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!')

    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')

    elif jogador == 2:
        print('EMPATE!!')

    else:
        print('JOGADA INVÁLIDA!!')
