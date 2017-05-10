import unittest
from logica import filme

class TestFilme(unittest.TestCase):
    
    def test_sem_filme(self):
        filmes = filme.listar_filmes()

        self.assertEqual(0, len(filmes))

    def test_cadastrar_um_filme(self):
        filme.cadastrar_filme("titulo", "duração", "classificação", "diretor", "distribuidora", "status", "genero")

        atores = ator.listar_atores()

        self.assertEqual(1, len(atores))

        a = atores[0]

        self.assertEqual("titulo", a[1])
        self.assertEqual("duração", a[2])
        self.assertEqual("classificação", a[3])
        self.assertEqual("diretor", a[4])
        self.assertEqual("distribuidora", a[5])
        self.assertEqual("status", a[6])
        self.assertEqual("genero", a[7])
        

if __name__ == '__main__':
    unittest.main(exit=False)
