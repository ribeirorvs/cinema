filmes = []
cod_filme = 0

def _gerar_codigo():
    global cod_filme
    cod_filme += 1

def listar_filmes():
    return filmes

def cadastrar_filme(titulo, duracao, classificacao, diretor, distribuidora, status, genero):
    cod_filme = _gerar_codigo()
    filme = [cod_filme, titulo, duracao, classificacao, diretor, distribuidora, status, genero]
    filmes.append(filme)

def remover_todos_filmes():
    global filmes
    global cod_filme
    filmes = []
    cod_filme = 0
