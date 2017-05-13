import unittest
from logica import ingresso
from logica import sessao
from logica import sala
from logica import filme


class TestIngresso(unittest.TestCase):
	
	def setUp(self):
		sala.iniciar_salas()
		filme.iniciar_filmes()
		sessao.iniciar_sessoes()
		ingresso.remover_todos_ingressos()
	
	def test_sem_ingresso(self):
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(0, len(ingressos))
	
	def test_venda_um_ingresso_meia(self):
		ingresso.venda_ingresso_meia(1, 1)
		
		ingressos = ingresso.listar_ingressos()
		self.assertEqual(1, len(ingressos))
		self.assertEqual("Meia", ingressos[0][2])
		i = ingressos[0][1]
	
		sessoes = sessao.recuperar_sessao(1)
		
		self.assertEqual(sessoes, i)
	def test_venda_dois_ingressos_meia(self):
		ingresso.venda_ingresso_meia(1, 1)
		ingresso.venda_ingresso_meia(2, 2)
		
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(2, len(ingressos))
		self.assertEqual("Meia", ingressos[1][2])
		i = ingressos[1][1]
		
		sessoes = sessao.recuperar_sessao(2)
		
		self.assertEqual(sessoes, i)
	
	def test_venda_um_ingresso_inteira(self):
		ingresso.venda_ingresso_inteira(1, 1)
		
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(1, len(ingressos))
		self.assertEqual("Inteira", ingressos[0][2])
		i = ingressos[0][1]
		
		sessoes = sessao.recuperar_sessao(1)
		
		self.assertEqual(sessoes, i)
	
	def test_venda_dois_ingressos_inteira(self):
		ingresso.venda_ingresso_inteira(1, 1)
		ingresso.venda_ingresso_inteira(2, 2)
		
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(2, len(ingressos))
		self.assertEqual("Inteira", ingressos[1][2])
		
		i = ingressos[1][1]
		
		sessoes = sessao.recuperar_sessao(2)
		
		self.assertEqual(sessoes, i)
		
	def test_listar_ingressos_vendidos(self):
		ingresso.venda_ingresso_inteira(1, 1)
		ingresso.venda_ingresso_inteira(2, 2)
		ingresso.venda_ingresso_meia(3, 1)
		ingresso.venda_ingresso_meia(4, 2)
		
		ingressos = ingresso.listar_ingressos_vendidos(1)
		
		self.assertEqual(2, len(ingressos))
	
	def test_listar_ingressos(self):
		ingresso.venda_ingresso_inteira(1, 1)
		ingresso.venda_ingresso_inteira(2, 2)
		ingresso.venda_ingresso_meia(3, 1)
		ingresso.venda_ingresso_meia(4, 2)
		
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(4, len(ingressos))
	
	def test_buscar_ingresso(self):
		ingresso.venda_ingresso_inteira(1, 1)
		ingresso.venda_ingresso_inteira(2, 2)
		ingresso.venda_ingresso_meia(3, 1)
		ingresso.venda_ingresso_meia(4, 2)
		
		i = ingresso.buscar_ingresso(3)
		
		self.assertEqual(3, i[0])
		
		s = sessao.recuperar_sessao(1)
		
		self.assertEqual(s, i[1])
		self.assertEqual("Meia", i[2])
	
if __name__ == '__main__':
	unittest.main(exit=False)