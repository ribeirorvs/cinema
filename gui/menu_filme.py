from logica import filme

def menu_cadastrar():
	print("\nCadastrar Filme\n")
	cod_filme = int(input("Codigo do filme: "))
	titulo = input("Titulo: ")
	duracao = input("Duracao: ")
	classificacao = input("Classificacao: ")
	diretor = input("Diretor: ")
	distribuidora = input("Distribuidora: ")
	status = input("Status: ")
	genero = input("Genero: ")
	filme.cadastrar_filme(cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero)

def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Cadastrar novo Filme \n" +
            "(2) Listar Filmes \n" +
            "(3) Buscar Filme por codigo \n" +
            "(4) Remover Filme \n" +
			"(0) Voltar\n"+
            "----------------")
	
	while True:
		print(menu)
		
		option = int(input("Digite sua escolha: "))
		
		if(option == 1):
			menu_cadastrar()
		elif(option == 2):
			pass
		elif(option == 3):
			pass
		elif(option == 4):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")