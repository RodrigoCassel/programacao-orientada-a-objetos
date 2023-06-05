# 1) Você foi contratado para desenvolver um programa de simulação de batalhas medievais. Para isso,
# você precisa implementar um sistema de unidades militares que possa se movimentar e atacar.
# Você deve criar três classes de unidades: Soldado, Arqueiro e Cavaleiro. Todas as classes devem
# herdar de uma classe base chamada UnidadeMilitar. A classe UnidadeMilitar deve ter os seguintes
# métodos:
# • mover(): exibe uma mensagem indicando que a unidade está se movendo.
# • atacar(): exibe uma mensagem indicando que a unidade está atacando.
# Cada uma das classes filhas deve implementar os métodos mover() e atacar() de forma específica,
# de acordo com a especialidade da unidade.
# Crie uma instância de cada uma das diferentes unidades (Soldado, Arqueiro e Cavaleiro), e adicione em
# uma lista chamada unidades. Por fim, você deve percorrer o array unidades usando um loop e chamar os
# métodos mover() e atacar() de cada unidade no array.

class UnidadeMilitar:
    def mover(self):
        print("A unidade está se movendo!")

    def atacar(self):
        print("A unidade está atacando!")


class Soldado(UnidadeMilitar):
    def mover(self):
        print("O soldado está marchando!")

    def atacar(self):
        print("O soldado está atacando!")


class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("O arqueiro está se movendo!")

    def atacar(self):
        print("O arqueiro está atirando!")


class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("O cavaleiro está se movendo!")

    def atacar(self):
        print("O cavaleiro está atacando!")


unidades = [Soldado(), Arqueiro(), Cavaleiro()]

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print()  
