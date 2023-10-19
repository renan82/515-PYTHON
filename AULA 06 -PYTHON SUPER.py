#AULA 06 - REVISÃO - EXERCICIOS

# #QUESTÃO 01 - 
# def soma(n1,n2):
#     return n1 + n2

# n1 = int(input("Digite o primeiro numero: "))
# n2 = int(input("Digite o segundo numero: "))
# print(f"A soma dos números digitados é: {soma(n1,n2)}")

# #QUESTÃO 02 - 
# quadrado = lambda z : z **2
# numero = int(input("Digite um número: "))
# print(quadrado(numero))

# # QUESTÃO 03 - 
# 03) FAÇA UMA FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS E RETORNE QUAL É O MAIOR ENTRE ELES
# def maior(lista):
#     return max(lista)

# lista = []
# for x in range(5):
#     numero = int(input("Digite um número a ser adicionado: "))
#     lista.append(numero)

# print(f"O maior número da lista foi {maior(lista)}")

#QUESTÃO 04
# # FAÇA UMA FUNÇÃO LAMBDA PARA MULTIPLICAR TODOS OS NÚMEROS DE UMA LISTA POR 2 (VOCE ESCOLHE QUANTOS ITENS VAI ADICIONAR NA LISTA)

# lista = []
# for c in range(5):
#     n = int(input("Digite o número a ser adicionado : "))
#     lista.append(n)
# quadrados = list(map(lambda x : x **2, lista))
# print(quadrados)

# def resultado(lista):
#     return lista * 2
# print(resultado)
# lista2 = []





# 05) FAÇA UMA FUNÇÃO LAMBDA QUE RECEBE UM NÚMERO E VERIFICA SE O NÚMERO É PAR

# par = lambda x : "é par" if x % 2 == 0 else "é impar"
# r = int(input("Digite um número para verificar se é PAR OU ÍMPAR: "))
# print(par(r))

# 06) FAÇA UMA FUNÇÃO QUE RECEBA UMA LISTA DE NÚMERO E RETORNE A MÉDIA DOS NÚMEROS DESSA LISTA

#MÉTODO  MAIS ENXUTO
# def media(lista):
#     return sum(lista) / len(lista)

# #MÉTODO CONVENCIONAL

# def media(lista):
#     soma = 0
#     for n in lista:
#         soma += n
#     media = soma/len(lista)
#     return media

# lista = []

# for x in range(5):
#     n = int(input("Digite um número para ser adicionado na lista: "))
#     lista.append(n)
        
# print(media(lista))
#07 FAÇA UMA FUNÇÃO QUE RECEBE UM TEXTO E RETORNE A QUANTIDADE DE VOGAIS QUE AQUELE TEXTO CONTÉM



# AULA 06 - MODULOS
# from caracter import contar_vogais, contar_consoantes
# from caracter import * # FAZ A IMPORTAÇÃO DE TODAS FUNÇÕES DENTRO DO ARQUIVO CARACTER SALVO NA PASTA DO PYTHON SEM PRECISAR MENCIONAR O MODULO (caracter)
# import texto.caracter as c # TRAZ O MODULO LOCALIZADO EM OUTRA PASTA, NUMA SUBPASTA
# texto = str(input("Digite um texto qalquer: "))
# print(f"O número de vogais é: {c.contar_vogais(texto)}")

# # #DICA: CRTL + D = SELECIONAR VARIAS PALAVRAS REPETIDAS

# while True:
#     menu = int(input("""
#                 1 - CONTAR AS VOGAIS
#                 2 - CONTAR AS CONSOANTES
#                 3 - CONTAR O TAMANHO DO TEXO
#                 4 - TRANSFORMAR EM MAIUSCULO
#                 5 - TRANSFORMAR EM MINUSCULO
#                 6 - SAIR
#     """))
#     if menu == 1:
#         print(c.contar_vogais(texto))
        
#     elif menu == 2:
#         print(c.contar_consoantes(texto))
        
#     elif menu == 3:
#         print(c.tamanho_da_palavra(texto))
        
#     elif menu == 4:
#         print(c.transformar_em_maiusculo(texto))
        
#     elif menu == 5:
#         print(c.transformar_em_minusculo(texto))
        
#     elif menu == 6:
#         break

#EXERCICIO
from funcoesmatematicas import *
num1 = int(input("Digite um numero qualquer: "))
num2 = int(input("Digite um segundo numero qalquer: "))


# #DICA: CRTL + D = SELECIONAR VARIAS PALAVRAS REPETIDAS

while True:
    menu = str(input("""
                1 - SOMAR
                2 - SUBTRAIR
                3 - MULTIPLICAR
                4 - DIVIDIR
                5 - SAIR 
    """))
    if menu == "1":
        print(soma(num1,num2))
            
    elif menu == "2":
        print(subtracao(num1,num2))
            
    elif menu == "3":
        print(multiplicacao(num1,num2))
            
    elif menu == "4":
        print(divisao(num1,num2))
            
    elif menu == "5":
        break
      
