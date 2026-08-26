#pip install pyautogui
#pip install pandas openpyxl

#bibliotecas
import pyautogui
import time
import pandas
from pathlib import Path


#variaveis
link = 'https://sheetigo.com/pt'
arquivo = Path(__file__).parent / 'produtos.csv'
tabela = pandas.read_csv(arquivo)




#comandos
#pyautogui.PAUSE = 0.5

#passo1: entrar no site
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
#pausa
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write(link)
pyautogui.press('enter')
#pausa
time.sleep(4)

#passo2: abrir a base de dados
#tabela = pandas.read_csv(r'C:\Users\Ramon.Telles\Downloads\produtos.csv')
#print(tabela)

#passo3: cadastrar produto
for linha in tabela.index:

    #codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')      
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')