import json

class Filme:
    def __init__(self, id_filme: int, titulo: str, genero: str):
        self.id_filme = id_filme
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True
        
class Cliente:
    def __init__(self, id_cliente: int, nome: str):
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
        print(f"O cliente {cliente.nome} foi adicionado ao sistema.")
        self.salvar_dados()
        
    def excluir_filme(self, id_filme):
        filme = next((f for f in self.filmes if f.id_filme == id_filme), None)
        self.filmes.remove(filme)
        print(f"O filme {filme.titulo} foi excluído do sistema.")
        self.salvar_dados()
        
    def excluir_cliente(self, id_cliente: int):
        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)
        self.clientes.remove(cliente)
        print(f"O cliente {cliente.nome} foi excluído do sistema.")
        self.salvar_dados()
        
    def listar_filmes(self):
        for filme in self.filmes:
            print(f"{filme.titulo} - {filme.id_filme}")
    
    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"{cliente.nome} - {cliente.id_cliente}")
    
    def alugar_filme(self, id_filme: int, id_cliente: int):
        filme = next((f for f in self.filmes if f.id_filme == id_filme and f.disponivel), None)
        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)
        
        if filme and cliente:
            filme.disponivel = False
            self.emprestimos.setdefault(id_cliente, []).append(id_filme)
            self.salvar_dados()
            print(f"O filme {filme.titulo} foi alugador por {cliente.nome}.")
        else:
            print("Filme ou cliente não encontrado!")
            
    def devolver_filme(self, id_filme: int, id_cliente: int):
        if id_cliente in self.emprestimos and id_filme in self.emprestimos[id_cliente]:
            filme = next((f for f in self.filmes if f.id_filme == id_filme), None)
            filme.disponivel = True
            self.emprestimos[id_cliente].remove(id_filme)
            if not self.emprestimos[id_cliente]:
                del self.emprestimos[id_cliente]
            self.salvar_dados()
            print(f"O filme {filme.titulo} foi devolvido.")
        else:
            print("Filme ou cliente não encontrado!")
            
    def salvar_dados(self):
        data = {
            "filmes":  [{"Título": f.titulo, "Gênero": f.genero, "Id": f.id_filme, "disponivel": f.disponivel} for f in self.filmes],
            "clientes":  [{"Nome": c.nome, "Id": c.id_cliente} for c in self.clientes],
            "Empréstimos":  self.emprestimos 
        }
        
        with open (self.arquivo_dados, "w") as file:
            json.dump(data, file, indent=4)
            
        
    def carregar_dados(self):
        try:
            with open (self.arquivo_dados, "r") as file:
                data = json.load(file)
                self.filmes = [Filme(f["Id"], f["Título"], f["Gênero"]) for f in data["filmes"]]
                for filme, disponivel in zip(self.filmes, [f["disponivel"] for f in data["filmes"]]):
                    filme.disponivel = disponivel
                self.clientes = [Cliente(c["Id"], c["Nome"]) for c in data["clientes"]]
                self.emprestimos = data["Empréstimos"]
        except FileNotFoundError:
            self.salvar_dados()  