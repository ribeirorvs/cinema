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

    def test_adicionar_dois_atores(self):
        ator.cadastrar_ator("Nome", "Nacionalidade", 20)
        ator.cadastrar_ator("Nome 2", "Nacionalidade 2", 22)

        atores = ator.listar_atores()

        self.assertEqual(2, len(atores))

    def test_buscar_ator(self):
        ator.cadastrar_ator("Nome", "Nacionalidade", 20)
        ator.cadastrar_ator("Nome 2", "Nacionalidade 2", 22)

        a = ator.buscar_ator(2)
        
        self.assertEqual("Nome 2", a[1])
        self.assertEqual("Nacionalidade 2", a[2])
        self.assertEqual(22, a[3])

    
    def test_remover_ator(self):
        ator.cadastrar_ator("Nome", "Nacionalidade", 20)
        ator.cadastrar_ator("Nome 2", "Nacionalidade 2", 22)

        ator.remover_ator(2)

        a = ator.buscar_ator(2)

        self.assertIsNone(a)


if __name__ == '__main__':
    unittest.main(exit=False)
