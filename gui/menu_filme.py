from logica import filme

def imprimir_filme(filme):
	print("Codigo do filme: ", filme[0])
	print("Titulo: ", filme[1])
	print("Duracao: ", filme[2])
	print("Classificacao: ", filme[3])
	print("Diretor: ", filme[4])
	print("Distribuidora: ", filme[5])
	print("Status: ", filme[6])
	print("Genero: ", filme[7])
	print()

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

def menu_listar():
	print("\nListar Filmes\n")
	filmes = filme.listar_filmes()
	for f in filmes:
		imprimir_filme(f)
	
def menu_buscar():
	print("\nBuscar Filme\n")
	cod_filme = int(input("Codigo do filme: "))
	print()
	f = filme.buscar_filme(cod_filme)
	if(f == None):
		print("Filme nao encontrado")
	else:
		imprimir_filme(f)
	
def menu_remover():
	print("\nRemover Filme\n")
	cod_filme = int(input("Codigo do filme: "))
	print()
	f = filme.remover_filme(cod_filme)
	if(f == False):
		print("Filme nao encontrado")
	else:
		print("Filme removido")

	
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
			menu_listar()
		elif(option == 3):
			menu_buscar()
		elif(option == 4):
			menu_remover()
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")