from pywinauto import application
from pywinauto import Desktop # or backend="win32" by default
import time
import pyautogui

top_windows = Desktop(backend="uia").windows()
janelas_ativas = []

timeout = 30
timeout_start = time.time()

def verificar_janelas():
    janelas_ativas.clear()
    for w in top_windows:
        janelas_ativas.append(w.window_text())

cod_empresa = '0004'

def abrir_fortes():
    verificar_janelas()
    fortes = list(filter(lambda value : value.find('Setor Pessoal') != -1, janelas_ativas))
    
    app = application.Application()

    '''win32_element_info.HwndElementInfo - 'Fortes AC - Setor Pessoal', TApplication'''
    if len(fortes) == 0 or fortes[0] not in janelas_ativas:
        app.start(f'C:\Fortes\AC\AC.exe')
        # Espera a janela principal do aplicativo ficar disponível
        while not app.window(title='Logon').exists():
            time.sleep(1)
    # Conecta-se à janela principal do aplicativo
        janela_principal = app.window(title='Logon')
        janela_principal.wait('ready', timeout=30)
        pyautogui.write('AUTOMACAO')
        pyautogui.press('enter')
        pyautogui.write('automacao')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.write(cod_empresa)
        pyautogui.press('enter')
        pyautogui.press('F9')
        janela_principal = app.window(title='Fortes AC - Setor Pessoal')
        janela_principal.wait('ready', timeout=30)
    else:
        try:
            app.connect(title_re='Fortes AC - Setor Pessoal')
            janela = app.window(title_re='Fortes AC - Setor Pessoal')
            janela.set_focus()
        except application.ProcessNotFoundError:
            print('ProcessNotFoundError has been raised. OK.')