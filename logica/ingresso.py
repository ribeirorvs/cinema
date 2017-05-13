from logica import sessao

ingressos = []

def listar_ingressos_vendidos():
	return ingressos
	
def venda_ingresso_meia(cod_ingresso, cod_sessao):
	disponibilidade = sessao.verificar_lotacao(cod_sessao)
	
	if(disponibilidade > 0):
		sessao.diminuir_lotacao(cod_sessao)
		s = sessao.recuperar_sessao(cod_sessao)
		i = [s, "Meia"]
		ingressos.append(i)
	else:
		return False

def remover_todos_ingressos():
	global ingressos
	ingressos = []
	
def venda_ingresso_inteira(cod_ingresso, cod_sessao):
	disponibilidade = sessao.verificar_lotacao(cod_sessao)
	
	if(disponibilidade > 0):
		sessao.diminuir_lotacao(cod_sessao)
		s = sessao.recuperar_sessao(cod_sessao)
		i = [s, "Inteira"]
		ingressos.append(i)
	else:
		return False