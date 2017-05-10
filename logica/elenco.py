from logica import filme
from logica import ator


elencos = []

def listar_elenco():
	return elencos
	
def adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo):
	a = ator.buscar_ator(cod_ator)
	f = filme.buscar_filme(cod_filme)
	elenco = [cod_elenco, cod_ator, cod_filme, tipo]
	for i in elencos:
		if(i[0] == cod_elenco):
			elenco = [a, f]
			elencos[cod_elenco] = elenco
			return True
	elenco = [cod_elenco, cod_ator, cod_filme, tipo]
	elencos.append(elenco)
	return True