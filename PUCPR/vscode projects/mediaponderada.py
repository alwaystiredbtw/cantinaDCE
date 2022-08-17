# ------ média ponderada exércicio por: Eduardo Moura de Resende Jargas

# ------ variáveis
count = int(1)
media = 0.0
quantnotas = int(input('Quantas notas deseja calcular ?:'))
somapeso = 0

while count <= quantnotas:
    print('Insira a nota e peso', count, 'abaixo: ')
    nota = float(input('Digite a nota:'))
    peso = float(input('Digite o peso da nota(sem a % ex: 30): '))
    somapeso += peso
# ------ verificação do peso
    if somapeso > 100:
        print('A soma dos pesos deve ser igual 100%, digite novamente a nota', count)
        somapeso -= peso
        continue
# ------ calculo da média
# ------
    soma = ((nota * peso) / 100)
    media += soma
# ------ contador
    count += 1
print('A média final é', media, '!')
