class Filme:
    def __init__(self, id_filme: int, titulo: str, genero: str):
        self.id_filme = id_filme
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True
        
class Cliente:
    def __init__(self, id_cliente: str, nome: str):
        self.id_cliente = id_cliente
        self.nome = nome
        
class Locadora:
    def __init__(self, arquivo_dados="dados_videolocadora.json"):
        self.arquivo_dados = arquivo_dados
        self.filmes = []
        self.clientes = []
        self.emprestimos = {}
        self.carregar_dados()
    
    def adicionar_filme(self, filme: Filme):
        self.filmes.append(filme)
        print(f"O filme {filme.titulo} foi adicionado ao sistema.")
        self.salvar_dados()
        
    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"O filme {cliente.nome} foi adicionado ao sistema.")
        self.salvar_dados()
        
    def excluir_filme(self, filme: Filme):
        self.filmes.remove(filme)
        print(f"O filme {filme.titulo} foi excluído do sistema.")
        self.salvar_dados()
        
    def excluir_cliente(self, cliente: Cliente):
        self.filmes.remove(cliente)
        print(f"O cliente {cliente.nome} foi excluído do sistema.")
        self.salvar_dados()
        
    def listar_filmes(self):
        for filme in self.filmes:
            print(f"{filme.nome} - {filme.id_filme}")
    
    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"{cliente.nome} - {cliente.id_cliente}")