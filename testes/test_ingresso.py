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
	
	def test_sem_ingresso(self):
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(0, len(ingressos))
	
	def test_venda_um_ingresso_meia(self):
		ingresso.venda_ingresso_meia(1)
		
		ingressos = ingresso.listar_ingressos()
		
		self.assertEqual(1, len(ingressos))

		i = ingressos[0]
		
		self.assertEqual(1, i[0])


if __name__ == '__main__':
	unittest.main(exit=False)