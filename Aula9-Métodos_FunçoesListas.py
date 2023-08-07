#MÉTODO APPEND (ADICIONA UM ELEMENTO NA LISTA, sempre no final)
#SINTAXE: nomedalista.append(valoradd)

#Criando lista e imprimindo cada item usando range
carro = ["alfa", "bmw", "corvet"]
print (len(carro))#check Nº itens
for i in range(len(carro)):
    print (carro[i])

#ADD ÍTEM(CARRO)
carro.append("Dodge")
print (carro)

#MÉTODO INSERT, ADD E ESCOLHE A POSIÇÃO
carro.insert(2, "bulgary")
print (carro)

#MÉTODO EXTEND ("CONCATENA" AS 2 LISTAS)
carro_brasil = ["brasília", "corsa", "del rey"]
print(carro_brasil)

carro.extend(carro_brasil)
print(carro)

#MÉTODO POP - ELIMINA ELEMENTOS DA LISTA
#se não especificar, nenhum parâmetro elimina o último elemento
carro.pop()
print(carro)

carro.pop(1)
print(carro)

#REMOVE ESCOLHE O VALOR E NÃO A POSIÇÃO DO ELEMENTO
carro.remove("Dodge")
print(carro)

#COUNT, CONTA UANTAS VZS REPETE O ELEMENTO
carro.append("alfa")
print(carro)
print (carro.count("alfa"))

#INDEX, DIZ O ÍNDICE DE UM ELEMENTO DA LISTA
print (carro.index("brasília"))

#SORT, ORDENA A LISTA
carro.sort()
print(carro)

#Coloca a lista em descrescente
carro.sort(reverse=True)
print(carro)


# SUM (SOMA OS ELEMENTOS DA LISTA), Só p/ Nº
# sum(nomedalista)

#MÁX (MAIOR ELEMENTO DA LISTA)

#MIN (MENOR ELEMENTO DA LISTA)