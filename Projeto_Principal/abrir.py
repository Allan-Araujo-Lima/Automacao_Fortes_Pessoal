from pywinauto import application, findwindows
import time
import pyautogui

cod_empresa = '0004'

nome_do_aplicativo = 'AC.exe'
app = application.Application()
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

setor_pessoal_window = None
for handle in findwindows.find_windows():
    window = app.window(handle=handle)
    title = window.window_text()
    if 'Setor Pessoal' in title:
        setor_pessoal_window = window
        break