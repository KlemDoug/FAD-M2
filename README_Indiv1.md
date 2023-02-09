
###########################################################################################################

## Descrição ##

Este repositório (FAD-M2) contém os arquivos utilizados para disponibilizar a infraestrutura necessária dos projetos referentes ao Módulo 2 (Estrutura de Dados e Inteligência Emocional) do curso de Formação em Análise de Dados promovido pela parceria SENAC/Resilia. Neste caso, é detalhado o primeiro projeto individual do módulo:

Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade de um candidato com uma vaga de acordo com seu resultado nas etapas do processo seletivo. Para isso foi criado um teste que devolve uma string no seguinte formato: eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills).

Com isso, teremos uma lista para armazenar esses resultados (e outros resultados que quiser no mesmo formato; o código funciona para qualquer lista que seja inserida nesse formato). Depois, haverá uma função que busca o candidato de acordo com os critérios digitados pelo usuário.


###########################################################################################################

## Arquivos ##

* **Projeto Individual 1 Módulo2.py**: arquivo contendo o código programado em python para execução do simulador de busca por candidatos conforme requerido no projeto.
* **README_Indiv1.md**: arquivo que abriga uma breve descrição do projeto com o título, funcionalidades e detalhes de implementação.


###########################################################################################################

## Funcionalidades ##

### * 1: Looping para leitura das listas desejadas conforme a demanda que o usuário for requerir ###

```python
consulta = input("Deseja iniciar a simulação (sim)?")
candidatos = []
resultados = []
while consulta == 'sim':
    candidatos.append(input("Informe o nome do candidato:"))
    e = int(input("Informe a nota da entrevista:"))
    t = int(input("Informe a nota do teste teórico:"))
    p = int(input("Informe a nota do teste prático:"))
    s = int(input("Informe a nota de avaliação das soft skills:"))
    resultados.append(f"e{format(e)}_t{format(t)}_p{format(p)}_s{format(s)}")
    consulta = input("Deseja continuar (sim/não)?")
else:
    print("Pronto! A simulação de candidatos dará prosseguimento...")
```
    
<sub>***Inicia-se o código com um input para a entrada no looping e o preenchimento das duas listas principais: uma que armazena os nomes dos candidatos e outra para armazenar os resultados das quatro avaliações numa string única. Note que após o input individual de cada nota do candidato, utiliza-se o comando append com o format para que todas assumam a estrutura 'eX_tX_pX_sX'. Por fim, insere-se um input que permite a quebra do looping de acordo com a quantidade de candidatos que o usuário pretenda inserir.***</sub>



### * 2: Leitura das notas de avaliação para a função de busca ###

```python
print("Por favor, informe agora os critérios mínimos desejados do(s) candidato(s):")
e2 = int(input("Entrevista:"))
t2 = int(input("Teste Teórico:"))
p2 = int(input("Teste Prático:"))
s2 = int(input("Soft Skills:"))
```

<sub>***Nota: supõe-se nesse modelo do projeto que todas as notas trabalhadas serão números inteiros. É possível trabalhar com números decimais, se for necessário; basta colocar 'float(input())' em substituição.***</sub>



### * 3: Função para verificação de notas sugeridas com as listas de candidatos ###

```python
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
        else:
            pass
print(ocandidato(e, t, p, s))
```

<sub>***Cria-se uma função que recebe como argumentos os quatro input anteriores. Nela, teremos uma nova lista que receberá os resultados tratados da lista de avaliações original. Esse tratamento passa por uma série de variáveis de conversão que utilizam, respectivamente, os comandos .translate, .maketrans, .join, .split e list(map(type,list)) para, justamente, remover os caracteres desnecessários e deixar em evidência somente os algarismos daquela string única e serem mais facilmente invocados na condicional seguinte. Por fim, utiliza-se o comando .zip para percorrer-se simultaneamente a lista de resultados tratada e a lista com os nomes dos candidatos e executar a condicional que compara as notas das avaliações desejadas com as notas das avaliações carregadas inicialmente no código. Caso algum candidato apresente notas iguais ou superiores às desejadas, a função fará um procedimento dizendo qual candidato e com quais resultados se mostrou apto aos critérios escolhidos.***</sub>

###########################################################################################################


