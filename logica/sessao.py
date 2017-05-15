from logica import filme
from logica import sala

sessoes = []
cod_sessao = 0

def listar_sessoes():
	return sessoes
	
def criar_sessao(cod_sessao, cod_filme, cod_sala, horario):
	f = filme.buscar_filme(cod_filme)
	s = sala.buscar_sala(cod_sala)
	disponibilidade = s
	sessao = [cod_sessao, f, s, horario, disponibilidade]
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

def iniciar_sessoes():
	criar_sessao(1, 1, 1, "18h")
	criar_sessao(2, 2, 2, "20h")
	
def verificar_lotacao(cod_sessao):
	for s in sessoes:
		if(s[0] == cod_sessao):
			return s[4][1]
	return None

def diminuir_lotacao(cod_sessao):
	global sessoes
	for i in range(len(sessoes)):
		if(sessoes[i][0] == cod_sessao):
			sessoes[i][4][1] -= 1
			return True
	return False