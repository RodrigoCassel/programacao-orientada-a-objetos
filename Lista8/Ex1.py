# 1. Crie quatro classes principais: Animal, Carnivoro, Herbivoro e Onivoro. A classe Animal será a classe
# base, enquanto as classes Carnivoro, Herbivoro e Onivoro serão classes intermediárias que
# herdarão da classe Animal e representarão diferentes tipos de dietas alimentares.
# Classe Animal
# Atributos: nome do animal
# Métodos:
# • exibirDescricao() - Exibe uma mensagem contendo o nome do animal
# Classe Carnivoro
# Métodos:
# • caçar(): exibe a ação de caça realizada pelo animal carnívoro
# • exibirDescricao() - Chama o método da classe base e acrescenta a mensagem informando que
# é um animal carnívoro
# Classe Herbivoro
# Métodos:
# • pastar(): exibe a ação de pastar realizada pelo animal herbívoro
# • exibirDescricao() - Chama o método da classe base e acrescenta a mensagem informando que
# é um animal herbívro
# Classe Onivoro
# Métodos:
# • comer(): sorteia um número inteiro entre 0 e 1, se der 0, chama o método caçar, se der 1,
# chama o método pastar
# • exibirDescricao() - Chama o método da classe Animal e acrescenta a mensagem informando
# que é um animal onívoro
# Dessa forma, cada classe intermediária (Carnivoro, Herbivoro e Onivoro) herda os atributos e
# métodos da classe Animal e acrescenta seus próprios métodos específicos. A classe Onivoro herda
# tanto o método caçar() quanto o método pastar().

import random

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"Sou um(a) {self.nome}!")

class Carnivoro(Animal):
    def caca(self):
        print("Estou caçando!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal carnívoro!")

class Herbivoro(Animal):
    def pastar(self):
        print("Como pasto igual vegano!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal herbívoro!")

class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        if random.randint(0, 1) == 0:
            self.caca()
        else:
            self.pastar()

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal onívoro!")

#Uso:

#Instâncias
leao = Carnivoro("Leão")
vaca = Herbivoro("Vaca")
urso = Onivoro("Urso")

#Puxando métodos
print()
leao.exibirDescricao()
leao.caca()
print()
vaca.exibirDescricao()
vaca.pastar()
print()
urso.exibirDescricao()
urso.comer()
print()
