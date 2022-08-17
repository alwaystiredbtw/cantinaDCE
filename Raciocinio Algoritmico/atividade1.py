# aula 01 ------------ atividade 1 #
from dataclasses import replace
import re

print("Olá ! Seja bem vindo ! Digite seus dados a seguir, conforme solicitado.")





nome = str(input("Qual seu nome?: "))

cpf = str(input("Digite seu CPF: ")).replace(".","").replace("-","")

tel = str(input("Digite seu telefone(com DDD):"))
for caracteres in "( ) -":
    tel = tel.replace(caracteres, "")

anoNasc = str(input("Digite sua data de nascimento(ex: 08/03/2001): ")).replace("/","")




print ("Seu nome é:\n",nome,
"\nSeu CPF é:\n",("{}.{}.{}-{}".format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:])),
"\nSeu número de telefone é:\n",("({}){}-{}".format(tel[:2],tel[2:7],tel[7:])),
"\nData de nascimento:\n",("{}/{}/{}".format(anoNasc[:2],anoNasc[2:4],anoNasc[4:])))








# -------------outras opções------------ #

############ .FORMAT seguidos ############# 
#       tel = str(input("Digite seu telefone(com DDD):")).replace("(","").replace(")","").replace("-","")
#       print (tel)

############# REGEX ##############
#    tel = str(input("Digite seu telefone(com DDD):"))
#    telPrint = re.sub("\(|\)|-","", tel)
#    print (telPrint)

