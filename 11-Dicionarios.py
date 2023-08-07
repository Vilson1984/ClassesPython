# CRIANDO UM DICIONÁRIO (dictionary)
dicionario = {"Nome":"Vilson", "idade":39, "altura":1.72}
print(dicionario)

#CRIANDO UM DICIONÁRIO VAZIO
dicionario_novo = dict()
print(dicionario_novo)

#ACESSANDO OS ELEMENTOS DE UM DICIONÁRIO
print(dicionario["Nome"])

#ALTERANDO VALORES DAS CHAVES
#nomedicionario ["nomeelemento"] = novo valor do elemento
dicionario ["altura"] = 1.73
print(dicionario)

#CRIANDO CHAVE E PASSANDO VALOR DA MESMA
dicionario["Profissao"] = "Programador"
print(dicionario)

#ITERANDO SOBRE O DICIONÁRIO
for i in dicionario:
    print(i, dicionario[i])