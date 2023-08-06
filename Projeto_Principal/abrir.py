from pywinauto import application, findwindows, timings
from pywinauto import Desktop # or backend="win32" by default
import time
import pyautogui

timings.Timings.window_find_timeout = 10
timings.Timings.window_activate_timeout = 10
timings.Timings.wait_for_idle_timeout = 10

top_windows = Desktop().windows()
janelas_ativas = []

def verificar_janelas():
    janelas_ativas.clear()
    for w in top_windows:
        janelas_ativas.append(w.window_text())

cod_empresa = '0004'
verificar_janelas()
fortes = list(filter(lambda value : value.find('Setor Pessoal') != -1, janelas_ativas))

nome_do_aplicativo = 'AC.exe'
app = application.Application()
bostaliquida = findwindows.find_element(best_match='Fortes AC - Setor Pessoal')
print(bostaliquida)

'''win32_element_info.HwndElementInfo - 'Fortes AC - Setor Pessoal', TApplication'''
if len(fortes) == 0 or fortes[0] not in janelas_ativas:
    app.start(f'C:\Fortes\AC\AC.exe')
    # Espera a janela principal do aplicativo ficar disponível
    while not app.window(title='Logon').exists():
        time.sleep(1)
# Conecta-se à janela principal do aplicativo
    janela_principal = app.window(title='Logon')
    janela_principal.wait('ready', timeout=30)
else:
    try:
        coneccao = app.connect(title_re='Fortes AC - Setor Pessoal')
        janela = app.window(title_re='Fortes AC - Setor Pessoal')
        janela_info =  janela.wrapper_object()
        janela_info.set_focus()
    except application.ProcessNotFoundError:
        print('ProcessNotFoundError has been raised. OK.')

pyautogui.write('AUTOMACAO')
pyautogui.press('enter')
pyautogui.write('automacao')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.write(cod_empresa)
pyautogui.press('enter')
pyautogui.press('F9')

if ("Criar Folha de Pagamento" in janelas_ativas):
    print('Está aqui')
    print(janelas_ativas.index('Criar Folha de Pagamento'))
else:
    print('não está')