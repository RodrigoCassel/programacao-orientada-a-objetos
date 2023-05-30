import math

class FiguraGeometrica:
    def calcularÁrea(self):
        pass

    def calcularPerimetro(self):
        pass


class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularÁrea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularÁrea(self):
        return 0.5 * self.base * self.altura

    def calcularPerimetro(self):
        # Triângulo genérico não possui uma fórmula geral para cálculo do perímetro.
        # Portanto, esse método retorna um valor fixo.
        return "Não é possível calcular o perímetro de um triângulo genérico."


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularÁrea(self):
        return math.pi * self.raio**2

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio


# Testando as classes e seus métodos

retangulo = Retangulo(4, 5)
print("Retângulo:")
print("Área:", retangulo.calcularÁrea())
print("Perímetro:", retangulo.calcularPerimetro())

triangulo = Triangulo(6, 8)
print("\nTriângulo:")
print("Área:", triangulo.calcularÁrea())
print("Perímetro:", triangulo.calcularPerimetro())

circulo = Circulo(3)
print("\nCírculo:")
print("Área:", circulo.calcularÁrea())
print("Perímetro:", circulo.calcularPerimetro())
