import unittest
from logica import sessao

class TestSessao(unittest.TestCase):
	
	def test_sem_sessao(self):
		sessoes = sessao.listar_sessoes()
		
		self.assertEqual(0, len(sessoes))
	
	
if __name__ == '__main__':
	unittest.main(exit=False)