#descobre se o numero e imapar ou par
#e pede para executar novamente

resp = ""
while(resp != "N" and resp != "n") :
    (input("digite um numero: "))
    numero= int(input("digite um numero: "))
    if(numero % 2 == 0) :
        print("esse numero é par...")
    else : 
        print("esse numero é impar...")

    resp = input("deseja executar novamente (S/N): ")
