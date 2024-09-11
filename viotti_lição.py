import math

salario = float(input("informe o seu salario: "))

convenio = float(input("informe o seu convenio: "))

farmacia = float(input("informe o seu valor gasto com farmacia: ")) 

inss = salario * 0.08


irrf = salario * 0.11


salario_liquido = salario - inss - irrf - convenio

print(f"\nResumo dos cálculos:")
print(f"INSS (8% sobre o salário): R$ {inss:.2f}")
print(f"IRRF (11% sobre o salário): R$ {irrf:.2f}")
print(f"Convênios (valor gasto com farmácia): R$ {convenio:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

