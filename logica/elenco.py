from logica import filme
from logica import ator


elencos = []

def listar_elencos():
	return elencos
	
def adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo):
	a = ator.buscar_ator(cod_ator)
	f = filme.buscar_filme(cod_filme)
	elenco = [cod_elenco, a, f, tipo]
	for i in range(len(elencos)):
		for j in range(len(elencos[i])):
			if(elencos[i][j][0] == cod_elenco):
				elencos[i].append(elenco)
				return True
	elencos.append([])
	elencos[len(elencos)-1].append(elenco)
	return True
		
def remover_todos_elencos():
	global elencos
	elencos = []
	
def buscar_elenco(cod_elenco):
	for i in range(len(elencos)):
		for j in range(len(elencos[i])):
			if(elencos[i][j][0] == cod_elenco):
				return elencos[i]
	return None
	
def remover_elenco(cod_elenco):
	for i in range(len(elencos)):
		for j in range(len(elencos[i])):
			if(elencos[i][j][0] == cod_elenco):
				elencos.remove(elencos[i])
				return True
	return False