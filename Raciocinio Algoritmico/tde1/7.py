# faça um algoritmo que dado o horário (hora minuto e segundo) e calcule o total de segundos que transcorreram durante o dia


print("Calcule quantos segundos se passaram até a hora desejada !")

horario= input("Qual o horário desejado? (utilize hh:mm:ss)? ").replace(":","")

hora = int(horario[0:2])
minuto = int(horario[2:4])
segundo = int(horario[4:])

count = segundo + ((hora*60 + minuto)*60)
  
print(f"Se passaram {count} segundos da 00:00 às {horario[:2]}:{horario[2:4]}:{horario[4:]}")




