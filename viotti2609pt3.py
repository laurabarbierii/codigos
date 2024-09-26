#programa só aceita numeros positivos

numero = int (input("digite o numero positivo: "))

#ROTINA DE VALIDAÇÃO
while(numero < 0) :
    print("numero invalido")
    numero = int(input("tente outro numero positivo: "))

print("agora sim, voce digitou corretamente...")
