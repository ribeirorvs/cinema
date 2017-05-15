from logica import ingresso

def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Vender ingresso Meia \n" +
            "(2) Vender ingresso Inteira \n" +
            "(3) Buscar Ingresso \n" +
            "(4) Remover Ingresso \n" +
            "(5) Listar ingressos por Sessao \n" +
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
		elif(option == 5):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")