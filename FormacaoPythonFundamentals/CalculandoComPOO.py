# Treinando Orientação a Objetos com Python
# 1 / 3 - Calculando com POO

# TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    def soma(self, a, b):
        return a + b


num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)
