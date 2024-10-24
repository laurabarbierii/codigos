#variáveis
tipoInstalacao = ""
totalKw = 0
valorPagar = 0.00
precoKwh = 0.00

#entrada de dados
print("Informe: ")
print("I - Instalação Industrial")
print("C - Instalação Comercial")
print("R - Instalação Residencial")
tipoInstalacao = input("Qual tipo de Instalação? ")
totalKw = int(input("Quantos kWh foram gastos? "))

#testes
if tipoInstalacao == "I" or tipoInstalacao == "i" :
    if totalKw <= 5000 :
        precoKwh = 0.55
    else :
        precoKwh = 0.60
elif tipoInstalacao == "R" or tipoInstalacao == "r" : 
    if totalKw <= 500 :
        precoKwh = 0.40
    else :
        precoKwh = 0.65
elif tipoInstalacao == "C" or tipoInstalacao == "c":
    if totalKw <= 1000 :
        precoKwh = 0.55
    else :
        precoKwh = 0.60        
else :
    print("Tipo de Instalação Inválida...")        
    print("Os valores não serão calculados...")

#vamos calcular somente se o tipo da instação for ICRicr
if tipoInstalacao == "C" or tipoInstalacao == "c" or tipoInstalacao == "I" or   tipoInstalacao == "i" or tipoInstalacao == "R" or tipoInstalacao == "r" :
    #Calculos
    valorPagar = precoKwh * totalKw

    #saida de dados
    print(f"Valor total a Pagar: R$ {valorPagar:10.2f}")

