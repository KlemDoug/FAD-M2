##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto Individual 2 - Módulo 2 - Contratado!                 #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Douglas Klem Portugal do Amaral                   #
#  Data de criação: 13/02/2023                                   #
#  versão = '3.11(64-bit)'                                       #
##################################################################
#
# Atividade:
#
# Uma empresa de recrutamento recebeu muitos currículos
# para determinadas vagas e agora precisa classificar
# quantos candidatos tem o perfil necessário e quantos
# candidatos estão concorrendo a cada vaga específica.
#
# Desenvolva um projeto (usando dicionários) que vai gravar
# a quantidade de currículos para aquela vaga e quantas
# pessoas têm as palavras-chave necessárias no currículo.
# Para isso, nosso código Python vai checar para qual vaga a
# pessoa se inscreveu e o resumo que a pessoa enviou em
# busca dessas informações.
#
from os import system, name
from time import *


def limpaTela():
    if name == 'nt':
        X = system('cls')
    else:
        X = system('clear')
    return X


print('*'*100)
print("Bem-vindx ao Jobs Curriculum Analyser FAD!")
print('*'*100)
print("Verificaremos a compatibilidade do(s) candidato(s) por seu(s) currículos e as vagas disponíveis.")
print('*'*100)
vaga1padrao = {'Vaga 1': 'Python, Programação, Desenvolvimento'}
vaga2padrao = {'Vaga 2': 'Análise de Dados, Dados, SQL'}
for i in vaga1padrao:
    for j in vaga2padrao:
        print(f"Opções: 1: {i} para {vaga1padrao['Vaga 1']}; \n"
              f"        2: {j} para {vaga2padrao['Vaga 2']}; \n"
              f"        0: para encerrar esta etapa."
              )
print('*'*100)
consulta = True
dictvaga1 = {}
dictvaga2 = {}
quanti_cv1 = 0
quanti_cv2 = 0
quanti_cand1 = 0
quanti_cand2 = 0
while consulta != 0:
    consulta = int(input(
        "Informe para qual vaga deseja se inscrever:"))
    print('*'*100)
    resumo = input("Informe seu resumo/minibio para a vaga anterior:")
    print('*'*100)
    if consulta == 1:
        dictvaga1.update({quanti_cv1: resumo})
        quanti_cv1 = quanti_cv1+1
        resuminho = str.lower(resumo)
        resuminho_ = resuminho.split()
        if "python" in resuminho_ and 'programação' in resuminho_ and 'desenvolvimento' in resuminho_:
            quanti_cand1 = quanti_cand1+1
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
        print('*'*100)
    elif consulta == 2:
        dictvaga2.update({quanti_cv2: resumo})
        quanti_cv2 = quanti_cv2+1
        resuminho2 = str.lower(resumo)
        resuminho2_ = resuminho2.split()
        if "análise" in resuminho2_ and 'de' in resuminho2_ and 'dados' in resuminho2_ and 'sql' in resuminho2_:
            quanti_cand2 = quanti_cand2+1
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
        print('*'*100)
    else:
        print("Opção de vaga inválida.")
        print('*'*100)
        consulta = int(
            input("Digite 9 para mais vagas ou 0 para encerrar:"))
        print('*'*100)
else:
    sleep(3)
    print("Pronto! Carregando análise dos currículos fornecidos...")
    print('*'*100)
sleep(3)


def final(dictvaga1, dictvaga2, quanti_cand1, quanti_cand2):
    totais = len(dictvaga1)+len(dictvaga2)
    finalvaga1 = {len(dictvaga1): quanti_cand1}
    finalvaga2 = {len(dictvaga2): quanti_cand2}
    print(f"Foram recebidas {totais} candidaturas no total, sendo \n"
          f"{len(dictvaga1)} para a Vaga 1 e {len(dictvaga2)} para a Vaga 2. \n"
          f"Desse total foram encontrados, respectivamente, \n"
          f"{finalvaga1[len(dictvaga1)]} candidato(s) com currículos pertinentes à Vaga 1 \n"
          f"e {finalvaga2[len(dictvaga2)]} candidato(s) com currículos pertinentes à Vaga 2.")
    print('*'*100)


print(final(dictvaga1, dictvaga2, quanti_cand1, quanti_cand2))
print('*'*100)
sleep(13)
print("Obrigado por utilizar o Jobs Curriculum Analyser FAD! Volte sempre!")
print('*'*100)
sleep(7)
limpaTela()
#
# Referências (último acesso em 16/02/2023):
# https://pt.stackoverflow.com/questions/403300/como-adicionar-uma-nova-chave-em-um-dicion%c3%a1rio
# https://docs.python.org/pt-br/3/library/string.html
# https://www.delftstack.com/pt/howto/python/strings-comparison-python/
# https://www.delftstack.com/pt/howto/python/number-of-keys-in-dictionary-python/#:~:text=Contar%20o%20n%C3%BAmero%20de%20chaves%20no%20dicion%C3%A1rio%20Python,o%20n%C3%BAmero%20de%20chaves%20em%20um%20dicion%C3%A1rio%20Python
#
#
