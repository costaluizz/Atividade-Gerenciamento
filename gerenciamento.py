
class Tarefa:
    incrementa_id = 1
    def __init__(self,titulo,descricao,prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Pendente"
        self.id = Tarefa.incrementa_id 
        Tarefa.incrementa_id += 1
    
    def concluir_tarefa(self):
        self.status = "Concluida"
        print(f"Tarefa: {self.titulo} concluida!")
    
    def editar_tarefa(self, novo_titulo, nova_descricao , nova_prioridade):
        self.titulo = novo_titulo
        self.descricao = nova_descricao
        self.prioridade = nova_prioridade


    def __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao} - {self.prioridade}"


class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.lista_tarefas = []
       
    def criar_tarefas(self,titulo,descricao,prioridade):
        nova_tarefa = Tarefa(titulo,descricao,prioridade)
        self.lista_tarefas.append(nova_tarefa)


    def listar_tarefas(self,status=None):
        for tarefa in self.lista_tarefas:
            if status is None or tarefa.status == status:
                print(tarefa)
    
    def procura_tarefa(self, id_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None
    
    def remover_tarefa(self, id_tarefa):
        tarefa_buscada = self.procura_tarefa(id_tarefa)
        if tarefa_buscada:
            self.lista_tarefas.remove(tarefa_buscada)
        else:
            print("Tarefa não encontrada!")
    
    def limpar_concluidas(self):
        tarefas_ativas = []
        for tarefa in self.lista_tarefas:
            if tarefa.status != "Concluida":
                tarefas_ativas.append(tarefa)
            self.lista_tarefas = tarefas_ativas


class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None
   
    def cadastrar_usuario(self):
        nome = input("Nome Usuario(max:15caracteres): ")
        email = input("Email do Usuario:  ")
        senha = input("Crie uma senha:  \n ")
        if "@" not in email:
            print("E-MAIL inválido \n")
       
        if len(senha) < 4:
            print("Senha muito curta \n")
           
        else:
            novo_usuario = Usuario(nome,email, senha)
            self.lista_usuarios.append(novo_usuario)
            print("Usuario Cadastrado com Sucesso \n")


    def login(self):
        email = input("Entre com o email:  ")
        senha = input("Entre com a senha:  ")


        for usuario in self.lista_usuarios:
            if (usuario.email == email) and (usuario.senha == senha):
               self.usuario_logado = usuario
               print(f"Usuário logado: {self.usuario_logado.nome}")
               self.menu_funcionalidades()
               return
       
        print("Usuário inexistente ou senha invalida \n")
   
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


    def menu_funcionalidades(self):
        escolha = ""
        while escolha != "0":


            print(" \n--------Tarefas--------")
            print("1 - Criar Tarefa")
            print("2 - Listar Tarefas")
            print("3 - Listar Tarefas Pendentes")
            print("4 - Listar Tarefas Concluidas")
            print("5 - Concluir Tarefa")
            print("6 - Editar Tarefa")
            print("7 - Remove Tarefa")
            print("8 - Limpar Tarefas Concluidas")
            escolha = input("Selecione: \n")


            if escolha == "1":
                titulo = str(input("Insira um Titulo: "))
                descricao = str(input("Insira uma Descrição: "))
                prioridade = str(input("Insira uma prioridade (Alta,Media,Baixa): \n"))
                self.usuario_logado.criar_tarefas(titulo,descricao,prioridade)


            elif escolha == "2":
                self.usuario_logado.listar_tarefas()
            
            elif escolha == "3":
                self.usuario_logado.listar_tarefas("Pendente")
            
            elif escolha == "4":
                self.usuario_logado.listar_tarefas("Concluida")
            
            elif escolha == "5":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))

                    if tarefa_buscada:
                        tarefa_buscada.concluir_tarefa()
                    else:
                        print("Tarefa não encontrada!")
            
            elif escolha == "6":
                id = input("Insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))
                    if tarefa_buscada:
                        novo_titulo = input("Insira novo título: ")
                        nova_descricao = input("Insira uma nova descrição: ")
                        nova_prioridade = input("Insira nova prioridade: ")
                        tarefa_buscada.editar_tarefa(novo_titulo, nova_descricao, nova_prioridade)
                    else:
                        print("Tarefa não encontrada!")
            
            elif escolha == "7":
                id = input("Insira o ID da tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.remover_tarefa(int(id))

            elif escolha == "8":
                self.usuario_logado.limpar_concluidas()
            
            

teste = Sistema()
teste.menu_principal()