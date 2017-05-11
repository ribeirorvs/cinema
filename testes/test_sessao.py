import unittest
from logica import sessao
from logica import sala
from logica import filme

class TestSessao(unittest.TestCase):
	
	def setUp(self):
		sala.iniciar_salas()
		filme.iniciar_filmes()
		sessao.remover_todas_sessoes()
	
	def test_sem_sessao(self):
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(0, len(sessoes))
	
	def test_criar_uma_sessao(self):
		sessao.criar_sessao(1, 1, "18h")
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(1, len(sessoes))
		
		s = sessoes[0]
		salas = sala.buscar_sala(1)
		filmes = filme.buscar_filme(1)
		self.assertEqual(1, s[0])
		self.assertEqual(filmes, s[1])
		self.assertEqual(salas, s[2])
		self.assertEqual("18h", s[3])
	
	def test_criar_duas_sessoes(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(2, len(sessoes))
		
		s = sessoes[1]
		salas = sala.buscar_sala(2)
		filmes = filme.buscar_filme(2)
		self.assertEqual(2, s[0])
		self.assertEqual(filmes, s[1])
		self.assertEqual(salas, s[2])
		self.assertEqual("20h", s[3])
	
	def test_recuperar_sessao(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		s = sessao.recuperar_sessao(2)
		salas = sala.buscar_sala(2)
		filmes = filme.buscar_filme(2)
		self.assertEqual(2, s[0])
		self.assertEqual(filmes, s[1])
		self.assertEqual(salas, s[2])
		self.assertEqual("20h", s[3])
	
	def test_remover_sessao(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		sessao.remover_sessao(2)
		
		s = sessao.recuperar_sessao(2)
		
		self.assertIsNone(s)
	
	def test_remover_todas_sessoes(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		sessao.remover_todas_sessoes()
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(0, len(sessoes))
	
	def test_iniciar_sessaoes(self):
		sessao.iniciar_sessoes()
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(2, len(sessoes))
	
	def test_verificar_lotacao(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		s = sessao.verificar_lotacao(2)
		salas = sala.buscar_sala(2)
		self.assertEqual(salas[1], s[1])
	
if __name__ == '__main__':
	unittest.main(exit=False)