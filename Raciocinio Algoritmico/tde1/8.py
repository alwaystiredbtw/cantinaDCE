#algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilindricos de combustivel em que sao fornecidos a altura e o raio desse cilindro 
#  A lata de tinta custa 50 
# Cada lata tem 5 litros
# Caad litro pinta 3 m²
# entradas: altura e raio
#saida custo em R$ e qnt de latas


print("Olá seja bem vindo! Calcule aqui seu gasto para pintar tanques cilindricos de combustivel!")


h = float(input("Qual a altura do cilindro(em m)? "))
r = float(input("Qual o raio do cilindro(em m)? "))

aTotal = 2 * 3.14 * r * (r + h)

# se cada lata pinta 3m², então: 
qtLatas = aTotal / 3 #m2 
# como não é possível comprar meia lata, é necessário arredondar o a quantidades de lata para + 
def arredonda(qtLatas):
    return int(qtLatas + (0 if qtLatas % 3 == 0 else 1))    

qtLatas = arredonda(qtLatas)
# calculo do valor por latas
valor = qtLatas * 50 #reais


print(f"O valor necessário para pintar o cilindro de {aTotal:.2f} m², utilizando {qtLatas} latas, com um valor final de R${valor:.2f} reais!")