import unittest
from logica import elenco

class TestElenco(unittest.TestCase):
	
	def setUp(self):
		elenco.remover_todos_elencos()
	
	def test_sem_elenco(self):
		elencos = elenco.listar_elencos()
		self.assertEqual(0, len(elencos))

	def test_adicionar_ator(self):
		elenco.adicionar_ator(0, 1, 1, "Coadjuvante")
		elencos = elenco.listar_elencos()
		
		e = elencos[0]
		
		##Verifica a quantidade de elencos
		self.assertEqual(1, len(elencos))
		
		##Verifica a quantidade de atores no elenco
		self.assertEqual(1, len(elencos[0]))
		
		self.assertEqual(0, e[0][0])
	
	def test_adicionar_dois_atores_mesmo_elenco(self):
		elenco.adicionar_ator(0, 1, 1, "Coadjuvante")
		elenco.adicionar_ator(0, 2, 1, "Principal")
		
		elencos = elenco.listar_elencos()
		
		##Verifica a quantidade de elencos
		self.assertEqual(1, len(elencos))
		
		##Verifica a quantidade de atores no elenco
		self.assertEqual(2, len(elencos[0]))
		
		e = elencos[0][1]
		
		self.assertEqual("Principal", e[3])
		
	def test_buscar_elenco(self):
		elenco.adicionar_ator(0, 1, 1, "Coadjuvante")
		elenco.adicionar_ator(0, 2, 1, "Principal")
		
		e = elenco.buscar_elenco(0)
		
		e1 = e[0]
		e2 = e[1]
		
		self.assertEqual(0, e1[0])
		self.assertEqual("Coadjuvante", e1[3])
		
		self.assertEqual(0, e2[0])
		self.assertEqual("Principal", e2[3])
		
	def test_listar_elenco(self):
		elenco.adicionar_ator(0, 1, 1, "Coadjuvante")
		elenco.adicionar_ator(0, 2, 1, "Principal")
		
		elencos = elenco.listar_elencos()
		
		self.assertEqual(1, len(elencos))
		self.assertEqual(2, len(elencos[0]))
	
if __name__ == '__main__':
	unittest.main(exit=False)