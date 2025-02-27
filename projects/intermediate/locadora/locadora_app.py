from locadora import Locadora, Cliente, Filme

locadora = Locadora()

while True:
    print("\n📚 MENU Locadora")
    print("1. Adicionar Filme")
    print("2. Adicionar Cliente")
    print("3. Alugar Filme")
    print("4. Devolver Filme")
    print("5. Listar Filmes")
    print("6. Listar Clientes")
    print("7. Excluir Filme")
    print("8. Excluir Cliente")
    print("0. Sair")
    
    escolha = input("Escolha uma ação: ")
    
    if escolha == "1":
        titulo = input("Digite o nome do filme: ")
        id = int(input("Digite o ID do filme: "))
        genero = input("Digite o gênero do filme: ")
        filme = Filme(id, titulo, genero)
        locadora.adicionar_filme(filme)
        print(f"O filme {filme.titulo} foi adicionado ao catálogo.")
    
    elif escolha == "2":
        nome = input("Digite o nome do cliente: ")
        id = int(input("Digite o ID do cliente: "))
        cliente = Cliente(id, nome)
        locadora.adicionar_cliente(cliente)
        print(f"O cliente {cliente.nome} foi adicionado a lista de clientes.")
    
    elif escolha == "3":
        id_filme = int(input("Digite o ID do filme: "))
        id_cliente = int(input("Digite o ID do cliente: "))
        locadora.alugar_filme(id_filme, id_cliente)
        
    elif escolha == "4":
        id_filme = int(input("Digite o ID do filme: "))
        id_cliente = int(input("Digite o ID do cliente: "))
        locadora.devolver_filme(id_filme, id_cliente)
        
    elif escolha == "5":
        print("Catálogo: \n")
        locadora.listar_filmes()
        
    elif escolha == "6":
        print("Lista de clientes: \n")
        locadora.listar_clientes()
        
    elif escolha == "7":
        id = int(input("Digite o ID do filme: "))
        locadora.excluir_filme(id)
        print("Filme excluído com sucesso")
        
    elif escolha == "8":
        id = int(input("Digite o ID do cliente: "))
        locadora.excluir_cliente(id)
        print("Cliente excluído com sucesso")
        
    elif escolha == "0":
        print("Encerrando o programa...")
        break
    
    else:
        print("Por favor selecione uma opção válida!")