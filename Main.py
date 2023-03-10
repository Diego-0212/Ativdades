from abc import ABC , abstractmethod
from tkinter import messagebox
import customtkinter

#configuração da janela de exibição do programa
janela = customtkinter.CTk()
janela.geometry("700x500")
janela.title("Fatec")

cod_entry = customtkinter.StringVar(janela)
nome_entry = customtkinter.StringVar(janela)

nome = customtkinter.CTkLabel(janela, text="Digite seu nome: " ,)
nome.pack(padx=15, pady=12)

nome_entrada = customtkinter.CTkEntry(janela , textvariable=nome_entry)
nome_entrada.pack(padx=15, pady=12)

texto_auxiliar = customtkinter.CTkLabel(janela, text="Qual a sua relação com a FATEC :\n\n1.Aluno\n2.Professor\n3. Coordenador \n 4. Diretor \n 5. Administrativo \n 6. Vestibulando \n")
texto_auxiliar.pack(padx=15, pady=12)

cod_entrada = customtkinter.CTkEntry(janela , textvariable=cod_entry)
cod_entrada.pack(padx=15, pady=12)

#Inicio com Classes Aluno, Professor, Coordenador, Diretor, Administrativo, Vestiibulando e Fabrica_pessoa
def clicar():
    class Pessoa(ABC):
        @abstractmethod 
        def entrar(self, nome) :
            pass

    class Aluno(Pessoa): 
        def entrar(self, nome):
            return f"{nome} tem relação com a instituição como Aluno(a)"

    class Professor(Pessoa):
        def entrar(self, nome):
            return f"{nome} tem relação com a instituição como Professor(a)"

    class Coordenador(Pessoa): 
        def entrar(self, nome): 
            return f"{nome} tem relação com a instituição como Coordenador(a)"       

    class Diretor(Pessoa):
        def entrar(self, nome): 
            return f"{nome} tem relação com a instituição como Diretor(a)"
        
    class Administrativo(Pessoa): 
        def entrar(self, nome): 
            return f"{nome} tem relação com a instituição como Administrativo(a)" 

    class Vestibulando(Pessoa): 
        def entrar(self, nome): 
            return f"{nome} tem relação com a instituição como Vestibulando"       


    class FabricaPessoa: 
        def identificar_pessoa(self, tipo_pessoa):
            if tipo_pessoa == 1: 
                return Aluno() 
            elif tipo_pessoa == 2: 
                return Professor()
            elif tipo_pessoa == 3:
                return Coordenador() 
            elif tipo_pessoa == 4: 
                return Diretor()    
            elif tipo_pessoa == 5: 
                return Administrativo()
            elif tipo_pessoa == 6: 
                return Vestibulando()    
            else: 
                return ("{self.nome} não tem nenhuma relação com a instituição, acompanhar até a secretaria")

#identificação 
    fabrica_pessoa = FabricaPessoa()

    if cod_entry.get() == "1":
        aluno = fabrica_pessoa.identificar_pessoa(1)
        ms = messagebox.showinfo("saida", aluno.entrar(nome_entry.get()))  

    elif cod_entry.get() == "2":
        prof = fabrica_pessoa.identificar_pessoa(2)
        ms = messagebox.showinfo("saida", prof.entrar(nome_entry.get()))    

    elif cod_entry.get()  == "3":
        coord = fabrica_pessoa.identificar_pessoa(3)
        ms = messagebox.showinfo("saida", coord.entrar(nome_entry.get()))

                
    elif cod_entry.get() == "4":
        dir = fabrica_pessoa.identificar_pessoa(4)
        ms = messagebox.showinfo("saida", (dir.entrar(nome_entry.get())))
    
    elif cod_entry.get() == "5":
        admin = fabrica_pessoa.identificar_pessoa(5)
        ms = messagebox.showinfo("saida", admin.entrar(nome_entry.get())) 

    elif cod_entry.get() == "6":
        Vestibulando = fabrica_pessoa.identificar_pessoa(6)
        ms = messagebox.showinfo("saida", Vestibulando.entrar(nome_entry.get()))            
        

    else:
        messagebox.showinfo("saida", f"{nome_entry.get()} não tem nenhuma relação com a instituição, acompanhar até a secretaria")


    if ms == 'ok':
        msg = messagebox.askquestion('sair App','Deseja Continuar? ')
        if msg == "sim":
            cod_entrada.delete(0 , customtkinter.END)
            cod_entrada.insert(customtkinter.END,"")
            nome_entrada.delete(0 , customtkinter.END)
            nome_entrada.insert(customtkinter.END,"")
        elif msg == "não":
            janela.destroy()

        
botao = customtkinter.CTkButton(janela , text = "Enviar" , command=clicar)
botao.pack(padx=20, pady=20)
        
janela.mainloop()



                