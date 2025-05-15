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
    
    def listar_tarefas(self):
        pass

    def listar_tarefas_pendentes(self):
        pass
    
    

class Usuario():

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

   
class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None

    def cadastrar_usuario(self):
        nome = input("Nome Usuario(max:15caracteres): ")
        email = input("Email do Usuario:  ")
        senha = input("Crie uma senha:  \n ")

        if "@" not in email:
            print("E-MAIL inválido")
            
        if len(senha) < 4:
            print("Senha muito curta \n")
        else:
            novo_usuario = Usuario(nome,email)
            self.lista_usuarios.append(novo_usuario)
            print("Usuario Cadastrado com Sucesso")

    def login(self):
        email = input("Entre com o email:  ")
        senha = input("Entre com a senha:  ")

        for usuario in self.lista_usuarios:
            if (usuario.email == email) and (usuario.senha == senha):
               self.usuario_logado = usuario
               print(f"Usuário logado: {self.usuario_logado.nome}")
               return
        
        print("Usuário inexistente ou senha invalida")
    
    def menu_principal(self):
        opcao_escolhida = ""
        while opcao_escolhida != "0":

            print("Bem Vindo!Escolha uma opção: \n")
            print("1. Cadastrar novo usuario")
            print("2.Fazer Login")
            print("0.Sair \n")
            opcao_escolhida = input("Escolha: \n")

            if opcao_escolhida == "1":
                self.cadastrar_usuario()
            elif opcao_escolhida == "2":
                self.login()
            elif opcao_escolhida == "0":
                print("Saindo...")
            else:
                print("Opção Invalida")


teste = Sistema()
teste.menu_principal()

        
        
    