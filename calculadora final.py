# adição
def adicionar(x, y):
    return x + y

# sub
def subtrair(x, y):
    return x - y

# mult
def multiplicar(x, y):
    return x * y

# divisao
def dividir(x, y):
    if y == 0:
        raise ValueError("se eu tenho 0 balas para dividir com 0 amigos, eu não divido nada com ninguém! minha vida é tão solitária...")
    return x / y
# Loop
while True:
    # opções
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # usuario escolhe operação
    escolha = input("Escolha a operação: ")

    # quebra do programa
    if escolha == '5':
        print("só burro usa calculadora")
        break
    elif escolha in ('1', '2', '3', '4'):
        try:
            # input humano
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # calcula
            if escolha == '1':
                print("(resultado) O neymar disse que a conta deu ", adicionar(num1, num2))
            elif escolha == '2':
                print("(resultado) você me deve ", subtrair(num1, num2))
            elif escolha == '3':
                print("(resultado) O lucro ontem foi de", multiplicar(num1, num2))
            elif escolha == '4':
                print("as células multiplicam se dividindo, que loucura , e temos o total de ", dividir(num1, num2))
        except ValueError:
            print("tá maluco jamelão, quer colocar letra na matemática?")
    else:
        print("você abriu uma calculadora e não sabe nem contar quantas opções tem? tá dificil... tenta de novo")
