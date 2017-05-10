import unittest
from logica import elenco

class TestElenco(unittest.TestCase):
	
	def test_sem_elenco(self):
		elencos = elenco.listar_elenco()
		self.assertEqual(0, len(elencos))

	def test_adicionar_ator(self):
		elenco.adicionar_ator(1, 1, 1, "Coadjuvante")
		elencos = elenco.listar_elenco()
		
		e = elencos[0]
		
		self.assertEqual(1, len(elencos))
		self.assertEqual(1, e[0])
		
if __name__ == '__main__':
	unittest.main(exit=False)