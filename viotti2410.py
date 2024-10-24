#area das funções 

def soma(a: int, b: int):
    print(a + b)

#função soma_2 que recebe 2 interiros e devolve um valor inteiro, 
#não existe nada na tela 
def soma_2(a: int, b: int) -> int :
    return a + b 

#usando uma função sem returno  

    soma(32, 88)

    x = 10
    y = 40
    soma(x, y) 

#não vai funcionar 
#a = soma(10, 20) + soma(15, 30)
soma_2(32, 88)
x = 10
y = 40
soma_2(x, y)
a = soma_2(10, 20) + soma_2(15, 30)
print(f"valor de a = {a}") 

#usando uma função com returno de inteiro
res = soma_2(32, 88)
print(res)

x = 10
y = 40
print(soma_2(x,y))
soma_2(x, y)
a = soma_2(10, 20) + soma_2(15, 30)
print(f"valor de a = {a}")
