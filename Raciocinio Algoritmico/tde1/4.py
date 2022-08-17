# ----------------------------- #

from cmath import pi


print("Calcule a área de um círculo !")

r = float(input("Digite o diâmetro do círculo: ")) / 2 # raio = diametro/2

pi = 3.14 

A = pi*r**2
um = str(input("Qual a unidade de medida?(m ou cm)"))

print(f"A área do circulio é {A}{um}")
       
