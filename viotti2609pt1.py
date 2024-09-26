#uso de laço de repetição WHILE para contagem e validações 

#mostrar os numeros de 1 a 5 na tela

#com for + range
for numero in range(1,6,1):
    print(f"{numero} ", end="")

print("Com while...")
#com while
numero = 1 #inicializa o contador 
while (numero < 6) :
    print(f"{numero} " , end="")

    #faz o incremento
    numero += 1 
