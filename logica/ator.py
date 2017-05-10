atores = []
cod_ator = 0
def _gerar_codigo():
    global cod_ator
    cod_ator += 1
    return cod_ator

def listar_atores():
    return atores

def cadastrar_ator(nome, nacionalidade, idade):
    cod = _gerar_codigo()
    ator = [cod, nome, nacionalidade, idade]
    atores.append(ator)

def buscar_ator(cod_ator):
    for i in atores:
        if(i[0] == cod_ator):
            return i
    return None

def remover_ator(cod_ator):
    for a in atores:
        if(a[0] == cod_ator):
            atores.remove(a)
            return True
    return False

def remover_todos_atores():
    global atores
    global cod_ator
    atores = []
    cod_ator = 0
    
def iniciar_atores():
    cadastrar_ator("Nome", "Nacionalidade", 20)
    cadastrar_ator("Nome 2", "Nacionalidade 2", 22)
