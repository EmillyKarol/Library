from tkinter import *

root = Tk()

class Biblioteca():
    def __init__(self):
        self.root = root
        self.janela()
        self.frames()
        self.widgets()
        self.registro_membros = []
        self.catalogo_livros = []
        root.mainloop()

    def janela(self):
        self.root.title('Biblioteca')
        self.root.config(bg='#4e4278')
        self.root.geometry('650x450')
        self.root.resizable(True,True)
        self.root.maxsize(width=800,height=600)
        self.root.minsize(width=600,height=400)

    def frames(self):
        self.frame_1 = Frame(self.root,bg='#ebebeb')
        self.frame_1.place(relx=0.02,rely=0.05,relwidth=0.96,relheight=0.45)
        self.frame_2 = Frame(self.root,bg='#ebebeb')
        self.frame_2.place(relx=0.02,rely=0.55,relwidth=0.96,relheight=0.4)

    # Cada id de um livro deve ser único, e como nas outras funções o input do id é nescessário, ficaria dificil fazer um incremento no id automaticamento sem que o usuario o informe. Por isso, o cadastro impede que o usuario cadastre livros com o mesmo id
    def cadastrar_livro(self):
        self.titulo_l = self.titulo_entry.get()
        self.autor_l = self.autor_entry.get()
        self.id_l = self.id_entry.get()

        if self.titulo_l == '' or self.autor_l == '' or self.id_l == '':
            self.var_resultado.set('Erro ao cadastrar novo livro')
            self.mensagem.config(background='indianred1')
        else:
            for livro in self.catalogo_livros:
                if livro.id == self.id_l:
                    self.var_resultado.set('ID existente | Cadastre novo ID')
                    self.mensagem.config(background='indianred1')
                    return

            self.novo_livro = Livro(self.titulo_l, self.autor_l)
            self.novo_livro.id = self.id_l
            self.catalogo_livros.append(self.novo_livro)
            self.var_resultado.set('Livro cadastrado com sucesso')
            self.mensagem.config(background='#99ff99')
            self.titulo_entry.delete(0, 'end')
            self.autor_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            self.titulo_entry.focus()       

    def pesquisar(self):
        self.var_resultado.set("")
        self.mensagem.configure(background="silver")
        print("|||||||||||||| Catálogo de Livros ||||||||||||||")
        for livro in self.catalogo_livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, ID:{livro.id}, Status:{livro.status}")

    # Para fazer o historico de livros emprestados de cada membro, é preciso que quando for emprestar o livro o usuario forneça as informações do membro
    def emprestar(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        id_livro = self.id_entry.get()
        nome_membro = self.nome_entry.get()
        num_membro = self.numero_entry.get()
        
        livro_encontrado = None
        membro_encontrado = None
        
        for membro in self.registro_membros:
            if membro.nome == nome_membro and membro.numero == num_membro:
                membro_encontrado = membro
                break
        if membro_encontrado is None:
            self.var_resultado.set("Erro ao procurar membro")
            self.mensagem.configure(background="indianred1")
            return
        
        for livro in self.catalogo_livros:
            if livro.id == id_livro and livro.titulo == titulo and livro.autor == autor:
                livro_encontrado = livro
                break
            
        if livro_encontrado is None:
            self.var_resultado.set("Erro ao procurar livro")
            self.mensagem.configure(background="indianred1")
        elif livro_encontrado.status == 'Emprestado':
            self.var_resultado.set("Livro não disponível para empréstimo")
            self.mensagem.configure(background="indianred1")
        else:
            membro_encontrado.historico.append(titulo)
            livro_encontrado.status = 'Emprestado'
            self.var_resultado.set("Empréstimo feito com sucesso")
            self.mensagem.configure(background="#99FF99")
            self.titulo_entry.delete(0,'end')
            self.autor_entry.delete(0,'end')
            self.id_entry.delete(0,'end')
            self.nome_entry.delete(0,'end')
            self.numero_entry.delete(0,'end')
            self.titulo_entry.focus()

    def devolver(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        id_livro = self.id_entry.get()
        livro_encontrado = None
        
        for livro in self.catalogo_livros:
            if livro.id == id_livro and livro.titulo == titulo and livro.autor == autor:
                livro_encontrado = livro
                break       
        if livro_encontrado == None:
            self.var_resultado.set("Livro não encontrado na Biblioteca")
            self.mensagem.configure(background="indianred1")
            return
        
        if livro_encontrado.status == 'Disponivel':
            self.var_resultado.set("Livro disponível na Biblioteca para empréstimo")
            self.mensagem.configure(background="indianred1")
        else:
            livro_encontrado.status = 'Disponivel'
            self.var_resultado.set("Devolução feita com sucesso")
            self.mensagem.configure(background="#99FF99")
            self.titulo_entry.delete(0,'end')
            self.autor_entry.delete(0,'end')
            self.id_entry.delete(0,'end')
            self.titulo_entry.focus()   
 
    # Para editar o livro é nescessario 2 inputs corretos para editar a informação, para que haja certeza de que é o livro certo
    def editar(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        id = self.id_entry.get()

        for livro in self.catalogo_livros:
            if livro.id == id and livro.autor == autor:
                livro.titulo = titulo
                self.var_resultado.set("titulo alterado.")
                self.mensagem.configure(background="#99FF99")
                self.titulo_entry.delete(0,'end')
                self.autor_entry.delete(0,'end')
                self.id_entry.delete(0,'end')
                self.titulo_entry.focus()
                break
            elif livro.id == id and livro.titulo == titulo:
                livro.autor = autor
                self.var_resultado.set("autor alterado.")
                self.mensagem.configure(background="#99FF99")
                self.titulo_entry.delete(0,'end')
                self.autor_entry.delete(0,'end')
                self.id_entry.delete(0,'end')
                self.titulo_entry.focus()
                break
            elif livro.titulo == titulo and livro.autor == autor:
                livro.id = id
                self.var_resultado.set("id alterado.")
                self.mensagem.configure(background="#99FF99")
                self.titulo_entry.delete(0,'end')
                self.autor_entry.delete(0,'end')
                self.id_entry.delete(0,'end')
                self.titulo_entry.focus()
                break
        else:
            self.var_resultado.set("Erro ao alterar registro.")
            self.mensagem.configure(background="indianred1")

    #Por medidas de segurança é bom que informe todos as informações corretas do livro para que o exclua, para que exclua livros com o mesmo autor ou de titulos iguais
    def excluir(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        id = self.id_entry.get()
        self.id = self.titulo_entry.get().split()
        for livro in self.catalogo_livros:
            if livro.id==id and livro.titulo == titulo and livro.autor == autor:
                self.catalogo_livros.remove(livro) 
                self.var_resultado.set("Registro excluído")
                self.mensagem.configure(background="#99FF99")
                self.titulo_entry.delete(0,'end')
                self.autor_entry.delete(0,'end')
                self.id_entry.delete(0,'end')
                self.titulo_entry.focus()
            else:
                self.var_resultado.set("Erro ao excluir registro")
                self.mensagem.configure(background="indianred1")           

    def add_membro(self):
        self.nome_m = self.nome_entry.get()
        self.numero_m = self.numero_entry.get()

        if self.nome_m=='' or self.numero_m=='':
            self.var_resultado.set('Erro ao cadastrar novo membro')
            self.mensagem.config(background='indianred1')
        else:
            for membro in self.registro_membros:
                if membro.numero == self.numero_m:
                    self.var_resultado.set('Número já cadastrado')
                    self.mensagem.config(background='indianred1')
                    return
            self.novo_membro = Membro(self.nome_m,self.numero_m)
            self.registro_membros.append(self.novo_membro)
            self.var_resultado.set('Membro cadastrado com sucesso')
            self.mensagem.config(background='#99ff99')
            self.nome_entry.delete(0,'end')
            self.numero_entry.delete(0,'end')
            self.nome_entry.focus()
 
    def editar_membro(self):
        self.nome_m = self.nome_entry.get()
        self.numero_m = self.numero_entry.get()

        for membro in self.registro_membros:
            if membro.nome == self.nome_m:
                if membro.numero == self.numero_m:
                    self.var_resultado.set('Número existente | Insira novo número')
                    self.mensagem.config(background='indianred1')
                    return
                else:
                    membro.numero = self.numero_m
                    self.var_resultado.set("Número do membro alterado")
                    self.mensagem.configure(background="#99FF99")
                    self.nome_entry.delete(0,'end')
                    self.numero_entry.delete(0,'end')
                    self.nome_entry.focus()
                    return
            elif membro.numero == self.numero_m:
                    membro.nome = self.nome_m
                    self.var_resultado.set("Nome do membro alterado")
                    self.mensagem.configure(background="#99FF99")
                    self.nome_entry.delete(0,'end')
                    self.numero_entry.delete(0,'end')
                    self.nome_entry.focus()
                    return
        else:
                self.var_resultado.set("Erro ao editar membro | Membro inexistente")
                self.mensagem.configure(background="indianred1")
    
    def mostrar_membros(self):
        self.var_resultado.set("")
        self.mensagem.configure(background="silver")
        print("|||||||||||||| Registro de Membros ||||||||||||||")
        for membro in self.registro_membros:
            print(f"Membro: {membro.nome}, Número: {membro.numero}")

    def mostrar_historico(self):
        self.nome_m = self.nome_entry.get()
        self.numero_m = self.numero_entry.get()

        if self.nome_m=='' or self.numero_m=='':
            self.var_resultado.set('Erro ao procurar histórico')
            self.mensagem.config(background='indianred1')
        else:
            for membro in self.registro_membros:
                if membro.nome == self.nome_m and membro.numero == self.numero_m:
                    self.var_resultado.set("")
                    self.mensagem.configure(background="silver")
                    print("|||||||||||||| Histórico ||||||||||||||")
                    print(f"Membro: {membro.nome}, Número: {membro.numero}\nHistórico:")
                    for livro in membro.historico:
                        print(f'{livro}',end='\n')
                    self.nome_entry.delete(0,'end')
                    self.numero_entry.delete(0,'end')
                    self.nome_entry.focus()
                    return
            else:
                self.var_resultado.set("Erro ao visualizar histórico | Membro inexistente")
                self.mensagem.configure(background="indianred1")

    def excluir_membro(self):
        nome = self.nome_entry.get()
        numero = self.numero_entry.get()
        for membro in self.registro_membros:
            if membro.nome==nome and membro.numero == numero:
                self.registro_membros.remove(membro) 
                self.var_resultado.set("Registro de membro excluído")
                self.mensagem.configure(background="#99FF99")
                self.nome_entry.delete(0,'end')
                self.numero_entry.delete(0,'end')
                self.nome_entry.focus()
            else:
                self.var_resultado.set("Erro ao excluir membro | Membro inexistente")
                self.mensagem.configure(background="indianred1")

    def widgets(self):
        # LABELS E ENTRADAS DO FRAME 1
        self.var_resultado = StringVar()
        self.mensagem = Label(self.frame_1,textvariable=self.var_resultado,font=('Verdana',12,'bold'),bg='silver')
        self.mensagem.place(relx=0.02,rely=0.03,relwidth=0.96,relheight=0.1)

        self.titulo = Label(self.frame_1,text='TÍTULO',font=('Verdana',10,'bold'),bg='#ebebeb')
        self.titulo.place(relx=0.03,rely=0.2,relwidth=0.1,relheight=0.08)

        self.titulo_entry = Entry(self.frame_1)
        self.titulo_entry.place(relx=0.15,rely=0.2,relwidth=0.4,relheight=0.1)
        self.titulo_entry.focus()

        self.autor = Label(self.frame_1,text='AUTOR',font=('Verdana',10,'bold'),bg='#ebebeb')
        self.autor.place(relx=0.03,rely=0.4,relwidth=0.1,relheight=0.1)

        self.autor_entry = Entry(self.frame_1)
        self.autor_entry.place(relx=0.15,rely=0.4,relwidth=0.4,relheight=0.1)

        self.id = Label(self.frame_1,text='ID',font=('Verdana',10,'bold'),bg='#ebebeb')
        self.id.place(relx=0.03,rely=0.6,relwidth=0.1,relheight=0.1)

        self.id_entry = Entry(self.frame_1)
        self.id_entry.place(relx=0.15,rely=0.6,relwidth=0.4,relheight=0.1)

        # Achei necessario criar um outro frame com inputs do nome e o numero do membro já que era preciso para identifica-los e criar um historico para cada membro

        # LABELS E ENTRADAS DO FRAME 2
        self.nome = Label(self.frame_2,text='MEMBRO',font=('Verdana',10,'bold'),bg='#ebebeb')
        self.nome.place(relx=0.03,rely=0.2,relwidth=0.1,relheight=0.1)

        self.nome_entry = Entry(self.frame_2)
        self.nome_entry.place(relx=0.15,rely=0.2,relwidth=0.4,relheight=0.1)

        self.numero = Label(self.frame_2,text='NÚMERO',font=('Verdana',10,'bold'),bg='#ebebeb')
        self.numero.place(relx=0.03,rely=0.4,relwidth=0.1,relheight=0.1)

        self.numero_entry = Entry(self.frame_2)
        self.numero_entry.place(relx=0.15,rely=0.4,relwidth=0.4,relheight=0.1)

        #BOTOES DO FRAME 1
        self.btn_cadastrar = Button(self.frame_1,text='Cadastrar',font=('Verdana',10),bg='#ebebeb',command=self.cadastrar_livro)
        self.btn_cadastrar.place(relx=0.6,rely=0.2,relwidth=0.12,relheight=0.1)

        self.btn_pesquisar = Button(self.frame_1,text='Pesquisar',font=('Verdana',10),bg='#ebebeb',command=self.pesquisar)
        self.btn_pesquisar.place(relx=0.8,rely=0.2,relwidth=0.12,relheight=0.1)

        self.btn_emprestar = Button(self.frame_1,text='Emprestar',font=('Verdana',10),bg='#ebebeb',command=self.emprestar)
        self.btn_emprestar.place(relx=0.6,rely=0.4,relwidth=0.12,relheight=0.1)

        self.btn_devolver = Button(self.frame_1,text='Devolver',font=('Verdana',10),bg='#ebebeb',command=self.devolver)
        self.btn_devolver.place(relx=0.8,rely=0.4,relwidth=0.12,relheight=0.1)

        self.btn_editar = Button(self.frame_1,text='Editar',font=('Verdana',10),bg='#ebebeb',command=self.editar)
        self.btn_editar.place(relx=0.6,rely=0.6,relwidth=0.12,relheight=0.1)

        self.btn_excluir = Button(self.frame_1,text='Excluir',font=('Verdana',10),bg='#ebebeb',command=self.excluir)
        self.btn_excluir.place(relx=0.8,rely=0.6,relwidth=0.12,relheight=0.1)

        # No frame 2 há botões baseados nos do frame 1 mas voltados para a organização dos membros da biblioteca

        # BOTOES DO FRAME 2
        self.btn_add_membro = Button(self.frame_2,text='Adicionar',font=('Verdana',10),bg='#ebebeb',command=self.add_membro)
        self.btn_add_membro.place(relx=0.6,rely=0.2,relwidth=0.12,relheight=0.1)

        self.btn_mostrar_membros = Button(self.frame_2,text='Registro',font=('Verdana',10),bg='#ebebeb',command=self.mostrar_membros)
        self.btn_mostrar_membros.place(relx=0.8,rely=0.2,relwidth=0.12,relheight=0.1)

        self.btn_editar_membro = Button(self.frame_2,text='Editar',font=('Verdana',10),bg='#ebebeb',command=self.editar_membro)
        self.btn_editar_membro.place(relx=0.6,rely=0.4,relwidth=0.12,relheight=0.1)

        self.btn_historico = Button(self.frame_2,text='Histórico',font=('Verdana',10),bg='#ebebeb',command=self.mostrar_historico)
        self.btn_historico.place(relx=0.8,rely=0.4,relwidth=0.12,relheight=0.1)

        self.btn_excluir_membro = Button(self.frame_2,text='Excluir',font=('Verdana',10),bg='#ebebeb',command=self.excluir_membro)
        self.btn_excluir_membro.place(relx=0.6,rely=0.6,relwidth=0.12,relheight=0.1)

class Livro(Biblioteca):
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.id = 1
        self.status = 'Disponivel'

class Membro(Biblioteca):
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero
        self.historico = []

Biblioteca()