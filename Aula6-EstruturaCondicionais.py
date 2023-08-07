#IF ELSE
idade = int(input('Digite sua idade:'))

if idade >= 18:
    print('Vc é de maior')
else:
    print('Vc é de menor')

#ELSE IF = ELIF
"""
media = float(input('Informe sua média:'))
if media >= 7:
    print ('Vc foi aprovado')
elif media >=5:
    print('vc foi para recuperação')
else:
    print('Vc foi reprovado')
"""

#COMPARAÇÃO CONJUTA >>> AND ou OR
media = float(input('informe sua media'))
presenca = 50

if media >= 7 and presenca >= 70:
    print('Vc está aprovado')
else:
    print('Vc está reprovado')