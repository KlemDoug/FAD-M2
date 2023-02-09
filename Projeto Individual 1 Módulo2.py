##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto Individual 1 - Módulo 2 - Deu Match!                  #
#  !/usr/bin/env python3                                         #
#  -*- coding: utf-8 -*-                                         #
#  Criado por: Douglas Klem Portugal do Amaral                   #
#  Data de criação: 02/02/2023                                   #
#  versão = '3.11(64-bit)'                                       #
##################################################################
#
# Atividade:
#
# Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
# de um candidato com uma vaga de acordo com seu resultado nas etapas do
# processo seletivo.
# Para isso foi criado um teste que devolve uma string no seguinte formato:
# eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em
# uma das etapas do processo - entrevista, teste teórico, teste prático e
# avaliação de soft skills).
#
# Criar com Python uma lista para armazenar esses resultados
# (e outros resultados que quiser no mesmo formato; o código
# precisa funcionar para qualquer lista que seja inserida nesse
# formato) e depois uma função que busca o candidato de
# acordo com os critérios digitados pelo usuário.
#
print('*'*100)
print("Bem-vindx ao Jobs Matching Maker FAD!")
print('*'*100)
print("Verificaremos a compatibilidade do(s) candidato(s) de acordo com seu(s) resultados.")
print('*'*100)
consulta = input("Deseja iniciar a simulação (sim)?")
print('*'*100)
candidatos = []
resultados = []
while consulta == 'sim':
    candidatos.append(input("Informe o nome do candidato:"))
    print('*'*100)
    e = int(input("Informe a nota da entrevista:"))
    print('*'*100)
    t = int(input("Informe a nota do teste teórico:"))
    print('*'*100)
    p = int(input("Informe a nota do teste prático:"))
    print('*'*100)
    s = int(input("Informe a nota de avaliação das soft skills:"))
    print('*'*100)
    resultados.append(f"e{format(e)}_t{format(t)}_p{format(p)}_s{format(s)}")
    consulta = input("Deseja continuar (sim/não)?")
    print('*'*100)
else:
    print("Pronto! A simulação de candidatos dará prosseguimento...")
    print('*'*100)

print('.')
print('.'*2)
print('.'*3)
print(' '*3)
print("Lista de candidatos:", candidatos)
print('*'*100)
print("Lista de resultados:", resultados)
print('*'*100)
print("Por favor, informe agora os critérios mínimos desejados do(s) candidato(s):")
print('*'*100)
e2 = int(input("Entrevista:"))
print('*'*100)
t2 = int(input("Teste Teórico:"))
print('*'*100)
p2 = int(input("Teste Prático:"))
print('*'*100)
s2 = int(input("Soft Skills:"))
print('*'*100)


def ocandidato(e2, t2, p2, s2):
    tratados = []
    for aval in resultados:
        tradutor = ['e', 't', 'p', 's']
        convert1 = aval.translate(str.maketrans('', '', ''.join(tradutor)))
        convert2 = convert1.split('_')
        convert3 = list(map(int, convert2))
        tratados.append(convert3)
    for trat, nomes in zip(tratados, candidatos):
        if int(trat[0]) >= e2 and int(trat[1]) >= t2 and int(trat[2]) >= p2 and int(trat[3]) >= s2:
            print("O candidato", nomes, "com os resultados",
                  aval, "atende aos critérios mínimos informados.")
            print('*'*100)
        else:
            pass


print(ocandidato(e, t, p, s))
print("Obrigado por utilizar o Jobs Matching Maker FAD! Volte sempre!")
print('*'*100)
#
# Referências (último acesso em 06/02/2023):
# https://www.pythonprogressivo.net/2018/10/Unir-Separar-Strings-join-split-Tutorial-Python.html
# https://www.techiedelight.com/pt/remove-specific-characters-string-python/#:~:text=Usando%20str.&text=Uma%20solu%C3%A7%C3%A3o%20eficiente%20%C3%A9%20usar,maketrans()%20fun%C3%A7%C3%A3o.
# https://www.techiedelight.com/pt/convert-list-of-string-into-list-of-integers-python/
#
#
