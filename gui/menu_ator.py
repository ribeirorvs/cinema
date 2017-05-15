from logica import ator

def menu_cadastrar():
	print("\nCadastrar Ator\n")
	cod_ator = int(input("Codigo do ator: "))
	nome = input("Nome: ")
	nacionalidade = input("Nacionalidade: ")
	idade = int(input("Idade: "))
	ator.cadastrar_ator(cod_ator, nome, nacionalidade, idade)

def mostrar_menu():
	menu = ("\n----------------\n"+
             "(1) Cadastrar novo Ator \n" +
             "(2) Listar Atores \n" +
             "(3) Buscar Ator por codigo \n" +
             "(4) Remover Ator \n" +
             "(5) Remover todos os Atores \n" +
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
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")