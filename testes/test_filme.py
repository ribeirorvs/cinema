import unittest
from logica import filme

class TestFilme(unittest.TestCase):
    
    def test_sem_filme(self):
        filmes = filme.listar_filmes()

        self.assertEqual(0, len(filmes))



if __name__ == '__main__':
    unittest.main(exit=False)
