import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect('Projeto_Principal\Banco.db')
cursor = connection.cursor()
cod_e_nomeempresa = {}
bala = 0
CorTema = '#e7a855'

# Janela em que o usuário cadastra a nova empresa
def tela_empresa():
    botaotela = tk.Toplevel()
    botaotela.title('Adicionar empresa')
    botaotela.geometry('530x130+300+200')
    botaotela.resizable(False, False)
    botaotela.configure(bg='#e7a855')
    
    titulobotaotela = tk.Label(botaotela, text='Cadastrar nova empresa', font='Calibre 16 bold', bg=CorTema, fg='white')
    titulobotaotela.pack()    
    
    codigol = tk.Label(botaotela, text='Código', font='Calibre 12', fg='white', bg=CorTema)
    codigol.pack()
    codigol.place(x=15, y=50, anchor='w')  
    
    def validate(P):
        if len(P) <= 4 and P.isdigit():
            # Entry with 4 digit is ok
            return True
        else:
            # Anything else, reject it
            return False
    vcmd = (botaotela.register(validate), '%P')
    
    codigoe = tk.Entry(botaotela, width=7, font='Calibre 8', validate='key', validatecommand=vcmd)
    codigoe.pack()
    codigoe.place(x=75, y=50, anchor='w')
    
    nomeempresal = tk.Label(botaotela, text='Nome', font='Calibre 12', fg='white', bg=CorTema)
    nomeempresal.pack()
    nomeempresal.place(x=130, y=50, anchor='w')

    nomeempresae = tk.Entry(botaotela, width=54, font='Calibre 8')
    nomeempresae.pack()
    nomeempresae.place(x=185, y=50, anchor='w')
    
    codigoEstabelecimentol = tk.Label(botaotela, text='Código Estabelecimento', font='Calibre 12', fg='white', bg=CorTema)
    codigoEstabelecimentol.pack()
    codigoEstabelecimentol.place(x=15, y=80, anchor='w')
    
    codigoEstabelecimentoe = tk.Entry(botaotela, width=5, font='Calibre 8', validate='key', validatecommand=vcmd)
    codigoEstabelecimentoe.pack()
    codigoEstabelecimentoe.place(x=195, y=80, anchor='w')
    
    nomeEstabelecimentol = tk.Label(botaotela, text='Estabelecimento', font='Calibre 12', fg='white', bg=CorTema)
    nomeEstabelecimentol.pack()
    nomeEstabelecimentol.place(x=235, y=80, anchor='w')
    
    nomeEstabelecimentoe = tk.Entry(botaotela, width=24, font='Calibre 8')
    nomeEstabelecimentoe.pack()
    nomeEstabelecimentoe.place(x=363, y=80, anchor='w')
    
    def pegar_valores():
        cod_empresa = codigoe.get()
        nome_empresa = nomeempresae.get()
        cod_estabelecimento = codigoEstabelecimentoe.get()
        nome_estabelecimento = nomeEstabelecimentoe.get()
        cod_e_nomeempresa[cod_empresa] = nome_empresa
        try:
            cursor.execute("INSERT INTO Empresas (Codigo_Fortes, Empresa) VALUES ({cod}, '{name}')".format(cod = cod_empresa, name = nome_empresa))
            nome_empresa_bd = cursor.execute("SELECT Id FROM Empresas WHERE Empresa='{nome_empresa}'".format(nome_empresa = nome_empresa))
            cursor.execute("INSERT INTO Estabelecimentos (Codigo, Nome, Empresa_Id) VALUES (0002, 'filfi1', 8)")
            connection.commit()
        except Exception as error:
            print(error, 'aaaaa')
        botaotela.destroy()
    
    adicionarempresa = tk.Button(botaotela, text='Adicionar Empresa', width=15, command=pegar_valores)
    adicionarempresa.pack()
    adicionarempresa.place(x=100, y=110, anchor='center')
    
    cancelar_adicionar_empresa = tk.Button(botaotela, text='Cancelar', width=15, command=botaotela.destroy)
    cancelar_adicionar_empresa.pack()
    cancelar_adicionar_empresa.place(x=430, y=110, anchor='center')

def exibir_empresas():
    janela_empresas = tk.Toplevel()
    janela_empresas.title('Empresas')
    janela_empresas.geometry('500x300+300+200')
    janela_empresas.resizable(False, False)
    janela_empresas.configure(bg=CorTema)

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
inicio.configure(bg=CorTema)

titulo = tk.Label(inicio, text='Automação de Folha', font='Calibri 25 bold', bg=CorTema, fg='white')
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