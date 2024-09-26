somapar = somaimpar = valoresentre = divisiveis = 0

for numero in range(500, 10001, 1) :
    if numero (numero % 2 == 0) :

        somapar += numero
    else :
        somaimpar += numero

    if(numero >= 600 and numero <= 8765) :
        valoresentre += numero

    if(numero % 4 == 0 and numero % 5 == 0) :
        divisiveis += numero

    #saida dos dados

    print(f"")
