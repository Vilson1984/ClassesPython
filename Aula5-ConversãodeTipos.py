# CONVERSÃO DE TIPOS
# SINTAXE EXPLÍCITA
# var_convertida = tipo_da_var_desejada(var_não_convertida)
idade = 39
print (idade, (type(idade)))

idade_convertida = str(idade)
print ('Se deu td certo mostrará str >>>', type(idade_convertida))



ano_hoje = 2023 
# CONVERTENDO AUTOMAT EM INT, UM NÚMERO VINDO COMO STR
ano_nasc = int(input('digite o ano do seu nascimento'))
idade = ano_hoje-ano_nasc
print('Você têm', idade, 'anos')