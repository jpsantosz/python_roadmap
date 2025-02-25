from biblioteca import Biblioteca, Book, User

biblioteca = Biblioteca()

while True: 
    print("\n📚 MENU BIBLIOTECA")
    print("1. Adicionar Livro")
    print("2. Adicionar Usuário")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Listar Livros")
    print("6. Listar Usuários")
    print("7. Excluir Livro")
    print("8. Excluir Usuário")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        id_book = int(input("ID do Livro: "))
        book_title = input("Título do livro: ")
        autor = input("Autor: ")
        biblioteca.add_books(Book(book_title, autor, id_book))
        
    elif opcao == "2":
        id_user = int(input("ID do Usuário: "))
        user_name = input("Nome do Usuário: ")
        biblioteca.add_users(User(user_name, id_user))
        
    elif opcao == "3":
        id_user = int(input("ID do Usuário: "))
        id_book = int(input("ID do Livro: "))
        biblioteca.emprestar_livros(id_user, id_book)
              
    elif opcao == "4":
        id_user = int(input("ID do Usuário: "))
        id_book = int(input("ID do Livro: "))
        biblioteca.devolver_livro(id_user, id_book)
        
    elif opcao == "5":
        print("\n📖 Lista de Livros:")
        biblioteca.listar_livros()
        
    elif opcao == "6":
        print("\n👥 Lista de Usuários:")
        biblioteca.listar_users()
        
    elif opcao == "7":
        id_book = int(input("ID do Livro: "))
        biblioteca.delete_book(id_book)
        
    elif opcao == "8":
        id_user = int(input("ID do Usuário: "))
        biblioteca.delete_user(id_user)
        
    elif opcao == "0":
        ("Print Encerrando o Programa...")
        break
        
    else:
        print("Digite uma opção válida!")