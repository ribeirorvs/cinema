from logica import sessao

def menu_criar():
	print("\nCriar Sessao\n")
	cod_sessao = int(input("Codigo Sessao: "))
	cod_filme = int(input("Codigo Filme: "))
	cod_sala = int(input("Codigo Sala: "))
	horario = input("Horario: ")
	sessao.criar_sessao(cod_sessao, cod_filme, cod_sala, horario)

def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Criar nova Sessao \n" +
            "(2) Listar Sessoes \n" +
            "(3) Buscar Sessao \n" +
            "(4) Remover Sessao \n" +
            "(5) Verificar Lotacao \n" +
			"(0) Voltar\n"+
            "----------------")
	
	while True:
		print(menu)
		
		option = int(input("Digite sua escolha: "))
		
		if(option == 1):
			menu_criar()
		elif(option == 2):
			pass
		elif(option == 3):
			pass
		elif(option == 4):
			pass
		elif(option == 5):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")