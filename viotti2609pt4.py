qtdmaior = qtdmenor = 0

#laço para 10x
for aux in range(10) :

    digitado = int(input(f"{aux+1}digite um numero entre 1 a 100: "))
    #vamos validar de 1 a 100
    while(digitado < 1 or digitado > 100) :
        print("numero invalido")
        digitado = int(input(f"{aux+1} digite um numero de 1 a 100:  "))

    if(digitado > 20) :
        qtdmaior += 1 

    if(digitado > 20) :
        qtdmenor += 1 

    print(f"quantidade maior que 20: {qtdmaior}") 
    print(f"quantidade maior que 20: {qtdmenor}") 
