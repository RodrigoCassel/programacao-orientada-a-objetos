class Mago:
    def __init__(self, nome, idade, escola, poder, tier):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.poder = poder
        self.tier = tier
        
    def andar(self):
        print('Estou andando!')
    
    def falar(self):
        print("Ola amigue! Meu nome é {}.".format(self.nome))
        
    def invocarMagia(self):
        print("Invocando magia!")
    
    def informarPoder(self):
        print("Possuo poder de {}.".format(self.poder))
    
    def informarTier(self):
        print("Sou tier {} no ranking de magos!".format(self.tier))

        
        
hp = Mago('Harry Potter', 17, 'Hogwarts', "Varinha", "B")
mg = Mago("Mestre dos Magos", 89, "Caverna", "Sabedoria", "A")
vd = Mago("Vingador", 370, "Caverna", "Fogo", "C+")
rd = Mago("Rodrigo", 22, "Da Vida", "Voar", "S++")


hp.falar()
hp.andar()
hp.invocarMagia()
hp.informarPoder()
hp.informarTier()

print(" ")

mg.falar()
mg.andar()
mg.invocarMagia()
mg.informarPoder()
mg.informarTier()

print(" ")

vd.falar()
vd.andar()
vd.invocarMagia()
vd.informarPoder()
vd.informarTier()

print(" ")

rd.falar()
rd.andar()
rd.invocarMagia()
rd.informarPoder()
rd.informarTier()

##
print(" ")
print(" ")
print(" ")
print(" ")

class Data:
    def __init__(self, dia, mes, ano):
        # Atributos de instância
        self.dia = dia
        self.mes = mes 
        self.ano = ano

    def imprimirData(self):
        print("Hoje é dia {}/{}/{}!".format(self.dia,self.mes,self.ano))
    def imprimirDataPorExtenso(self):
        cidade = input("Informe a cidade para exibir a data por extenso: ")
        print("Hoje é dia {} de {} de {} na cidade de {}!".format(self.dia,self.mes,self.ano,cidade))
  
dt = Data(input("Iformar dia: "), input("Iformar mês: "), input("Iformar ano: "))

dt.imprimirData()
dt.imprimirDataPorExtenso() 

####

class Musica:
    def __init__(self, nomeMusica, artistaMusica, generoMusica, anoMusica, duracaoMusica):
        self.nomeMusica = nomeMusica
        self.artistaMusica = artistaMusica
        self.generoMusica = generoMusica
        self.anoMusica = anoMusica
        self.duracaoMusica = duracaoMusica
    
    def visualizaDados(self):
        print(self.nomeMusica, self.artistaMusica, self.generoMusica, self.anoMusica, self.duracaoMusica)
    
    def visualizaNome(self):
        print(self.nomeMusica)

    def visualizaArtista(self):
        print(self.artistaMusica)

    def visualizaGenero(self):
        print(gerenoMusica)

    def visualizaAno(self):
        print(self.anoMusica)

    def visualizaDuracao(self):
        print(self.duracaoMusica)

m1 = Musica('Fa fe fi fo Funk', 'Anira', 'Funk', 2019, '3:05')
m2 = Musica('Sofrência de programar', 'Ada & Turing','Sertanejo', 1998, '2:58')
m3 = Musica('Rock n Rolo', 'The Buns','Rock',	1984, '4:01')
m4 = Musica('Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25')
m5 = Musica('Outra musica', 'Anira', 'Funk', 2019, '3:05')

print(" ")
print("Segue abaixo a base de dados: ")
print ("Música 1:"), m1.visualizaDados()
print(" ")
print ("Música 2:"), m2.visualizaDados()
print(" ")
print ("Música 3:"), m3.visualizaDados()
print(" ")
print ("Música 4:"), m4.visualizaDados()
print(" ")
print ("Música 5:"), m5.visualizaDados()

print(" ")

print("Segue abaixo o ano das músicas: ")
m1.visualizaAno()
m2.visualizaAno()
m3.visualizaAno()
m4.visualizaAno()
m5.visualizaAno()

print(" ")

print("Segue abaixo o nome das músicas: ")
m1.visualizaNome()
m2.visualizaNome()
m3.visualizaNome()
m4.visualizaNome()
m5.visualizaNome()

print(" ")

print("Segue abaixo o artista das músicas: ")
m1.visualizaArtista()
m2.visualizaArtista()
m3.visualizaArtista()
m4.visualizaArtista()
m5.visualizaArtista()

## acredito que esta seja a solução mais rudimentar possível, pois não consegui fazer um menu com opções e nem a função de adicionar músicas na playlist
## de qualquer forma, continuarei tentando