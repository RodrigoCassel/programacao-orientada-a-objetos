#1) Escreva uma classe que represente um País. Um país é representado através dos atributos: código
#ISO 3166-1 (ex.: BRA), nome (ex.:Brasil), população (ex.: 193.946.886) e a sua dimensão em Km2
#(ex.: 8.515.767,049). Além disso, cada país mantém uma lista de outros países com os quais ele faz
#fronteira. Escreva a classe e forneça os seus membros a seguir:
#a. Construtor que inicialize o código ISO, o nome e a dimensão do país;
#b. Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e
#dimensão do país;
#c. Um método que permita verificar se dois objetos representam o mesmo país (isso se chama
#igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO;
#d. Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
#e. Um método que retorne a densidade populacional do país;
#f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos
#dois países.

class Pais:
    def __init__(self, codigo=None, nome=None, dimensao=None, populacao=0):
        self.__codigo = codigo
        self.__nome = nome
        self.__dimensao = dimensao
        self.__populacao = populacao
        self.__vizinhos = []

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setPopulacao(self, populacao):
        self.__populacao = populacao

    def getPopulacao(self):
        return self.__populacao

    def setDimensao(self, dimensao):
        self.__dimensao = dimensao

    def getDimensao(self):
        return self.__dimensao

    def compararIgual(self, pais):
        # retorna true/false
        if self.__codigo == pais.getCodigo():
            return True
        else:
            return False

    def verificarVizinho(self, pais):
        for i in self.__vizinhos:
            if i.compararIgual(pais) == True:
                return True
        return False

    def calcularDensidade(self):
        return self.__populacao / self.__dimensao

    def vizinhosComuns(self, pais):
        vizinhos_pais = pais.getVizinhos() #pega a listagem de vizinhos do outro pais
        vizinhos_ambos = [] #inicia a lista dos vizinhos comuns a ambos
        for i in vizinhos_pais:  
            if self.verificarVizinho(i) == True: #verifica se o vizinho do outro país é vizinho do país
                vizinhos_ambos.append(i) #adiciona na lista de ambos se verdadeiro! :)
        return vizinhos_ambos #retorna a lista, como o exercício pede!

    def adicionarVizinho(self, pais):
        self.__vizinhos.append(pais)

    def getVizinhos(self):
        return self.__vizinhos

    def listarVizinhos(self):
        for i in self.__vizinhos:
            print(i.getCodigo())

# Exemplo de uso da classe:
pais01 = Pais('BRA', 'Brasil', 8515767.049, 193946886)
pais02 = Pais('ARG', 'Argentina', 2780400, 45031000)
pais03 = Pais('URU', 'Uruguai', 176215, 3473730)
pais04 = Pais('PAR', 'Paraguai', 406752, 7152703)
pais05 = Pais('CHI', 'Chile', 756096, 19269370)
pais06 = Pais('PER', 'Peru', 1285216, 32971846)

# Adicionando vizinhos a cada país:
pais01.adicionarVizinho(pais02)
pais01.adicionarVizinho(pais03)
pais01.adicionarVizinho(pais04)
pais01.adicionarVizinho(pais06)

pais02.adicionarVizinho(pais01)
pais02.adicionarVizinho(pais03)
pais02.adicionarVizinho(pais04)
pais02.adicionarVizinho(pais05)