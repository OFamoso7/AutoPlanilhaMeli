import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 0.7


time.sleep(5)
tabela = pd.read_csv("PlanilhaSvc.csv")
tabelaEX = pd.read_csv("PlanilhaExtenso.csv")
print(tabela)

for linha in tabela.index:
    svc = tabela.loc[linha, "SVC"]
    ex = tabelaEX.loc[linha, "SVC_EX"]

    #atalho para entrar na barra de pesquisa
    pg.hotkey("ctrl", "f")
    #ecrever o nome do SVC
    pg.write(str(ex))
    time.sleep(3)
    #clicar na conversa do SVC
    pg.click(x=153, y=197)
    #clicar no clips
    pg.click(x=513, y=708)
    #clicar em documentos
    pg.doubleClick(x=485, y=573)
    #tempo pra carregar o documento
    time.sleep(5)
    #click na pasta download
    pg.click(x=70, y=184)
    #click na barra de pesquisa das pastas
    pg.click(x=238, y=417)
    #escrever o nome do SVC
    pg.write(str(svc))
    #clicar no ultimo documento com o nome escrito
    pg.click(x=261, y=435)
    #clicar em enviar
    pg.click(x=511, y=447)
    #tempo para esperar o documento carregar
    time.sleep(3)
    #escrever a mensagem padrão do envio dos documentos
    pg.write("Segue planilha atualizada!")
    #enviar mensagem com documento correto
    pg.click(x=960, y=696)
    pg.click(x=384, y=119)
