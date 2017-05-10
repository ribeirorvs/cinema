import unittest
from logica import sala

class TestSala(unittest.TestCase):

	def test_sem_sala(self):
		salas = sala.listar_salas()
		self.assertEqual(0, len(salas))
		
	def test_cadastrar_sala(self):
		sala.cadastrar_sala(200)
		
		salas = sala.listar_salas()
		
		self.assertEqual(1, len(salas))
		
		s = salas[0]
		
		self.assertEqual(200, s[1])

if __name__ == '__main__':
	unittest.main(exit=False)
