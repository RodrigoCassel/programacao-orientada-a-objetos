# 2) Você está desenvolvendo um sistema para uma plataforma de streaming e precisa implementar a
# funcionalidade de assinaturas. Cada assinatura possui um tipo, um preço e detalhes específicos.
# Você deve criar uma classe base chamada Assinatura que possui os seguintes métodos:
# • calcular_preco(): retorna o preço da assinatura. Esse método precisa ser implementado nas
# subclasses.
# • exibir_detalhes(): exibe os detalhes da assinatura. Esse método também precisa ser
# implementado nas subclasses.
# Em seguida, você deve criar duas subclasses: AssinaturaSimples e AssinaturaPremium. Cada uma
# dessas subclasses deve herdar da classe Assinatura e implementar os métodos calcular_preco() e
# exibir_detalhes() de acordo com o tipo de assinatura.
# A classe AssinaturaSimples representa uma assinatura básica que fornece acesso a filmes e séries em
# qualidade padrão. O método calcular_preco() retorna o valor fixo de R$ 29.99 para essa assinatura, e o
# método exibir_detalhes() exibe a descrição da assinatura simples.
# A classe AssinaturaPremium representa uma assinatura avançada que oferece acesso a filmes e séries em
# qualidade HD e Ultra HD. O método calcular_preco() retorna o valor fixo de R$ 49.99 para essa assinatura,
# e o método exibir_detalhes() exibe a descrição da assinatura premium.
# Após criar as classes, você deve criar instâncias das assinaturas AssinaturaSimples e AssinaturaPremium
# com os tipos "Simples" e "Premium", respectivamente.
# Em seguida, crie um array chamado assinaturas e adicione as instâncias das assinaturas a esse array.
# Por fim, percorra o array assinaturas usando um loop e para cada assinatura, exiba o tipo de assinatura, o
# preço e os detalhes usando os métodos calcular_preco() e exibir_detalhes().

class Assinatura:
    def calcular_preco(self):
        pass
    
    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return "R$ 29.99"
    
    def exibir_detalhes(self):
        print("Assinatura Simples - Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return "R$ 49.99"
    
    def exibir_detalhes(self):
        print("Assinatura Premium - Acesso a filmes e séries em qualidade HD e Ultra HD.")

assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

assinaturas = [assinatura_simples, assinatura_premium]

for assinatura in assinaturas:
    print()
    print("Tipo de assinatura:", type(assinatura).__name__)
    print("Preço da assinatura:", assinatura.calcular_preco())
    assinatura.exibir_detalhes()
    print()