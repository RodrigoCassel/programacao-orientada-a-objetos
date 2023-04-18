#1)Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
#possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
#de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
#um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
#jogada deve ser impresso na tela. Não deve ser usado print dentro da classe.

import random

class Dice:
    def __init__(self, face):
        self.face = face

    def roll(self):
        return random.randint(1,self.face)

d6 = Dice(6)
d8 = Dice(8)
d12 = Dice(12)

print("Rolling dice 6")
for i in range (3):
    print(d6.roll())

print("Rolling dice 8")
for i in range (3):
    print(d8.roll())

print("Rolling dice 12")
for i in range (3):
    print(d12.roll())


    
        
