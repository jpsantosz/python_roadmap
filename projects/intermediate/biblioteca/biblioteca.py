import json

class User:
    def __init__(self, name: str, id_user: int):
        self.name = name
        self.id_user = id_user
        
    def __repr__(self):
        return f"({self.id_user}) {self.name}"
        
class Book:
    def __init__(self, title: str, autor: str, id_book: int, avaliable: bool):
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
            "livros": [{"id": l.id_book, "titulo": l.title, "autor": l.autor, "disponivel": l.avaliable} for l in self.books],
            "usuarios": [{"id": u.id_user, "nome": u.name} for u in self.users],
            "emprestimos": self.emprestimos
        }
        
        with open (self.arquivo_dados,"w") as file:
            json.dump(dados, file, indent=4)
            
        