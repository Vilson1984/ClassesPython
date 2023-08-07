#LISTAS OU ARRAY >>> []

#CRIANDO LISTAS 
# lista = [1, 3, 5] cria uma lista com os ns 1, 3 e 5
# lista = list() cria uma lista vazia
# lista = ["Vilson", 39, True, 1,72]
# lista_de_lista = [10[1, 2, 3]]
lista = ["Vilson", 39, 1.72, True]


# INDEXAÇÃO E SLICES (FATIAMENTO)
# Posição[0] >> 1º Termo da lista
# Posição[-1] >> Último termo da lista, [-2]Penúltimo 
# Posição[0:3] >> Posição do 0 até o 2.


#Imprime lista
"""print("Meu nome é", lista[0],", tenho", lista[1], "anos,")"""


# 1 -UTILIZANDO OS PRÓPRIOS ELEMENTOS DA LISTA
'''for elemento in lista:
    print(elemento)'''

# 2 -UTILIZANDO OS ÍNDICES
print(lista) #imprime lista
print(len(lista)) #imprime o comprimento da lista

print (range (len(lista))) #de 0 até menor ki 4

for i in range(len(lista)): #imprimindo a lista pelo índice i
    print (lista[i])