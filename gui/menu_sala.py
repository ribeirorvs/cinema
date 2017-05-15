from logica import sala

def imprimir_sala(sala):
	print("Codigo da sala: ", sala[0])
	print("Lotacao maxima: ", sala[1])
	print()

def menu_cadastrar():
	print("\nCadastrar Sala\n")
	cod_sala = int(input("Codigo da sala: "))
	lotacao = int(input("Lotacao maxima: "))
	sala.cadastrar_sala(cod_sala, lotacao)

def menu_listar():
	print("\nListar Salas\n")
	salas = sala.listar_salas()
	print()
	for s in salas:
		imprimir_sala(s)

def menu_buscar():
	print("\nBuscar Sala\n")
	cod_sala = int(input("Codigo da sala: "))
	print()
	s = sala.buscar_sala(cod_sala)
	if(s == None):
		print("Sala nao encontrada")
	else:
		imprimir_sala(s)

def menu_remover():
	print("\nRemover Sala\n")
	cod_sala = int(input("Codigo da sala: "))
	print()
	s = sala.remover_sala(cod_sala)
	if(s == False):
		print("Sala nao encontrada")
	else:
		print("Sala removida")

def menu_status_ocupada():
	print("\nDefinir Sala ocupada\n")
	cod_sala = int(input("Codigo da sala: "))
	print()
	s = sala.definir_status_ocupada(cod_sala)
	if(s == False):
		print("Sala nao encontrada ou já ocupada")
	else:
		print("Status da sala alterado para ocupada")

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
			menu_listar()
		elif(option == 3):
			menu_buscar()
		elif(option == 4):
			menu_remover()
		elif(option == 5):
			menu_status_ocupada()
		elif(option == 6):
			pass
		elif(option == 0):
			print("Retornando ao menu principal...")
			break
		else:
			print("Opcao invalida...")