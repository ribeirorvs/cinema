import unittest
from logica import elenco

class TestElenco(unittest.TestCase):
	
	def test_sem_elenco(self):
		elencos = elenco.listar_elenco()
		self.assertEqual(0, len(elencos))

		
		
if __name__ == '__main__':
	unittest.main(exit=False)