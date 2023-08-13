import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('Criar Folha de Pagamento')
pyautogui.press('enter')

janelas_ativas = []
timer = 0

while 'Criar Folha de Pagamento' not in janelas_ativas:
    janelas_ativas.clear()
    for x in pyautogui.getAllWindows():
        janelas_ativas.append(x.title)
    time.sleep(1)
    timer += 1
    if timer == 12:
        print('é isso')
        break

print('Passou do loop')