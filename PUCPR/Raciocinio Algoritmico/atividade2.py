# ----------- atividade 2 imc ---------- #


print ("Olá seja bem vindo a calculadora de IMC ! Vamos lá?")

peso = (input("Digite seu peso:")).replace(",",".")
alt = (input("Digite sua altura:")).replace(",",".")
p = float(peso)
a = float(alt)
imc = (p / a**2)

print (f"Seu IMC é: {imc:.2f}","consulte a tabela no link abaixo:\nhttps://www.calculoimc.com.br/tabela-de-imc/")
