salas = []
cod_sala = 0

def _gerar_codigo():
	global cod_sala
	cod_sala +=1
	return cod_sala

def listar_salas():
	return salas

def cadastrar_sala(lotacao):
	cod = _gerar_codigo()
	sala = [cod, lotacao]
	salas.append(sala)
	
def remover_todas_salas():
	global salas
	global cod_sala
	salas = []
	cod_sala = 0
	
def buscar_sala(cod_sala):
	for s in salas:
		if(s[0] == cod_sala):
			return s
	return None