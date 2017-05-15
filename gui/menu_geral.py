from gui import menu_ator
from logica import ator

def inicializar_dados():
	ator.iniciar_atores()
	
def mostrar_menu():
	inicializar_dados()
	
	menu = ("\n----------------\n"+
             "(1) Menu Ator \n" +
             "(2) Menu Sala \n" +
             "(3) Menu Filme \n" +
             "(4) Menu Elenco \n" +
             "(5) Menu Sessao \n" +
             "(6) Menu Ingresso \n" +
             "(0) Sair\n"+
            "----------------")
	
	while True:
		print(menu)
		
		option = int(input("Digite sua escolha: "))
		
		if(option == 1):
			menu_ator.mostrar_menu()
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
			print("Finalizando...")
			break
		else:
			print("Opcao invalido")