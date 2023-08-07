# CRIANDO FUNÇÕES >>>
#def nomedafunção():
    #AÇÃO DA FUNÇÃO
    
# e depois é só chamar a função pra ser executada
# nomedafunção()



#FUNÇÃO QUE RECEBE PARÂMETROS >>>
#def nomedafunção(parâmetros que espera receber):
    #ação da função

#def saudacao(nome):
#    print(f"Olá {nome}")

#nome = (input('Digite seu nome:'))

#saudacao(nome)



#FUNÇÃO RECEBE MAIS DE UM PARÂMETRO
def saudacao(nome, curso):
    print(f"Olá {nome}, é um prazer ver vc estudando {curso}")

nome = "Vilson"
curso = "Python"
 
saudacao(nome, curso)

#FUNÇÃO COM PARÂMETRO DEFAULT 
# def saudacao(nome, curso="nomedocurso"): >>> já define o valor parâmetro, e a função assume isso como padrão, até que seja mudada.

def soma(a, b, c):
    s = a + b + c
    print(s)

soma(1,1,5)

# FUNÇÃO USANDO RETURN
# def nomedafunção():
# return >>> Aqui eu coloco o que eu quero q faça de fato
# var = nomedafunção (valor parâm) variável q recebe o valor de return
# print (a var q t o valor do return) 

# MINHA CONCLUSÃO, O LEGAL DE USAR RETURN É qUE POSSO CRIAR N VAR REUTILIZANDO A MESMA FUNÇÃO E APENAS IMPRIMINDO OS VALORES DE CADA OPERAÇÃO

def potenciacao(num1, num2):
    return num1 ** num2
resp = potenciacao(2,3)
resp2= potenciacao(5,9)
resp3 = potenciacao(9,144)
print(resp, resp2, resp3)
