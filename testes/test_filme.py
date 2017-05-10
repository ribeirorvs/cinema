import unittest
from logica import filme

class TestFilme(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()

    def test_sem_filme(self):
        filmes = filme.listar_filmes()

        self.assertEqual(0, len(filmes))

    def test_cadastrar_um_filme(self):
        filme.cadastrar_filme("titulo", "duração", "classificação", "diretor", "distribuidora", "status", "genero")

        filmes = filme.listar_filmes()

        self.assertEqual(1, len(filmes))

        f = filmes[0]
        
        self.assertEqual("titulo", f[1])
        self.assertEqual("duração", f[2])
        self.assertEqual("classificação", f[3])
        self.assertEqual("diretor", f[4])
        self.assertEqual("distribuidora", f[5])
        self.assertEqual("status", f[6])
        self.assertEqual("genero", f[7])
        
    def test_adicionar_dois_filmes(self):
        filme.cadastrar_filme("titulo", "duração", "classificação", "diretor", "distribuidora", "status", "genero")
        filme.cadastrar_filme("titulo 2", "duração 2", "classificação 2", "diretor 2", "distribuidora 2", "status 2", "genero 2")

        filmes = filme.listar_filmes()

        self.assertEqual(2, len(filmes))        

    def test_buscar_filme(self):
        filme.cadastrar_filme("titulo", "duração", "classificação", "diretor", "distribuidora", "status", "genero")
        filme.cadastrar_filme("titulo 2", "duração 2", "classificação 2", "diretor 2", "distribuidora 2", "status 2", "genero 2")

        f = filme.buscar_filme(2)

        self.assertEqual("titulo 2", f[1])
        self.assertEqual("duração 2", f[2])
        self.assertEqual("classificação 2", f[3])
        self.assertEqual("diretor 2", f[4])
        self.assertEqual("distribuidora 2", f[5])
        self.assertEqual("status 2", f[6])
        self.assertEqual("genero 2", f[7])
    
if __name__ == '__main__':
    unittest.main(exit=False)
