def main():
    num1 = float(input("Digite o primeiro número: "))
    
    num2 = float(input("Digite o segundo número: "))
    
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = int(input("Digite o número da operação desejada (1/2/3/4): "))
    
    if escolha == 1:
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é {resultado}")
    elif escolha == 2:
        resultado = num1 - num2
        print(f"A subtração de {num1} e {num2} é {resultado}")
    elif escolha == 3:
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é {resultado}")
    elif escolha == 4:
       
        if num2 != 0:
            resultado = num1 / num2
            print(f"A divisão de {num1} por {num2} é {resultado}")
        else:
            print("Erro: Não é possível dividir por zero.")
    else:
        print("Escolha inválida. Por favor, insira um número entre 1 e 4.")

if __name__ == "__main__":
    main()
