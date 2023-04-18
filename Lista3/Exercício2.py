#2) Escreva uma classe Continente. Um continente possui um nome e é composto por um conjunto
#de países. Forneça os membros de classe a seguir:
#a. Construtor que inicialize o nome do continente;
#b. Um método que permita adicionar países aos continentes;
#c. Um método que retorne a dimensão total do continente;
#d. Um método que retorne a população total do continente;
#e. Um método que retorne a densidade populacional do continente;
#f. Um método que retorne o país com maior população no continente;
#g. Um método que retorne o país com menor população no continente;
#h. Um método que retorne o país de maior dimensão territorial no continente;
#i. Um método que retorne o país de menor dimensão territorial no continente;
#j. Um método que retorne a razão territorial do maior país em relação ao menor país.

class Pais:
    def __init__(self, nome, populacao, dimensao):
        self.nome = nome
        self.populacao = populacao
        self.dimensao = dimensao

    def __str__(self):
        return f"{self.nome} - População: {self.populacao} - Dimensão: {self.dimensao}"

class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []

    def adicionarPais(self, pais):
        self.paises.append(pais)

    def dimensaoTotal(self):
        total = 0
        for pais in self.paises:
            total += pais.dimensao
        return total

    def populacaoTotal(self):
        total = 0
        for pais in self.paises:
            total += pais.populacao
        return total

    def densidadePopulacional(self):
        return self.populacaoTotal() / self.dimensaoTotal()

    def maiorPopulacao(self):
        return max(self.paises, key=lambda pais: pais.populacao)

    def menorPopulacao(self):
        return min(self.paises, key=lambda pais: pais.populacao)

    def maiorDimensao(self):
        return max(self.paises, key=lambda pais: pais.dimensao)

    def menorDimensao(self):
        return min(self.paises, key=lambda pais: pais.dimensao)

    def razaoTerritorial(self):
        return self.maiorDimensao().dimensao / self.menorDimensao().dimensao

# pedir para inserir informações de países
continente = Continente(input("Insira o nome do continente: "))
while True:
    nome = input("Insira o nome do país (ou deixe em branco para encerrar): ")
    if not nome:
        break
    populacao = int(input("Insira a população do país: "))
    dimensao = float(input("Insira a dimensão do país (em km²): "))
    pais = Pais(nome, populacao, dimensao)
    continente.adicionarPais(pais)

# imprimir resultados
print(f"\nInformações do continente {continente.nome}:")
print(f"Total de países: {len(continente.paises)}")
print(f"Dimensão total: {continente.dimensaoTotal()} km²")
print(f"População total: {continente.populacaoTotal()} habitantes")
print(f"Densidade populacional: {continente.densidadePopulacional()} hab/km²")
print(f"País com maior população: {continente.maiorPopulacao()}")
print(f"País com menor população: {continente.menorPopulacao()}")
print(f"País com maior dimensão: {continente.maiorDimensao()}")
print(f"País com menor dimensão: {continente.menorDimensao()}")
print(f"Razão territorial entre o maior e o menor país: {continente.razaoTerritorial()}")
