import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect('Projeto_Principal\Banco.db')
cursor = connection.cursor()
cod_e_nomeempresa = {}
bala = 0

# Janela em que o usuário cadastra a nova empresa
def tela_empresa():
    botaotela = tk.Toplevel()
    botaotela.title('Adicionar empresa')
    botaotela.geometry('600x400+300+200')
    botaotela.resizable(False, False)
    botaotela.configure(bg='#e7a855')
    
    titulobotaotela = tk.Label(botaotela, text='Cadastrar nova empresa', font='Calibre 16 bold', bg='#e7a855', fg='white')
    titulobotaotela.pack()    
    
    codigol = tk.Label(botaotela, text='Código', font='Calibre 12', fg='white', bg='#e7a855')
    codigol.pack()
    
    codigoe = tk.Entry(botaotela, width=7, font='Calibre 8')
    codigoe.pack()
    
    nomeempresal = tk.Label(botaotela, text='Nome', font='Calibre 12', fg='white', bg='#e7a855')
    nomeempresal.pack()

    nomeempresae = tk.Entry(botaotela, width=54, font='Calibre 8')
    nomeempresae.pack()
    
    def pegar_valores():
        cod_empresa = codigoe.get()
        nome_empresa = nomeempresae.get()
        cod_e_nomeempresa[cod_empresa] = nome_empresa
        cursor.execute("INSERT INTO Empresas (Codigo_Fortes, Empresa) VALUES ({cod}, '{name}')".format(cod = cod_empresa, name = nome_empresa))
        connection.commit()
        botaotela.destroy()
    
    adicionarempresa = tk.Button(botaotela, text='Adicionar Empresa', command=pegar_valores)
    adicionarempresa.pack()
    
    cancelar_adicionar_empresa = tk.Button(botaotela, text='Cancelar', command=botaotela.destroy)
    cancelar_adicionar_empresa.pack()

def exibir_empresas():
    janela_empresas = tk.Toplevel()
    janela_empresas.title('Empresas')
    janela_empresas.geometry('500x300+300+200')
    janela_empresas.resizable(False, False)
    janela_empresas.configure(bg='#e7a855')

    lista_empresas = tk.Listbox(janela_empresas, width=50)
    lista_empresas.pack()
        
    #vaiável que seleciona todos os dados do banco de dados
    x = cursor.execute("SELECT * from Empresas")
    for i in x:
        lista_empresas.insert(tk.END, f'Código: {i[1]}, Nome: {i[2]}')

def config():
    configuracao = tk.Toplevel()
    configuracao.title('Configurações')
    configuracao.grab_set()
    
inicio = tk.Tk()
inicio.title('Automação de Folha')
inicio.geometry('1080x720+300+200')
inicio.minsize(600, 600)
inicio.configure(bg='#e7a855')

titulo = tk.Label(inicio, text='Automação de Folha', font='Calibri 25 bold', bg='#e7a855', fg='white')
titulo.pack()

botao = tk.Button(inicio, text='Adicionar Nova Empresa', command=tela_empresa)
botao.pack()

exibiradd = tk.Button(inicio, text='Empresas', command=exibir_empresas)
exibiradd.pack()

min_w = 70  # Largura mínima do frame
max_w = 300  # Largura máxima do frame
cur_width = min_w  # Largura atual do frame
expanded = False  # Verifica se o frame está completamente expandido

def expandir():
    global cur_width, expanded
    cur_width += 10
    frame.config(width=cur_width)
    if cur_width >= max_w:
        expanded = True
        fill()

def contrair():
    global cur_width, expanded
    cur_width -= 10
    frame.config(width=cur_width)
    if cur_width <= min_w:
        expanded = False
        fill()

def fill():
    if expanded:
        home_b.config(text='Home', image='', font=(0, 21))
        set_b.config(text='Settings', image='', font=(0, 21))
    else:
        home_b.config(image=home, font=(0, 21))
        set_b.config(image=settings, font=(0, 21))

home = ImageTk.PhotoImage(Image.open('Projeto_Principal\Imagens\home.png').resize((40, 40)))
settings = ImageTk.PhotoImage(Image.open('Projeto_Principal\Imagens\config.png').resize((40, 40)))

inicio.update()
frame = tk.Frame(inicio, bg='white', width=50, height=inicio.winfo_height(), borderwidth=1)

home_b = tk.Button(frame, image=home, bg='white', relief='flat')
set_b = tk.Button(frame, image=settings, bg='white', relief='flat', command=config)

frame.place(x=0, y=0, anchor='nw')  # Posiciona o frame no topo esquerdo
frame.grid_rowconfigure(0, weight=1)  # Permite o preenchimento vertical dos itens
frame.grid_columnconfigure(0, weight=1)  # Permite o preenchimento horizontal dos itens

home_b.grid(row=0, column=0, pady=10)  # Centraliza o botão Home verticalmente
set_b.grid(row=1, column=0, pady=15)  # Centraliza o botão Settings verticalmente

inicio.mainloop()