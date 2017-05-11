from logica import filme
from logica import sala

sessoes = []
cod_sessao = 0

def _gerar_codigo():
	global cod_sessao
	cod_sessao += 1

def listar_sessoes():
	return sessoes
	
def criar_sessao(cod_filme, cod_sessao, horario):
	cod = _gerar_codigo()
	s = [cod, cod_filme, cod_sessao, horario]
	sessoes.append(s)