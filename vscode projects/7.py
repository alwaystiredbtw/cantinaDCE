# ---------------------------
mes = ''
datan = input('Digite sua data de nascimento(XX/XX/XXXX):').replace('/', '')
modo = int(input('\n 1 – Data simples. Ex.: 10/08/1990;'
                 '\n 2 – Data abreviada. Ex.: 10/ago/1990;'
                 '\n 3 – Data completa. Ex.: 10 de agosto de 1990;''\n Qual modo deseja exibir a data?'))

if modo == 1:
    print('{}/{}/{}'.format(datan[0:2], datan[2:4], datan[4:8]))
elif modo == 2:
    if datan[2:4] == '01':
        mes = 'jan'
    elif datan[2:4] == '02':
        mes = 'fev'
    elif datan[2:4] == '03':
        mes = 'mar'
    elif datan[2:4] == '04':
        mes = 'abr'
    elif datan[2:4] == '05':
        mes = 'mai'
    elif datan[2:4] == '06':
        mes = 'jun'
    elif datan[2:4] == '07':
        mes = 'jul'
    elif datan[2:4] == '08':
        mes = 'ago'
    elif datan[2:4] == '09':
        mes = 'set'
    elif datan[2:4] == '10':
        mes = 'out'
    elif datan[2:4] == '11':
        mes = 'nov'
    elif datan[2:4] == '12':
        mes = 'dez'
    print('{}/{}/{}'.format(datan[0:2], mes, datan[4:8]))
elif modo == 3:
    if datan[2:4] == '01':
        mes = 'janeiro'
    elif datan[2:4] == '02':
        mes = 'fevereiro'
    elif datan[2:4] == '03':
        mes = 'março'
    elif datan[2:4] == '04':
        mes = 'abril'
    elif datan[2:4] == '05':
        mes = 'maio'
    elif datan[2:4] == '06':
        mes = 'junho'
    elif datan[2:4] == '07':
        mes = 'julho'
    elif datan[2:4] == '08':
        mes = 'agosto'
    elif datan[2:4] == '09':
        mes = 'setembro'
    elif datan[2:4] == '10':
        mes = 'outubro'
    elif datan[2:4] == '11':
        mes = 'novembro'
    elif datan[2:4] == '12':
        mes = 'dezembro'
    print('{} de {} de {}'.format(datan[0:2], mes, datan[4:8]))
