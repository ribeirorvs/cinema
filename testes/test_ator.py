import unittest
from logica import ator

class TestAtor(unittest.TestCase):


    def test_sem_ator(self):
        atores = ator.listar_atores()
        self.assertEqual(0, len(atores))

if __name__ == '__main__':
    unittest.main(exit=False)
