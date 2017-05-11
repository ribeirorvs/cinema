import unittest
from logica import ingresso

class TestIngresso(unittest.TestCase):
	
	def test_sem_ingresso(self):
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(0, len(ingressos))





if __name__ == '__main__':
	unittest.main(exit=False)