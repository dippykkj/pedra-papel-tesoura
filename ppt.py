import random
print('1 = pedra, 2 = tesoura, 3 = papel')
voce = int(input('faça sua escolha '))
opcoes = [1, 2, 3]
eu = random.choice(opcoes)
if voce == 1 and eu == 2:
    print('Você jogou pedra e eu joguei papel, eu venci.')
elif voce == 1 and eu == 3:
    print('Você jogou pedra e eu joguei tesoura, você venceu.')
elif voce == 2 and eu == 1:
    print('Você jogou papel e eu joguei pedra, você venceu.')
elif voce == 2 and eu == 3:
    print('Você jogou papel e eu joguei tesoura, eu venci.')
elif voce == 3 and eu == 1:
    print('Você jogou tesoura e eu joguei pedra, eu venci.')
elif voce == 3 and eu == 2:
    print ('Você jogou tesoura e eu joguei papel, você venceu.')
elif voce == eu:
    print('Os dois jogaram iguais, deu empate.')
else:
    print('Ops! Algo deu errado... Verifique a ortografia e veja se está escrito correto! Lembre-se: As opções são 1 (pedra), 2 (tesoura) e 3 (papel).')
    
#Peço perdão em casos de erros, ainda estou começando na linguagem!
