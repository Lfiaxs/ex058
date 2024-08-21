from random import randint
computador = randint (0,10)
print('-=-' * 20)
print('Sou seu computador... ')
print ('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpites))
print('FIM')
