import pyautogui
import time
import calendar
from datetime import datetime
import abrir
from pywinauto import application

coneccao = application.Application(backend='uia')

#variaveis
fortes_janelas = []
agora = time.time()
timeout = 60

def checar_janelas():
    fortes_janelas.clear()
    for x in pyautogui.getAllWindows():
        fortes_janelas.append(x.title)   

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
    diretorio = pyautogui.prompt('Em qual diretório devo salvar?', title='Diretório')
    pyautogui.alert('Os relatórios serão salvos.', title='Alerta')
time.sleep(1)

'''Folha de Pagamento'''
def criar_folha():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('folha de pagamento criar')
    pyautogui.press('enter')
    agora = time.time()
    while 'Criar Folha de Pagamento' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(competencia)
    time.sleep(5)
    agora = time.time()
    while True:
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        checar_janelas()
        if 'Confirmação' in fortes_janelas:
            pyautogui.press('enter')
            break
        else:
            pyautogui.press('enter')
        time.sleep(1)
    agora = time.time()
    time.sleep(5)
    while 'Informação' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        time.sleep(1) 
    pyautogui.press('enter')
    time.sleep(5)
    checar_janelas()
    if 'Confirmação' in fortes_janelas:
        pyautogui.press('esc')
        pyautogui.press('alt')
        
'''GPS'''
def criar_gps():
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('gps')
    time.sleep(0.25)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('f2')
    time.sleep(1)
    pyautogui.write(competencia)
    pyautogui.press('tab')
    pyautogui.press('pgdn')
    pyautogui.press('enter')
    time.sleep(0.5)
    for x in range(5):
        pyautogui.press('enter')
        time.sleep(5)
        checar_janelas()
        if 'Atenção!' in fortes_janelas:
            exit(pyautogui.alert(f'O processo Falhou. A GPS da competência {competencia[0:2]}/{competencia[2:6]} já está criada.', title='Obrigado'))
    pyautogui.press('f9')
    time.sleep(3)
    for x in range(2):
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(5)
    agora = time.time()
    while 'Confirmação' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado')) 
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'r')

'''Provisão de férias'''
def criar_provisao_ferias():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('criar provisao ferias')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    agora = time.time()
    while 'Criar Provisão de Férias' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        time.sleep(1)
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter')
    time.sleep(5)
    checar_janelas()
    if 'Atenção!' in fortes_janelas:
        exit(pyautogui.alert(f'O processo Falhou. A Privisão de Férias da competência {competencia[0:2]}/{competencia[2:6]} já está criada.', title='Obrigado'))
    pyautogui.press('pgdn')
    pyautogui.press('enter')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(provisaoi)
    pyautogui.press('tab')
    pyautogui.write(provisaof)
    agora = time.time()
    while True:
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        checar_janelas()
        if 'Confirmação' in fortes_janelas:
            pyautogui.press('enter')
            break
        else:
            pyautogui.press('enter')
        time.sleep(1)
    agora = time.time()
    time.sleep(5)
    while 'Informação' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
    pyautogui.press('enter')
    pyautogui.press('alt')
    time.sleep(1)
    
'''Provisão de 13° salário'''
def criar_provisao_13():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('criar provisao 13')
    pyautogui.press('enter')
    time.sleep(1)
    agora = time.time()
    while 'Criar Provisão de 13º Salário' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter')
    time.sleep(5)
    checar_janelas()
    if 'Atenção!' in fortes_janelas:
        exit(pyautogui.alert(f'O processo Falhou. A Privisão de Férias da competência {competencia[0:2]}/{competencia[2:6]} já está criada.', title='Obrigado'))
    pyautogui.press('pgdn')
    pyautogui.press('enter')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(provisao13)
    pyautogui.press('tab')
    pyautogui.write(provisaof)
    while True:
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
        checar_janelas()
        if 'Confirmação' in fortes_janelas:
            pyautogui.press('enter')
            break
        else:
            pyautogui.press('enter')
        time.sleep(1)
    agora = time.time()
    time.sleep(5)
    while 'Informação' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
    pyautogui.press('enter')
    pyautogui.press('alt')
    time.sleep(1)

abrir.abrir_fortes()
criar_folha()
criar_gps()
criar_provisao_ferias()
criar_provisao_13()

if (relatorios == 'NAO'): exit(pyautogui.alert('O processo terminou', title='Obrigado'))
    
'''Salvar Relatórios'''
'''listagem de pagameto'''
def salvar_folha():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('folha listagem de pagamento')
    pyautogui.press('enter')
    time.sleep(5)
    agora = time.time()
    while 'Listagem de Pagamento de Folha' not in fortes_janelas:
        checar_janelas()
        if time.time() > agora + timeout:
            exit(pyautogui.alert('O processo falhou', title='Obrigado'))
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('enter')
    pyautogui.write(competencia)
    time.sleep(5)
    if 'Atenção!' in fortes_janelas:
        exit(pyautogui.alert(f'O processo Falhou. A Folha de Pagamento da competência {competencia[0:2]}/{competencia[2:6]} já está criada.', title='Obrigado'))
    
    pyautogui.press('enter')
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
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write("/1. Folha de Pagamento.pdf")
    time.sleep(0.75)
    pyautogui.press('enter')
    time.sleep(1)
    for x in range(5):
        pyautogui.press('esc')
        time.sleep(0.25)

'''recibo de pagamento'''
def salvar_recibos():
    time.sleep(0.5)
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
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write("/1.1 Recibo de Pagamento.pdf")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    for x in range(5):
        pyautogui.press('esc')
        time.sleep(0.25)

'''Listagem de autonomos'''
def salvar_autonomos():
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
    autonomos = pyautogui.locateOnScreen('imagens/autonomos.png', confidence=0.25)
    if (autonomos is None):
        pyautogui.hotkey('alt', 's')
        pyautogui.write('documento')
        pyautogui.press('tab')
        pyautogui.write(diretorio)
        time.sleep(0.5)
        pyautogui.write("/1.2 Listagem de Autônomos.pdf")
        time.sleep(0.75)
        pyautogui.press('enter')
        time.sleep(1)
    for x in range(6):
        pyautogui.press('esc')
        time.sleep(0.25)
        
'''Resumo geral do periodo'''
def salvar_resumo():
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
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write("/1.3 Resumo Geral do Periodo.pdf")
    time.sleep(0.75)
    pyautogui.press('enter')
    time.sleep(1.5)
    for x in range(6):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''GPS Analitica'''

def salvar_gps():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('gps ana')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.press('pgdn')
    pyautogui.press('enter')
    pyautogui.press('tab')
    detalhar = pyautogui.locateOnScreen('imagens/detalharsemflag.png')
    if (detalhar is not None):
        pyautogui.press('tab')
        pyautogui.press('space')
    else:
        pyautogui.press('tab')
    demons = pyautogui.locateOnScreen('imagens/demonstrativosemflag.png')    
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
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write('/2. GPS Analitica.pdf')
    time.sleep(0.75)
    pyautogui.press('enter')
    time.sleep(1)
    for x in range(7):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''darf irrf'''

def salvar_irrf():
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
    darfzerado = pyautogui.locateOnScreen('imagens/darfzerado.png')
    if (darfzerado is None):
        for x in range(2):
            pyautogui.press('enter')
            time.sleep(0.15)
        time.sleep(0.50)
        pyautogui.hotkey('alt', 's')
        pyautogui.write('documento')
        pyautogui.press('tab')
        pyautogui.write(diretorio)
        time.sleep(0.5)
        pyautogui.write('/4. Listagem de IRRF.pdf')
        time.sleep(0.75)
        pyautogui.press('enter')
        for x in range(5):
            pyautogui.press('esc')
            time.sleep(0.25)
    else:
        for x in range(4):
            pyautogui.press('esc')
            time.sleep(0.25)
    time.sleep(1.5)

'''Férias previstas'''

def salvar_ferias_previstas():
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
    pyautogui.write('/5. Ferias Previstas.pdf')
    time.sleep(0.25)
    pyautogui.press('enter')
    for x in range(7):
        pyautogui.press('esc')
        time.sleep(0.25)
    
'''listagem de férias'''

def salvar_listagem_ferias():
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
    totalgeral = pyautogui.locateOnScreen('imagens/totalgeral.png')
    time.sleep(0.5)
    if (totalgeral is None):
        pyautogui.hotkey('alt', 's')
        pyautogui.write('documento')
        pyautogui.press('tab')
        pyautogui.write(diretorio)
        time.sleep(0.5)
        pyautogui.write("/5.1 Listagem de Ferias.pdf")
        time.sleep(0.25)
        pyautogui.press('enter')
    for x in range(6):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)
    
'''listagem de rescisão'''

def salvar_listagem_rescisao():
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
    totalgeral2 = pyautogui.locateOnScreen('imagens/totalgeral2.png')
    time.sleep(0.5)
    if (totalgeral2 is None):
        pyautogui.hotkey('alt', 's')
        pyautogui.write('documento')
        pyautogui.press('tab')
        pyautogui.write(diretorio)
        time.sleep(0.5)
        pyautogui.write('/5.2 Listagem de Rescisão.pdf')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    for x in range(6):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)
    
'''listagem de periodo de experiência'''

def salvar_periodo_experiencia():
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
    experiencia = pyautogui.locateOnScreen('imagens/periododeexp.png')
    time.sleep(0.5)
    if (experiencia is None):
        pyautogui.hotkey('alt', 's')
        pyautogui.write('documento')
        pyautogui.press('tab')
        pyautogui.write(diretorio)
        time.sleep(0.5)
        pyautogui.write('/5.3 Periodo de Experiencia.pdf')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    for x in range(6):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''provisão de férias'''

def salvar_provisao_ferias():
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
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write('/6. Provisao de Ferias.pdf')
    for x in range(7):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''Provisão de 13'''

def salvar_provisao_13():
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('obrigacoes 13 pro')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.write(str(lastday))
    pyautogui.press('enter')
    pyautogui.press('pgdn')
    for x in range(6):
        pyautogui.press('enter')
        time.sleep(0.15)
    time.sleep(0.5)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 's')
    pyautogui.write('documento')
    pyautogui.press('tab')
    pyautogui.write(diretorio)
    time.sleep(0.5)
    pyautogui.write('/6.1 Provisao de 13° Salario.pdf')
    pyautogui.press('enter')
    time.sleep(1)
    for x in range(7):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''GFIP'''
def salvar_gfip():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('gfip')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(competencia)
    pyautogui.press('enter')
    pyautogui.write('115')
    pyautogui.press('enter')
    pyautogui.write('recolh')
    for x in range(15):
        pyautogui.press('enter')
        time.sleep(0.25)
    pyautogui.write(diretorio)
    for x in range(3):
        pyautogui.press('enter')
        time.sleep(1.5)
    for x in range(2):
        pyautogui.press('esc')
        time.sleep(0.25)
    time.sleep(1.5)

'''FGTS'''

'''eSocial'''

pyautogui.alert('O processo terminou', title='Obrigado')