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