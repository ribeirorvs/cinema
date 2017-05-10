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
    pass

def remover_ator(cod_ator):
    pass

def remover_todos_atores():
    pass

