"""Versão 1.0

• Criar uma tela de cadastro de informações do álbum. As seguintes
informações são necessárias: nome do álbum, ano de lançamento,
nome da banda/artista, álbum lançamento do artista (sim/não);
• Criar uma tela que liste todos os álbuns cadastrados na sua base de
dados.
"""



from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox






#listar álbuns
def listar_albuns():
    nome_album = inputNome_Album.get()
    ano_lancamento = inputAno_lancamento.get()
    nome_banda = inputNome_banda.get()
    lancamento_arista = ComboboxAlbum_lancamento.get()

    with open("albuns_cadastrados.txt","a",encoding='utf 8') as arquivo:
        arquivo.write(f"{nome_album},{ano_lancamento},{nome_banda},{lancamento_arista}\n")


    messagebox.showinfo(title="Sucesso", message="Álbum cadastrado com sucesso!")



#validar os dados do álbum
def validar_dados():
    booleano = True
    nome_album = inputNome_Album.get()
    ano_lancamento = inputAno_lancamento.get()
    nome_banda = inputNome_banda.get()
    lancamento_arista = ComboboxAlbum_lancamento.get()
    if nome_album.strip() == "":
        messagebox.showerror(title="Erro", message="Digite o nome do álbum!")
        booleano = False
    elif ano_lancamento.strip() == "" or ano_lancamento.isnumeric() == False:
        messagebox.showerror(title="Erro", message="Digite um número!")
        booleano = False
    elif nome_banda.strip() == "" or nome_banda == " ":
        messagebox.showerror(title="Erro", message="Digite um nome!")
        booleano = False
    elif lancamento_arista.strip() == "":
        messagebox.showerror(title="Erro", message="Selecione se e ou não álbum lançamento do artista!")
        booleano = False
    if booleano == True:
        listar_albuns()


#listar os álbuns em outra tela
def mostrar_albums():
    windowTwo = Toplevel()
    windowTwo.title("Álbuns cadastrados!")
    windowTwo.geometry("1000x500")


    scrollbar = Scrollbar(windowTwo)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(windowTwo, yscrollcommand=scrollbar.set)
    listbox.pack(fill=BOTH, expand=True)

    scrollbar.config(command=listbox.yview)


    with open("albuns_cadastrados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo.readlines():
            album = linha.split(",")
            listbox.insert(END, f"Nome do álbum: {album[0]}, Ano de lançamento do álbum: {album[1]}, Nome da banda/artista: {album[2]}, Álbum lançamento do artista: {album[3]}")

            
    windowTwo.update_idletasks()



window = Tk()
window.title("Sistema de Cadastro de Álbuns")
window.geometry("600x300")


#nome do album
lblNome_Album = Label(window, text="nome do álbum:")
lblNome_Album.pack()
inputNome_Album = Entry(window, text="nome do álbum",bd=2)
inputNome_Album.pack()

#ano de lançamento
lblAno_lancamento = Label(window, text="ano de lançamento:")
lblAno_lancamento.pack()
inputAno_lancamento = Entry(window, bd=2)
inputAno_lancamento.pack()



#nome da banda/artista
lblNome_banda = Label(window, text="nome da banda/artista:")
lblNome_banda.pack()
inputNome_banda = Entry(window, text="nome da banda/artista", bd=2)
inputNome_banda.pack()


#álbum lançamento do artista (sim/não)
valores = ("Sim","Não")
lblAlbum_lancamento = Label(window,text="álbum lançamento do artista")
lblAlbum_lancamento.pack()
ComboboxAlbum_lancamento = Combobox(window,values=valores)
ComboboxAlbum_lancamento.pack()



#botao de cadastro de album
btn = Button(window, text="Cadastrar álbum", command=validar_dados)
btn.pack()

#botao de listagem de album
btn2 = Button(window,text="Listar todos os álbus cadastrados!",command=mostrar_albums)
btn2.pack()






window.mainloop()