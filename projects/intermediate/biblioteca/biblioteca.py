import json

class User:
    def __init__(self, name: str, id_user: int):
        self.name = name
        self.id_user = id_user
        
    def __repr__(self):
        return f"({self.id_user}) {self.name}"
        
class Book:
    def __init__(self, title: str, autor: str, id_book: int):
        self.title = title
        self.autor = autor
        self.id_book = id_book
        self.avaliable = True
        
    def __repr__(self):
        status = "Disponível" if self.avaliable else "Emprestado"
        return f"({self.id_book}) {self.title} - {self.autor} [{status}]"

class Biblioteca:
    def __init__(self, arquivo_dados="dados.json"):
        self.arquivo_dados = arquivo_dados
        self.books = []
        self.users = []
        self.emprestimos = {}
        self.carregar_dados()
    
    def add_books(self, book: Book):
        self.books.append(book)
        self.salvar_dados()
        
    def add_users(self, user: User):
        self.users.append(user)
        self.salvar_dados()
        
    def delete_book(self, id_book):
        book = next((b for b in self.books if b.id_book == id_book), None)
        
        if book:
            self.books.remove(book)
            print(f"📕 Livro '{book.title}' removido com sucesso.")
            self.salvar_dados()
        else:
            print(f"❌ Nenhum livro encontrado com o ID {id_book}.")

        
    def delete_user(self, id_user):
        user = next((u for u in self.users if u.id_user == id_user), None)
        
        if user:
            self.users.remove(user)
            print(f"👤 Usuário '{user.name}' removido com sucesso.")
            self.salvar_dados()
        else:
            print(f"❌ Nenhum usuário encontrado com o ID {id_user}.")

        
    def emprestar_livros(self, id_user, id_book):
        user = next((u for u in self.users if u.id_user == id_user), None)
        book = next((l for l in self.books if l.id_book == id_book and l.avaliable), None)
        
        if user and book:
            book.avaliable = False
            self.emprestimos.setdefault(id_user, []).append(id_book)
            self.salvar_dados()
            print(f"✅ Livro '{book.title}' emprestado para {user.name}.")
        else:
            print("❌ Usuário não encontrado ou livro indisponível.")
            
    def devolver_livro(self, id_user, id_book):
        if id_user in self.emprestimos and id_book in self.emprestimos[id_user]:
            book = next(b for b in self.books if b.id_book == id_book)
            book.avaliable = True
            self.emprestimos[id_user].remove(id_book)
            if not self.emprestimos[id_user]:
                del self.emprestimos[id_user]
            self.salvar_dados()
            print(f"🔄 Livro '{book.title}' foi devolvido.")
        else:
            print("❌ Empréstimo não encontrado.")
            
    def listar_livros(self):
        for book in self.books:
            print(book)
            
    def listar_users(self):
        for user in self.users:
            print(user)
            
    def salvar_dados(self):
        dados = {
            "livros": [{"titulo": l.title,"autor": l.autor, "id": l.id_book, "disponivel": l.avaliable} for l in self.books],
            "usuarios": [{"id": u.id_user, "nome": u.name} for u in self.users],
            "emprestimos": self.emprestimos
        }
        
        with open (self.arquivo_dados,"w") as file:
            json.dump(dados, file, indent=4)
            
    def carregar_dados(self):
        try:
            with open (self.arquivo_dados, "r") as file:
                dados = json.load(file)
                self.books = [Book(l["titulo"], l["autor"], l["id"]) for l in dados["livros"]]
                for livro, avaliable in zip(self.books, [l["disponivel"] for l in dados["livros"]]):
                    livro.avaliable = avaliable
                self.users = [User(u["nome"], u["id"]) for u in dados["usuarios"]]
                self.emprestimos = dados["emprestimos"]
        except FileNotFoundError:
            self.salvar_dados()  
        