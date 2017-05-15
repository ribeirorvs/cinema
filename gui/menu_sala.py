from logica import sala

def menu_cadastrar():
	print("\nCadastrar Sala\n")
	cod_sala = int(input("Codigo da sala: "))
	lotacao = int(input("Lotacao maxima: "))
	sala.cadastrar_sala(cod_sala, lotacao)

def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Cadastrar nova Sala \n" +
            "(2) Listar Salas \n" +
            "(3) Buscar Sala por codigo \n" +
            "(4) Remover Sala \n" +
            "(5) Definir Sala  ocupada \n" +
            "(6) Definir Sala livre \n" +
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
		elif(option == 5):
			pass
		elif(option == 6):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")