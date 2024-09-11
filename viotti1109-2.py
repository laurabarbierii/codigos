import math

casa = float(input("Digite o valor da casa desejada: "))
    
salario = float(input("Digite o seu salario: "))

prestacao = float(input("Digite quantos anos pagando: "))
    

if prestacao >= casa:
        resultado = 0
        print(f"você não pode comprar essa casa")
elif prestacao <= casa:
        resultado = prestacao/casa
        print(f"a sua prestação vai ser tendo o resultado de {prestacao} e {casa} é {resultado}")
