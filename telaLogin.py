#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Jul 23, 2020 04:41:56 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class Toplevel1:
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {SimSun} -size 21 -weight bold"
        font14 = "-family {SimSun} -size 13"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top=tk.Tk()
        self.top.geometry("626x542+677+160")
        self.top.minsize(120, 1)
        self.top.maxsize(1924, 1061)
        self.top.resizable(1, 1)
        self.top.title("Login")
        self.top.configure(background="#f2dc91")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.24, rely=0.148, relheight=0.638, relwidth=0.511)

        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#4f9499")
        self.Frame1.configure(cursor="fleur")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.125, rely=0.28,height=20, relwidth=0.763)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Frame1, show='*')
        self.Entry2.place(relx=0.125, rely=0.506,height=20, relwidth=0.763)
        self.Entry2.configure(background="white")
        self.Entry2.configure(cursor="fleur")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.325, rely=0.029, height=39, width=108)
        self.Label1.configure(background="#4f9499")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Login''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.119, rely=0.197, height=21, width=70)
        self.Label2.configure(background="#4f9499")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font14)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Usuario''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.119, rely=0.422, height=20, width=51)
        self.Label3.configure(background="#4f9499")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Senha''')

        self.Button1 = tk.Button(self.Frame1, command=self.LoginBackEnd)
        self.Button1.place(relx=0.125, rely=0.702, height=34, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#417092")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")
        self.Button1.configure(text='''Logar''')

        self.Button2 = tk.Button(self.Frame1, command=self.Cadastro)
        self.Button2.place(relx=0.594, rely=0.702, height=34, width=97)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#417092")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Cadastre-se''')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.506, rely=0.694, relheight=0.116)
        self.TSeparator1.configure(orient="vertical")
        self.top.mainloop()

    def Cadastro(self):
        '''This class configures and populates the toplevel window.
                           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font12 = "-family {SimSun} -size 21 -weight bold"
        font14 = "-family {SimSun} -size 13"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        self.root = tk.Tk()
        self.root.geometry("626x542+677+160")
        self.root.minsize(120, 1)
        self.root.maxsize(1924, 1061)
        self.root.resizable(1, 1)
        self.root.title("Cadastro")
        self.root.configure(background="#f2dc91")

        self.frameCadastro = tk.Frame(self.root)
        self.frameCadastro.place(relx=0.24, rely=0.148, relheight=0.638, relwidth=0.511)

        self.frameCadastro.configure(relief='flat')
        self.frameCadastro.configure(borderwidth="2")
        self.frameCadastro.configure(background="#4f9499")
        self.frameCadastro.configure(cursor="fleur")

        self.Entry1Cadastro = tk.Entry(self.frameCadastro)
        self.Entry1Cadastro.place(relx=0.125, rely=0.28, height=20, relwidth=0.763)
        self.Entry1Cadastro.configure(background="white")
        self.Entry1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry1Cadastro.configure(font="TkFixedFont")
        self.Entry1Cadastro.configure(foreground="#000000")
        self.Entry1Cadastro.configure(insertbackground="black")

        self.Entry2Cadastro = tk.Entry(self.frameCadastro, show='*')
        self.Entry2Cadastro.place(relx=0.125, rely=0.506, height=20, relwidth=0.763)
        self.Entry2Cadastro.configure(background="white")
        self.Entry2Cadastro.configure(cursor="fleur")
        self.Entry2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2Cadastro.configure(font="TkFixedFont")
        self.Entry2Cadastro.configure(foreground="#000000")
        self.Entry2Cadastro.configure(insertbackground="black")

        self.Label1Cadastro = tk.Label(self.frameCadastro)
        self.Label1Cadastro.place(relx=0.325, rely=0.029, height=39, width=120)
        self.Label1Cadastro.configure(background="#4f9499")
        self.Label1Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label1Cadastro.configure(font=font12)
        self.Label1Cadastro.configure(foreground="#ffffff")
        self.Label1Cadastro.configure(text='''Cadastro''')

        self.Label2Cadastro = tk.Label(self.frameCadastro)
        self.Label2Cadastro.place(relx=0.119, rely=0.197, height=21, width=70)
        self.Label2Cadastro.configure(background="#4f9499")
        self.Label2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Label2Cadastro.configure(font=font14)
        self.Label2Cadastro.configure(foreground="#ffffff")
        self.Label2Cadastro.configure(text='''Usuario''')

        self.Label3 = tk.Label(self.frameCadastro)
        self.Label3.place(relx=0.119, rely=0.422, height=20, width=51)
        self.Label3.configure(background="#4f9499")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Senha''')

        self.Button2Cadastro = tk.Button(self.frameCadastro, command=self.CadastrarBackEnd)
        self.Button2Cadastro.place(relx=0.594, rely=0.702, height=34, width=97)
        self.Button2Cadastro.configure(activebackground="#ececec")
        self.Button2Cadastro.configure(activeforeground="#000000")
        self.Button2Cadastro.configure(background="#417092")
        self.Button2Cadastro.configure(disabledforeground="#a3a3a3")
        self.Button2Cadastro.configure(foreground="#ffffff")
        self.Button2Cadastro.configure(highlightbackground="#d9d9d9")
        self.Button2Cadastro.configure(highlightcolor="black")
        self.Button2Cadastro.configure(pady="0")
        self.Button2Cadastro.configure(relief="flat")
        self.Button2Cadastro.configure(text='''Cadastre-se''')

        self.TSeparator1 = ttk.Separator(self.frameCadastro)
        self.TSeparator1.place(relx=0.506, rely=0.694, relheight=0.116)
        self.TSeparator1.configure(orient="vertical")
        self.root.mainloop()

    def CadastrarBackEnd(self):
        try:
            with open('usuarios.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry1Cadastro.get() + '\n')

            with open('senhas.txt', 'a') as arquivoUsuario:
                arquivoUsuario.write(self.Entry2Cadastro.get() + '\n')
            self.root.destroy()
        except:
            print('Houve um erro')

    def LoginBackEnd(self):
        with open('usuarios.txt', 'r') as arquivoUsuario:
            usuarios = arquivoUsuario.readlines()
        with open('senhas.txt', 'r') as arquivoUsuario:
            senhas = arquivoUsuario.readlines()

        usuarios = list(map(lambda x: x.replace('\n', ''),usuarios)) #retirar \n do final de cada usuario
        senhas = list(map(lambda x: x.replace('\n', ''), senhas)) #retirar \n do final de cada senha

        usuario = self.Entry1.get()
        senha = self.Entry2.get()

        logado = False

        for i in range(len(usuarios)):
            if usuario == usuarios[i] and senha == senhas[i]:
                print('Usuario Logado')
                self.top.destroy()
                self.telaLogado()
                logado = True

        if not logado:
            print('usuario ou senha incorreto')
            self.top.destroy()
            self.usuarioIncorreto()

    def telaLogado(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {SimSun} -size 16"

        self.telaLogado = tk.Tk()
        self.telaLogado.geometry("600x450+752+221")
        self.telaLogado.minsize(120, 1)
        self.telaLogado.maxsize(1924, 1061)
        self.telaLogado.resizable(1, 1)
        self.telaLogado.title("Usuario logado")
        self.telaLogado.configure(background="#f5e4bc")

        self.Frame1Logado = tk.Frame(self.telaLogado)
        self.Frame1Logado.place(relx=0.1, rely=0.267, relheight=0.211, relwidth=0.808)
        self.Frame1Logado.configure(relief='groove')
        self.Frame1Logado.configure(borderwidth="2")
        self.Frame1Logado.configure(relief="groove")
        self.Frame1Logado.configure(background="#f4d9bd")

        self.Label1Logado = tk.Label(self.Frame1Logado)
        self.Label1Logado.place(relx=0.227, rely=0.316, height=31, width=254)
        self.Label1Logado.configure(background="#f4d9bd")
        self.Label1Logado.configure(disabledforeground="#a3a3a3")
        self.Label1Logado.configure(font=font10)
        self.Label1Logado.configure(foreground="#000000")
        self.Label1Logado.configure(text='''Usuario Logado''')
        self.telaLogado.mainloop()

    def usuarioIncorreto(self):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.telaIncorreto = tk.Tk()
        self.telaIncorreto.geometry("600x450+752+221")
        self.telaIncorreto.minsize(120, 1)
        self.telaIncorreto.maxsize(1924, 1061)
        self.telaIncorreto.resizable(1, 1)
        self.telaIncorreto.title("Atenção")
        self.telaIncorreto.configure(background="#f5e4bc")
        self.telaIncorreto.configure(highlightbackground="#d9d9d9")
        self.telaIncorreto.configure(highlightcolor="black")

        self.Frame1Incorreto = tk.Frame(self.telaIncorreto)
        self.Frame1Incorreto.place(relx=0.1, rely=0.267, relheight=0.211, relwidth=0.808)
        self.Frame1Incorreto.configure(relief='groove')
        self.Frame1Incorreto.configure(borderwidth="2")
        self.Frame1Incorreto.configure(relief="groove")
        self.Frame1Incorreto.configure(background="#f4d9bd")
        self.Frame1Incorreto.configure(highlightbackground="#d9d9d9")
        self.Frame1Incorreto.configure(highlightcolor="black")

        self.Label1Incorreto = tk.Label(self.Frame1Incorreto)
        self.Label1Incorreto.place(relx=0.165, rely=0.316, height=31, width=314)
        self.Label1Incorreto.configure(activebackground="#f9f9f9")
        self.Label1Incorreto.configure(activeforeground="black")
        self.Label1Incorreto.configure(background="#f4d9bd")
        self.Label1Incorreto.configure(disabledforeground="#a3a3a3")
        self.Label1Incorreto.configure(
            font="-family SimSun -size 16 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1Incorreto.configure(foreground="#000000")
        self.Label1Incorreto.configure(highlightbackground="#d9d9d9")
        self.Label1Incorreto.configure(highlightcolor="black")
        self.Label1Incorreto.configure(text='''Usuario ou Senha incorreto !''')




Toplevel1()




