from logica import elenco

def menu_adicionar():
	print("\nAdicionar ator no Elenco\n")
	cod_elenco = int(input("Codigo elenco: "))
	cod_ator = int(input("Codigo ator: "))
	cod_filme = int(input("Codigo filme: "))
	tipo = input("Tipo de ator: ")
	elenco.adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo)


def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Adicionar ator no Elenco \n" +
            "(2) Listar Elencos \n" +
            "(3) Buscar Elenco por codigo \n" +
            "(4) Buscar Elenco por filme \n" +
            "(5) Buscar Filmes por ator \n" +
            "(6) Remover Elenco \n" +
			"(0) Voltar\n"+
            "----------------")
	
	while True:
		print(menu)
		
		option = int(input("Digite sua escolha: "))
		
		if(option == 1):
			menu_adicionar()
		elif(option == 2):
			pass
		elif(option == 3):
			pass
		elif(option == 4):
			pass
		elif(option == 5):
			pass
		elif(option == 6):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")