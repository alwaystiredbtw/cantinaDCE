# ------------------ calcular idade 2032 ------------- # 

print ("Olá, seja bem vindo a calculadora de idade !")
ano = 2032
anoN = int(input("Digite seu ano de nascimento:  "))
idade = ano - anoN
ver = (input("Já fez aniversário esse ano?(Responda sim/nao)  ")).replace("não","nao").lower


if ver == "sim":
    print (f"Sua idade em 2032 será {idade} anos !")
else:
    idade -= 1 
    print (f"Sua idade em 2032 será {idade} anos !")
