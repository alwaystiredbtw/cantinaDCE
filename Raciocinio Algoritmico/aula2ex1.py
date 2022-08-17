#------------- r.a --------------- # eduardo moura # 


# calcular idade 

print ("Olá, seja bem vindo a calculadora de idade !")
ano = 2022
anoN = int(input("Digite seu ano de nascimento:  "))
idade = ano - anoN
ver = (input("Já fez aniversário esse ano?(Responda sim/nao)  "))


if ver == "sim":
    print (f"Sua idade é {idade} anos !")
else:
    idade -= 1 
    print (f"Sua idade é {idade} anos !")


#-------------------------------#