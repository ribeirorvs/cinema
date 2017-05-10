import unittest
from logica import ator

class TestAtor(unittest.TestCase):

    def setUp(self):
        ator.remover_todos_atores()

    def test_sem_ator(self):
        atores = ator.listar_atores()
        self.assertEqual(0, len(atores))

    def test_cadastrar_ator(self):
        ator.cadastrar_ator("Nome", "Nacionalidade", 20)

        atores = ator.listar_atores()
        self.assertEqual(1, len(atores))

        a = atores[0]

        self.assertEqual("Nome", a[1])
        self.assertEqual("Nacionalidade", a[2])
        self.assertEqual(20, a[3])

    

if __name__ == '__main__':
    unittest.main(exit=False)
