#Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
#úmeros. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
#resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
#execução do método e retornar -1.

class Calculadora:
    
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 == 0:
            print('-1')
            print("AVISO: Divisão por zero!")
            return -1
    
        else:
            return num1 / num2


calc = Calculadora()

opcao = input("Digite a operação desejada (1-soma, 2-subtração, 3-multiplicação ou 4-divisão): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    resultado = calc.somar(num1, num2)
    print("O resultado da soma é {}".format(resultado))
elif opcao == "2":
    resultado = calc.subtrair(num1, num2)
    print(f"O resultado da subtração é {resultado}")
elif opcao == "3":
    resultado = calc.multiplicar(num1, num2)
    print(f"O resultado da multiplicação é {resultado}")
elif opcao == "4":
    resultado = calc.dividir(num1, num2)
    if resultado == -1:
        print("Não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão é {resultado}")
else:
    print("Operação inválida!")
