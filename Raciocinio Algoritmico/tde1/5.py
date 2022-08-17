# elabore um algoritmo que leia o preço de un produto e então mostre quais os valores em: 3 parcelas com 5% de juros, 2 parcelas sem juros e 0 preço a vista com 5% de desconto.

print("Veja aqui o valor dos produtos e os métodos de pagamento")

preco = float(input("Qual o preço do produto ? "))

print (f"Em 3 parcelas de {(preco*1.05)/3} com 5% de juros, totalizando {preco*1.05} \nEm 2 parcelas de {preco/2} sem juros, totalizando {preco} \nÀ vista com 5% de desconto, totalizando {preco*0.95}")
