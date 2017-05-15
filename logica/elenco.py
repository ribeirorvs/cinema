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
	
def iniciar_elencos():
	adicionar_ator(0, 1, 1, "Coadjuvante")
	adicionar_ator(0, 2, 1, "Principal")
	adicionar_ator(1, 1, 1, "Coadjuvante")
	adicionar_ator(1, 2, 1, "Principal")
	
def buscar_elenco_por_filme(cod_filme):
	e = []
	for i in range(len(elencos)):
		for j in range(len(elencos[i])):
			if(elencos[i][j][2][0] == cod_filme):
				e.append(elencos[i])
	return e
	
def buscar_filmes_por_ator(cod_ator):
	e = []
	for i in range(len(elencos)):
		for j in range(len(elencos[i])):
			if(elencos[i][j][1][0] == cod_ator):
				e.append(elencos[i])
	return e