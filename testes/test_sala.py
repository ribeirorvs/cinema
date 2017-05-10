import unittest
from logica import sala

class TestSala(unittest.TestCase):

	def test_sem_sala(self):
		salas = sala.listar_salas()
		self.assertEqual(0, len(salas))
		
	

if __name__ == '__main__':
	unittest.main(exit=False)
