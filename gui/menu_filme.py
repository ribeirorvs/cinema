from logica import filme


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
			pass
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