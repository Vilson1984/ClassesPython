"""
# USO LAÇO WHILE
numero_sorteado = 12
numero_escolhido = int(input('chute um número entre 1 e 20:'))
while numero_escolhido != numero_sorteado:
    print('Vc errou, faça outra aposta')
    numero_escolhido = int(input('chute um número:'))
    
if numero_sorteado == numero_escolhido:
    print('Vc acertou')
else:
    print('Vc errou')
"""

#USO WHILE COM CONTADOR
contador = 0
while contador != 5:
    print (contador)
    contador = contador +1