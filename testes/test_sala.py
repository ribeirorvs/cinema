import unittest
from logica import sala

class TestSala(unittest.TestCase):
	
	def setUp(self):
		sala.remover_todas_salas()
	
	def test_sem_sala(self):
		salas = sala.listar_salas()
		self.assertEqual(0, len(salas))
		
	def test_cadastrar_sala(self):
		sala.cadastrar_sala(1, 200)
		
		salas = sala.listar_salas()
		
		self.assertEqual(1, len(salas))
		
		s = salas[0]
		
		self.assertEqual(200, s[1])
		self.assertEqual("Livre", s[2])

	def test_cadastrar_duas_salas(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		salas = sala.listar_salas()
		
		self.assertEqual(2, len(salas))
	
	def test_buscar_sala(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		s = sala.buscar_sala(2)
		
		self.assertEqual(400, s[1])
		self.assertEqual("Livre", s[2])
		
	def test_remover_sala(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		sala.remover_sala(2)
		
		s = sala.buscar_sala(2)
		
		self.assertIsNone(s)
		
	def test_remover_todas_salas(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		sala.remover_todas_salas()
		
		s = sala.listar_salas()
		
		self.assertEqual(0, len(s))
	
	def test_iniciar_salas(self):
		sala.iniciar_salas()
		salas = sala.listar_salas()
		
		self.assertEqual(2, len(salas))
		
	def test_definir_status_ocupada(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		sala.definir_status_ocupada(2)
		
		s = sala.buscar_sala(2)
		
		self.assertEqual("Ocupada", s[2])
	
	def test_definir_status_livre(self):
		sala.cadastrar_sala(1, 200)
		sala.cadastrar_sala(2, 400)
		
		sala.definir_status_ocupada(2)
		
		s = sala.buscar_sala(2)
		
		self.assertEqual("Ocupada", s[2])
		
		sala.definir_status_livre(2)
		
		s = sala.buscar_sala(2)
		
		self.assertEqual("Livre", s[2])
	
	
if __name__ == '__main__':
	unittest.main(exit=False)
