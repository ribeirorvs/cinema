elencos = []

def adicionar_ator(cod_elenco, cod_ator, cod_filme, tipo):
    a = cod_ator
    f = cod_filme
    elenco = [cod_elenco, cod_ator, cod_filme, tipo]
    for i in range(len(elencos)):
        for j in range(len(elencos[i])):
            if(elencos[i][j][0] == cod_elenco):
                elenco = [cod_elenco, a, f, tipo]
                elencos[i].append(elenco)
                return True
    elencos.append([])
    elenco = [cod_elenco, cod_ator, cod_filme, tipo]
    elencos[len(elencos)-1].append(elenco)
    return True

adicionar_ator(1, 1, 1, 0)
adicionar_ator(1, 1, 1, 0)
adicionar_ator(1, 1, 1, 0)
adicionar_ator(1, 1, 1, 0)
adicionar_ator(3, 1, 1, 10)
adicionar_ator(2, 1, 1, 10)

adicionar_ator(2, 1, 1, 20)

adicionar_ator(0, 1, 1, 30)
print(elencos)
