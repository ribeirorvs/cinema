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
	sala = [cod, lotacao, "Livre"]
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
	
def remover_sala(cod_sala):
	for s in salas:
		if(s[0] == cod_sala):
			salas.remove(s)
			return True
	return False
	
def iniciar_salas():
	cadastrar_sala(200)
	cadastrar_sala(400)
	
def definir_status_ocupada(cod_sala):
	for i in range(len(salas)):
		if(salas[i][0] == cod_sala):
			salas[i][2] = "Ocupada"
			return True
	return False

def definir_status_livre(cod_sala):
	for i in range(len(salas)):
		if(salas[i][0] == cod_sala):
			salas[i][2] = "Livre"
			return True
	return False