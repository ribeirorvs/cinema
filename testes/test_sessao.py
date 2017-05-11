import unittest
from logica import sessao

class TestSessao(unittest.TestCase):
	
	def setUp(self):
		sessao.remover_todos_ingressos()
	
	def test_sem_sessao(self):
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(0, len(sessoes))
	
	def test_criar_uma_sessao(self):
		sessao.criar_sessao(1, 1, "18h")
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(1, len(sessoes))
		
		s = sessoes[0]
		
		self.assertEqual(1, s[0])
		self.assertEqual(None, s[1])
		self.assertEqual(None, s[2])
		self.assertEqual("18h", s[3])
	
	def test_criar_duas_sessoes(self):
		sessao.criar_sessao(1, 1, "18h")
		sessao.criar_sessao(2, 2, "20h")
		
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(2, len(sessoes))
		
		s = sessoes[1]
		
		self.assertEqual(2, s[0])
		self.assertEqual(None, s[1])
		self.assertEqual(None, s[2])
		self.assertEqual("20h", s[3])
	
if __name__ == '__main__':
	unittest.main(exit=False)