from logica import sessao

ingressos = []

def listar_ingressos():
	return ingressos
	
def venda_ingresso_meia(cod_ingresso, cod_sessao):
	disponibilidade = sessao.verificar_lotacao(cod_sessao)
	
	if(disponibilidade > 0):
		sessao.diminuir_lotacao(cod_sessao)
		s = sessao.recuperar_sessao(cod_sessao)
		i = [cod_ingresso, s, "Meia"]
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
		i = [cod_ingresso, s, "Inteira"]
		ingressos.append(i)
	else:
		return False

def listar_ingressos_vendidos(cod_sessao):
	vendidos = []
	for i in ingressos:
		if(i[1][0] == cod_sessao):
			vendidos.append(i)
	if(len(vendidos) > 0):
		return vendidos
	return None

def buscar_ingresso(cod_ingresso):
	for i in ingressos:
		if(i[0] == cod_ingresso):
			return i
	return None

def remover_ingresso(cod_ingresso):
	for i in ingressos:
		if(i[0] == cod_ingresso):
			ingressos.remove(i)
			return True
	return False