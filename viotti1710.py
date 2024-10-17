qtd_i = qtd_a= 0

while True:
 for cont in range(10):
    fruta = input(f"Digite a{cont+1}ª fruta:")
    qtd_a = qtd_i= 0
    for pos in range (len(fruta)):
        if(fruta.upper()[pos]== "A"):
            qtd_a +=1
        if(fruta.upper()[pos]=="I"):
            qtd_i += 1
 print (f"Total de letras 'A' ou 'a' para {fruta} = {qtd_a}")
 print (f"Total de letras 'I' ou 'i' para {fruta} = {qtd_i}")
 resp = input ("Quer executar (S/M)?").upper()
 if(resp == "N"):
     break
