from logica import sessao

def imprimir_sessao(sessao):
	print("Codigo Sessao: ", sessao[0])
	print("Filme: ", sessao[1])
	print("Sala: ", sessao[2][0])
	print("Horario: ", sessao[3])
	print("Lotacao: ", sessao[4][1])
	print()
	
def menu_criar():
	print("\nCriar Sessao\n")
	cod_sessao = int(input("Codigo Sessao: "))
	cod_filme = int(input("Codigo Filme: "))
	cod_sala = int(input("Codigo Sala: "))
	horario = input("Horario: ")
	sessao.criar_sessao(cod_sessao, cod_filme, cod_sala, horario)

def menu_listar():
	print("\nListar Sessoes\n")
	
	sessoes = sessao.listar_sessoes()
	for s in sessoes:
		imprimir_sessao(s)
	
def menu_buscar():
	print("\nBuscar Sessao\n")
	cod_sessao = int(input("Codigo Sessao: "))
	print()
	s = sessao.recuperar_sessao(cod_sessao)
	if(s == None):
		print("Sessao nao encontrada")
	else:
		imprimir_sessao(s)

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
			menu_listar()
		elif(option == 3):
			menu_buscar()
		elif(option == 4):
			pass
		elif(option == 5):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")