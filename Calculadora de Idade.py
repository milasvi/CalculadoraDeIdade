print('Bem-vinde à Calculadora de Idade!')

ano = int(input('Em que ano estamos?'))
nascimento = int(input('Em que ano você nasceu?'))
idade = ano - nascimento

print(f'Você deve ter {idade}!')
if idade > 17 :
    print('...e já chegou à maoridade, parabéns!.')
elif idade < 17:
    print('...e é nenem ainda!')  
elif idade > 59:
    print('...e é jovem ainda!')

print('Temos um bônus!')
bonus = input('Deseja saber quantos anos terá ou tinha em algum ano especifico?[S/N]')
if bonus == 'S':
    ano2 = int(input('Qual ano deseja?'))
    if ano2 < ano:
        idade2 = ano2 - nascimento
        print(f'Você tinha {idade2} anos em {ano2}!')
        print('Obrigade por usar a Calculadora de idade! n/Até mais!')
    elif ano2 > ano:
        idade2 = ano2 - nascimento
        print(f'Você terá {idade2} anos em {ano2}!')
        print('Obrigade por usar a Calculadora de idade! \nAté mais!')
else:
    print('Então tá...Obrigade por usar a Calculadora de idade! \nAté mais!')
        