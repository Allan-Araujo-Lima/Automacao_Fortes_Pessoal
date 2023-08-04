from ast import Num, Return
from enum import auto
from itertools import count
from numbers import Integral, Number
import numbers
from tracemalloc import stop
from turtle import back, pu
from unicodedata import numeric
from xmlrpc.client import Boolean, boolean
from cv2 import integral, line, repeat
from numpy import character, int0, intp, number
from ast import Not
from types import NoneType
import pyautogui
import time
import pyperclip
from tomlkit import integer
import calendar
from datetime import datetime

'''time.sleep can chance in diferents computer and/or in diferents campanys.'''

competencia = pyautogui.prompt('Qual a competência da folha de pagamento?', default='mmaaaa', title='Informe a competência.')
contagem = len(competencia)
while (contagem != 6 or int(competencia) < 11950 or int(competencia) > 132999): #verifica se a competência é válida.
    pyautogui.alert('Competência inválida!')
    competencia = pyautogui.prompt('Qual a competência da folha de pagamento?', default='mmaaaa', title='Informe a competência.')
    contagem = len(competencia)
competenciames = int(competencia[0:2]) #mês da competência
competenciaano = int(competencia[2:6]) #ano da competência
lastday = calendar.monthrange(competenciaano, competenciames)[1] #localiza o ultimo dia da semana
confirmation = pyautogui.confirm(text='Deseja Criar a folha da {}?'.format(competencia), title='Confirmação de execução.') #confirma se o código será executado.
if (confirmation == 'OK'):
    pyautogui.alert('O código vai iniciar, não mexa no computador.', title='Alerta')
else: exit(pyautogui.alert('O código foi encerrado'))
pyautogui.PAUSE = (0.05)
competencia = int(competencia)
provisaoi = int(competencia - 1)    
provisaof = int(competencia - 10000)
provisao13 = '01' + str(competenciaano)
if (provisaoi < 100000):
    provisaoi = '0' + str(provisaoi)
else: provisaoi = str(provisaoi)
if (provisaof < 100000):
    provisaof = '0' + str(provisaof)
else: provisaof = str(provisaof)
if (competencia < 100000):
        competencia ='0' + str(competencia)
else: competencia = str(competencia)
relatorios = pyautogui.confirm('Deseja salvar os relatórios da folha?', title='Salvar relatórios', buttons=['SIM', 'NAO'])
if (relatorios == 'SIM'):
    diretorio = pyperclip.copy(pyautogui.prompt('Em qual diretório devo salvar?', title='Diretório'))
    pyautogui.alert('Os relatórios serão salvos.', title='Alerta')
time.sleep(1)
pyautogui.hotkey('alt', 'tab') #troca para o fortes

# '''Folha de Pagamento'''

# pyautogui.hotkey('ctrl', 'l')
# pyautogui.write('folha de pagamento')
# pyautogui.press('down')
# pyautogui.press('down')
# time.sleep(0.25)
# pyautogui.press('enter')
# time.sleep(0.75)
# pyautogui.press('enter')
# time.sleep(0.5)
# pyautogui.write(competencia)
# for x in range (13):
#     pyautogui.press('enter')
#     time.sleep(0.25)
# time.sleep(5)
# pyautogui.press('enter')
# for x in range(4):
#     pyautogui.press('esc')
#     time.sleep(0.5)
# time.sleep(1)

# '''GPS'''

# pyautogui.hotkey('ctrl', 'l')
# pyautogui.write('gps')
# time.sleep(0.25)
# pyautogui.press('enter')
# time.sleep(0.75)
# pyautogui.press('f2')
# time.sleep(0.5)
# pyautogui.write(competencia)
# pyautogui.press('tab')
# pyautogui.press('pgdn')
# pyautogui.press('enter')
# time.sleep(0.5)
# for x in range(3):
#     pyautogui.press('enter')
# pyautogui.press('f9')
# time.sleep(0.5)
# encerrargps = pyautogui.locateOnScreen('encerrargps.png')
# clicarencerrargps = pyautogui.center(encerrargps)
# time.sleep(0.25)
# pyautogui.click(clicarencerrargps)
# time.sleep(0.25)
# for x in range(2):
#     pyautogui.press('enter')
#     time.sleep(0.25)
# for x in range(4):
#     pyautogui.press('esc')
#     time.sleep(0.25)
# time.sleep(1)

# '''Provisão de férias'''

# pyautogui.hotkey('ctrl', 'l')
# pyautogui.write('provisao de ferias')
# time.sleep(0.75)
# pyautogui.press('down')
# pyautogui.press('down')
# time.sleep(0.5)
# pyautogui.press('enter')
# time.sleep(0.5)
# pyautogui.write(competencia)
# pyautogui.press('enter')
# pyautogui.write('1')
# pyautogui.press('enter')
# pyautogui.press('pgdn')
# pyautogui.press('enter')
# pyautogui.press('space')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.write(provisaoi)
# pyautogui.press('tab')
# pyautogui.write(provisaof)
# for x in range(13):
#     pyautogui.press('enter')
#     time.sleep(0.5)
# time.sleep(1)
# for x in range(4):
#     pyautogui.press('esc')
#     time.sleep(0.5)
# time.sleep(1)

# '''Provisão de 13° salário'''

# pyautogui.hotkey('ctrl', 'l')
# pyautogui.write('provisao de 13')
# time.sleep(0.75)
# pyautogui.press('down')
# pyautogui.press('down')
# pyautogui.press('enter')
# time.sleep(0.5)
# pyautogui.write(competencia)
# pyautogui.press('enter')
# pyautogui.write('1')
# pyautogui.press('enter')
# pyautogui.press('pgdn')
# pyautogui.press('enter')
# pyautogui.press('space')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.write(provisao13)
# pyautogui.press('tab')
# pyautogui.write(provisaof)
# for x in range(13):
#     pyautogui.press('enter')
#     time.sleep(0.5)
# time.sleep(1)
# for x in range(4):
#     pyautogui.press('esc')
#     time.sleep(0.5)
# time.sleep(1)

# if (relatorios == 'NAO'): exit(pyautogui.alert('O processo terminou', title='Obrigado'))
    
'''Salvar Relatórios'''
'''listagem de pagameto'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('folha listagem de pagamento')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write(competencia)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('pgdn')
pyautogui.press('enter')
for x in range(4):
    pyautogui.press('enter')
    time.sleep(0.25)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(1.0)
pyautogui.hotkey('alt', 's')
time.sleep(0.5)
pyautogui.write('documento')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.write("/1. Folha de Pagamento.pdf")
time.sleep(0.75)
pyautogui.press('enter')
for x in range(5):
    pyautogui.press('esc')
    time.sleep(0.25)

'''recibo de pagamento'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('folha recibo')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write(competencia)
pyautogui.press('enter')
pyautogui.write('1')
pyautogui.press('enter')
pyautogui.press('pgdn')
for x in range(8):
    pyautogui.press('enter')
    time.sleep(0.15)
time.sleep(2)
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('alt', 's')
time.sleep(0.5)
pyautogui.write('documento')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.write("/1.1 Recibo de Pagamento.pdf")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
for x in range(5):
    pyautogui.press('esc')
    time.sleep(0.25)

'''Listagem de autonomos'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('listagem de autonomos')
pyautogui.press('enter')
pyautogui.write('01' + competencia)
pyautogui.press('tab')
pyautogui.write(str(lastday))
pyautogui.press('tab')
pyautogui.write(competencia)
pyautogui.press('enter')
pyautogui.write('Data de Pagamento - Nome')
for x in range(7):
    pyautogui.press('enter')
    time.sleep(0.15)
time.sleep(1)
autonomos = pyautogui.locateOnScreen('autonomos.png', confidence=0.25)
if (autonomos is None):
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write("/1.2 Listagem de Autônomos.pdf")
    time.sleep(0.75)
    pyautogui.press('enter')
    time.sleep(1)
for x in range (6):
    pyautogui.press('esc')
    time.sleep(0.15)
        
'''Resumo geral do periodo'''

pyautogui.hotkey('ctrl', 'l')
time.sleep(0.5)
pyautogui.write('resumo geral')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write(competencia)
pyautogui.press('tab')  
pyautogui.write(competencia)
pyautogui.press('tab')
pyautogui.press('pgdn')
for x in range(4):
    pyautogui.press('enter')
time.sleep(0.50)
pyautogui.hotkey('alt', 's')
pyautogui.write('documento')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
if (autonomos is None):
    pyautogui.write("/1.3 Resumo Geral do Periodo.pdf")
    time.sleep(0.75)
    pyautogui.press('enter')
else:
    pyautogui.write("/1.2 Resumo Geral do Periodo.pdf")
    time.sleep(0.75)
    pyautogui.press('enter')
time.sleep(1.5)
for x in range (6):
    pyautogui.press('esc')
    time.sleep(0.20)

'''GPS Analitica'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('gps ana')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.write(competencia)
pyautogui.press('enter')
pyautogui.press('pgdn')
pyautogui.press('enter')
pyautogui.press('tab')
detalhar = pyautogui.locateOnScreen('detalharsemflag.png')
if (detalhar is not None):
    pyautogui.press('tab')
    pyautogui.press('space')
else:
    pyautogui.press('tab')
demons = pyautogui.locateOnScreen('demonstrativosemflag.png')    
if (demons is not None):
    pyautogui.press('tab')
    pyautogui.press('space')
else:
    pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(0.50)
pyautogui.hotkey('alt', 's')
pyautogui.write('documento')
pyautogui.press('tab')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.write('/2. GPS Analítica.pdf')
time.sleep(0.75)
pyautogui.press('enter')
for x in range(7):
    pyautogui.press('esc')
    time.sleep(0.25)
time.sleep(1.5)

'''darf irrf'''

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('darf i')
pyautogui.press('enter')
pyautogui.write('01' + competencia)
pyautogui.press('enter')
pyautogui.write(str(lastday))
time.sleep(0.5)
for x in range(3):
    pyautogui.press('enter')
    time.sleep(0.15)
darfzerado = pyautogui.locateOnScreen('darfzerado.png')
if (darfzerado is None):
    for x in range(2):
        pyautogui.press('enter')
        time.sleep(0.15)
    time.sleep(0.50)
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write('/4. DARF IRRF.pdf')
    time.sleep(0.75)
    pyautogui.press('enter')
    for x in range(5):
        pyautogui.press('esc')
        time.sleep(0.25)
else:
    for x in range(4):
        pyautogui.press('esc')
        time.sleep(0.25)

'''Férias previstas'''

time.sleep(0.5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('previsao re')
pyautogui.press('enter')
pyautogui.write(str(lastday))
pyautogui.press('enter')
pyautogui.write('11')
pyautogui.press('enter')
pyautogui.press('pgdn')
for x in range(7):
    pyautogui.press('enter')
    time.sleep(0.20)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('right')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('left')
pyautogui.press('enter')
time.sleep(1)
if (darfzerado is None):
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write('/5. Férias Previstas.pdf')
    time.sleep(0.25)
    pyautogui.press('enter')
else:
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.write('/4. Férias Previstas.pdf')
    time.sleep(0.75)
    pyautogui.press('enter' )
for x in range (7):
    pyautogui.press('esc')
    time.sleep(0.15)
    
'''listagem de férias'''

time.sleep(0.5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('listagem ferias')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write('01' + competencia)
pyautogui.press('enter')
pyautogui.write(str(lastday))
pyautogui.press('enter')
pyautogui.press('pgdn')
for x in range (6):
    pyautogui.press('enter')
    time.sleep(0.15)
totalgeral = pyautogui.locateOnScreen('totalgeral.png')
time.sleep(0.5)
if (totalgeral is None):
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    if (darfzerado is None):
        pyautogui.write("/5.1 Listagem de Férias.pdf")
        time.sleep(0.25)
        pyautogui.press('enter')
    else:
        pyautogui.write("/4.1 Listagem de Férias.pdf")
        time.sleep(0.25)
        pyautogui.press('enter') 
time.sleep(1)
for x in range (6):
    pyautogui.press('esc')
    time.sleep(0.15)
    
'''listagem de rescisão'''

time.sleep(0.5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('rescisao listagem')
pyautogui.press('enter')
pyautogui.write('01' + competencia)
pyautogui.press('tab')
pyautogui.write(str(lastday))
pyautogui.press('tab')
pyautogui.press('pgdn')
for x in range(6):
    pyautogui.press('enter')
    time.sleep(0.15)
totalgeral2 = pyautogui.locateOnScreen('totalgeral2.png')
time.sleep(0.5)
if (totalgeral2 is None):
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    if (darfzerado is None):
        if (totalgeral is None):
            pyautogui.write('/5.2 Listagem de Rescisão.pdf')
        else:
            pyautogui.write('/5.1 Listagem de Rescisão.pdf')
    else:
        if (totalgeral is None):
            pyautogui.write('/4.2 Listagem de Rescisão.pdf')
        else:
            pyautogui.write('/4.1 Listagem de Rescisão.pdf')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
for x in range(6):
    pyautogui.press('esc')
    time.sleep(0.15)
    
'''listagem de periodo de experiência'''

time.sleep(0.5)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('periodo de expe')
pyautogui.press('enter')
pyautogui.write('01' + competencia)
pyautogui.press('enter')
pyautogui.write(str(lastday))
pyautogui.press('enter')
pyautogui.press('pgdn')
for x in range(4):
    pyautogui.press('enter')
experiencia = pyautogui.locateOnScreen('periododeexp.png')
time.sleep(0.5)
if (experiencia is None):
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    if (darfzerado is None):
        if (totalgeral is None):
            if (totalgeral2 is None):
                pyautogui.write('/5.3 Periodo de Experiência.pdf')
            else:
                pyautogui.write('/5.2 Periodo de Experiência.pdf')
        else:
            pyautogui.write('/5.1 Periodo de Experiência.pdf')
    else:
        if (totalgeral is None):
            if (totalgeral2 is None):
                pyautogui.write('/4.3 Periodo de Experiência.pdf')
            else:
                pyautogui.write('/4.2 Periodo de Experiência.pdf')
        else:
            pyautogui.write('/4.1 Periodo de Experiência.pdf')  
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
for x in range(5):
    pyautogui.press('esc')

'''provisão de férias'''
def pro():
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('obrigacoes ferias pro')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.write(str(lastday))
    pyautogui.press('enter')
    pyautogui.press('pgdn')
    for x in range(9):
        pyautogui.press('enter')
        time.sleep(0.15)
    time.sleep(0.5)
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    if (darfzerado is None):
        pyautogui.write('/6. Provisao de Férias.pdf')
    else:
        pyautogui.write('/5. Provisao de Ferias.pdf')
    pyautogui.press('enter')
    for x in range(5):
        pyautogui.press('esc')
        time.sleep(0.5)

pyautogui.alert('O processo terminou', title='Obrigado')