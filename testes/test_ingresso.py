import unittest
from logica import ingresso

class TestIngresso(unittest.TestCase):
	
	def test_sem_ingresso(self):
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(0, len(ingressos))
	
	def test_venda_um_ingresso_meia(self):
		ingressos = ingresso.venda_ingresso_meia(1)
		
		self.assertEqual(1, len(i))

		i = ingressos[0]
		
		self.assertEqual(1, i[0])


if __name__ == '__main__':
	unittest.main(exit=False)