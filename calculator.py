
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("Selecione a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite sua opção (1/2/3/4): ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == '1':
    print(num1, "+", num2, "=", soma(num1, num2))

elif opcao == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif opcao == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif opcao == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Opção inválida!")
