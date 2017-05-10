import unittest
from logica import sala

class TestSala(unittest.TestCase):
	
	def setUp(self):
		sala.remover_todas_salas()
	
	def test_sem_sala(self):
		salas = sala.listar_salas()
		self.assertEqual(0, len(salas))
		
	def test_cadastrar_sala(self):
		sala.cadastrar_sala(200)
		
		salas = sala.listar_salas()
		
		self.assertEqual(1, len(salas))
		
		s = salas[0]
		
		self.assertEqual(200, s[1])

	def test_cadastrar_duas_salas(self):
		sala.cadastrar_sala(200)
		sala.cadastrar_sala(400)
		
		salas = sala.listar_salas()
		
		self.assertEqual(2, len(salas))
		
if __name__ == '__main__':
	unittest.main(exit=False)
