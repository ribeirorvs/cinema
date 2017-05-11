from logica import filme
from logica import sala

sessoes = []
cod_sessao = 0

def _gerar_codigo():
	global cod_sessao
	cod_sessao += 1
	return cod_sessao

def listar_sessoes():
	return sessoes
	
def criar_sessao(cod_filme, cod_sala, horario):
	cod = _gerar_codigo()
	f = filme.buscar_filme(cod_filme)
	s = sala.buscar_sala(cod_sala)
	sessao = [cod, f, s, horario]
	sessoes.append(sessao)
	
def remover_todas_sessoes():
	global sessoes
	global cod_sessao
	
	sessoes = []
	cod_sessao = 0
	
def recuperar_sessao(cod_sessao):
	for s in sessoes:
		if(s[0] == cod_sessao):
			return s
	return None

def remover_sessao(cod_sessao):
	for s in sessoes:
		if(s[0] == cod_sessao):
			sessoes.remove(s)
			return True
	return False

