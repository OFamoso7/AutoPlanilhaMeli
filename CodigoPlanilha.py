import pyautogui as pg
import time
import pandas as pd


pg.PAUSE = 0.3




# PASSO 1: Abrir sistema do MELI (OU DEIXAR EM ALGUMA POSIÇÃO PADRÃO PARA O CLICK)
# PASSO 2: baixar planilha do sistema
time.sleep(6)
pg.click(x=1269, y=329)
#DEIXA UMA PLANILHA ABERTA EM BRANCO
# Click na aba da planilha 
pg.click(x=24, y=15)
#Click no "archivo", sim são dois de propósito por conta da página de download
time.sleep(2)
#pg.click(x=77, y=153)
time.sleep(2)
pg.click(x=77, y=153)
time.sleep(1)
#click no importar
pg.click(x=109, y=249)
#Click no subir
time.sleep(3)
pg.click(x=658, y=260)
time.sleep(1)
#Click no botão azul
pg.click(x=663, y=548)

#Click no documento para planilha
time.sleep(3)
pg.doubleClick(x=292, y=162)
#Tempo para carregar a planilha
time.sleep(5)

#Click no IMPORTAR DADOS
pg.click(x=729, y=550)
#tempo para carregar a planilha após importar
time.sleep(15)

#selecionar tudo
pg.hotkey('ctrl', 'a' )
time.sleep(1)
#Click nos 3 pontinhos
pg.click(x=1087, y=192)
time.sleep(1)
#click no filtro
pg.click(x=1012, y=233)
time.sleep(1)
#Click nos 3 pontinhos
pg.click(x=1087, y=192)
time.sleep(1)


#arrumar filtro das transportadoras de A a Z 
#click nos filtros
pg.click(x=1047, y=282)
time.sleep(1)
#click no A a Z
pg.click(x=852, y=318)
time.sleep(1)
#descer a barrinha
#pg.scroll(-5000)
#click para aplicar
#pg.click(x=975, y=706)


#arrumar filtros de REVERTIDOS
#click no filtro

pg.click(x=537, y=283)
time.sleep(2)
#click para deixar apenas os revertidos
pg.click(x=344, y=619)
time.sleep(1)
#descer a barrinha
pg.scroll(-5000)
time.sleep(1)
#click no aplicar
pg.click(x=457, y=703)


#colocando a planilha com os SVC na variável 'tabela'
tabela = pd.read_csv("PlanilhaSvc.csv")
tabelaEX = pd.read_csv("PlanilhaExtenso.csv")
print(tabela)



for linha in tabela.index:
    svc = tabela.loc[linha, "SVC"]
    ex = tabelaEX.loc[linha, "SVC_EX"]

    #click nos filtros do FACILITY
    pg.click(x=738, y=284)
    time.sleep(1)
    #remover os filtros 
    pg.click(x=590, y=534)

    #descer a barrinha
    pg.scroll(-5000)

    #clicar na barra de pesquisa
    pg.click(x=532, y=502)
    #escrever oque está na planilha
    pg.write(str(svc))
    #selecionar
    pg.click(x=522, y=541)
    #aplicar
    pg.click(x=663, y=701)
    #clicar em arquivo
    pg.click(x=82, y=153)
    #clicar em renomear
    pg.click(x=137, y=507)
    #escrever o nome do SVC que foi baixado
    pg.write(str(ex))
    #pressionar enter
    pg.press("enter")
    #clicar no arquivo de novo
    pg.click(x=82, y=153)
    #clicar em baixar
    pg.click(x=160, y=392)
    #clicar no formato 
    pg.click(x=467, y=531)

    #tempo pro pc carregar os documentos


#pesquisar o SVC
#pg.write('SMG1')
#Selecionar o SVC correto que aparecerá na busca
#pg.click(x=527, y=540)
#Clicar em aplicar
#pg.click(x=663, y=705)


#Pontos para falar na reunião
# 1- SOBRE OS PIXELS
# 2- SOBRE O TEMPO DE RODAR
# 3- SOBRE COMO FUNCIONA(RAPIDAMENTE)
# 4- SOBRE AS PLANILHAS EM BRANCO QUE PODEM SER ENVIADAS
# 5- pedir Listas dos grupos


