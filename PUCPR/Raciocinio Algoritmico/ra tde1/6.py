# leia o valor dos catetos de um triangulo e rangulo e calcule a hipotenusa a = ((b**2 + c**2) ** 0.5) 



print("Seja bem vindo ! Calcule aqui o valor da hipotenusa de um triângulo retângulo utilizando a formula de pitágoras!")

catO = float(input("Digite o valor do cateto oposto: "))
catA = float(input("Digite o valor do cateto adjacente: "))
um = str(input("Qual a unidade de medida? (m / cm / mm)? "))
hip = (catO**2 + catA**2)**0.5




print(f"O valor da hipotenusa é: {hip} {um}")

