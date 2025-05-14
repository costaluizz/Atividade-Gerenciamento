from abc import ABC, abstractmethod

class Tarefa (ABC):
    def __init__(self,titulo,descricao,status,prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade

    @abstractmethod
    def cadastro_usuario(self):
        pass

    def criar_tarefas(self,titulo,descricao,status):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
    
    

class Usuario():

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

    def cadastro_usuario(self,nome,email):
        if len(nome) <= 15 and "@"  in email :
            print("Cadastro realizado com sucesso")
        else:
            print("Cadastro não realizado")
        
        
print("-----Cadastro Usuario-----")
nome = str(input("Nome Usuario(max:15caracteres):  "))
email = str(input("Email do Usuario:  "))

usuario_teste = Usuario(nome,email)
usuario_teste.cadastro_usuario(nome,email)

class Sistema_de_Tarefas