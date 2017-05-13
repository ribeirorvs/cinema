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
		self.assertEqual("Meia", ingressos[0][1])

		i = ingressos[0][0]
	
		sessoes = sessao.recuperar_sessao(1)
		
		self.assertEqual(sessoes, i)
	# def test_venda_dois_ingressos_meia(self):
		# ingresso.venda_ingresso_meia(1, 1)
		# ingresso.venda_ingresso_meia(2, 2)
		
		# ingressos = ingresso.listar_ingressos()
		
		# self.assertEqual(2, len(ingressos))
		
		# i = ingressos[1]
		
		# sessoes = sessao.recuperar_sessao(2)
		
		# self.assertEqual(sessoes, i)
	
	# def test_venda_um_ingresso_inteira(self):
		# ingresso.venda_ingresso_inteira(1, 1)
		
		# ingressos = ingresso.listar_ingressos()
		
		# self.assertEqual(1, len(ingressos))
		
		# i = ingressos[0]
		
		# sessoes = sessao.recuperar_sessao(1)
		
		# self.assertEqual(sessoes, i)
	
if __name__ == '__main__':
	unittest.main(exit=False)