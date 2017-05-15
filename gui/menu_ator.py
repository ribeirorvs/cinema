from logica import ator

def imprimir_ator(ator):
	print("Codigo do ator: ", ator[0])
	print("Nome: ", ator[1])
	print("Nacionalidade: ", ator[2])
	print("Idade: ", ator[3])
	print()

def menu_cadastrar():
	print("\nCadastrar Ator\n")
	cod_ator = int(input("Codigo do ator: "))
	nome = input("Nome: ")
	nacionalidade = input("Nacionalidade: ")
	idade = int(input("Idade: "))
	ator.cadastrar_ator(cod_ator, nome, nacionalidade, idade)

def menu_listar():
	print("\nListar Atores\n")
	atores = ator.listar_atores()
	for a in atores:
		imprimir_ator(a)

def menu_buscar():
	print("\nBuscar Ator\n")
	cod_ator = int(input("Codigo do ator: "))
	print()
	a = ator.buscar_ator(cod_ator)
	if (a == None):
		print("Ator nao encontrado")
	else:
		imprimir_ator(a)

def menu_remover():
	print("\nRemover Ator\n")
	cod_ator = int(input("Codigo do ator: "))
	print()
	a = ator.remover_ator(cod_ator)
	if (a == False):
		print("Ator nao encontrado")
	else:
		print("Ator removido")

def mostrar_menu():
	menu = ("\n----------------\n"+
            "(1) Cadastrar novo Ator \n" +
            "(2) Listar Atores \n" +
            "(3) Buscar Ator por codigo \n" +
            "(4) Remover Ator \n" +
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