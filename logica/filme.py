filmes = []
cod_filmes = 0

def _gerar_codigo():
    global cod_filmes
    cod_filmes += 1
    return cod_filmes

def listar_filmes():
    return filmes

def cadastrar_filme(titulo, duracao, classificacao, diretor, distribuidora, status, genero):
    cod_filme = _gerar_codigo()
    filme = [cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero]
    filmes.append(filme)

def remover_todos_filmes():
    global filmes
    global cod_filmes
    filmes = []
    cod_filmes = 0

def buscar_filme(cod_filme):
    for f in filmes:
        if(f[0] == cod_filme):
            return f
    return None
