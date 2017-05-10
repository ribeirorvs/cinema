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

        a = filmes[0]

        self.assertEqual("titulo", a[1])
        self.assertEqual("duração", a[2])
        self.assertEqual("classificação", a[3])
        self.assertEqual("diretor", a[4])
        self.assertEqual("distribuidora", a[5])
        self.assertEqual("status", a[6])
        self.assertEqual("genero", a[7])
        
    def test_adicionar_dois_filmes(self):
        filme.cadastrar_filme("titulo", "duração", "classificação", "diretor", "distribuidora", "status", "genero")
        filme.cadastrar_filme("titulo 2", "duração 2", "classificação 2", "diretor 2", "distribuidora 2", "status 2", "genero 2")

        filmes = filme.listar_filmes()

        self.assertEqual(2, len(filmes))        
        
if __name__ == '__main__':
    unittest.main(exit=False)
