import unittest
from manager.adubo_manager import Adubo


class TestAdubo(unittest.TestCase):
    def setUp(self):
        # Criando um objeto Adubo para os testes
        self.adubo = Adubo("Composto Orgânico", "Adubo orgânico para enriquecer o solo", 50, "kg", "Orgânico", "Granulado", "300g/m²")

    def test_atributos(self):
        # Verifica se os atributos foram corretamente atribuídos
        self.assertEqual(self.adubo.nome, "Composto Orgânico")
        self.assertEqual(self.adubo.descricao, "Adubo orgânico para enriquecer o solo")
        self.assertEqual(self.adubo.quantidade, 50)
        self.assertEqual(self.adubo.unidade, "kg")
        self.assertEqual(self.adubo.tipo, "Orgânico")
        self.assertEqual(self.adubo.forma_aplicacao, "Granulado")
        self.assertEqual(self.adubo.dosagem_recomendada, "300g/m²")

    def test_verificar_dosagem(self):
        # Testa se o método verificar_dosagem retorna corretamente a dosagem recomendada
        self.assertEqual(self.adubo.verificar_dosagem(), "Dosagem recomendada: 300g/m²")
    
    def test_str(self):
        # Testa a representação em string da classe
        esperado = "Adubo: Orgânico, Forma de Aplicação: Granulado, Adubo orgânico para enriquecer o solo, Dosagem recomendada: 300g/m²"
        self.assertIn("Adubo: Orgânico", str(self.adubo))  # Teste parcial para evitar dependência do super().__str__()

if __name__ == "__main__":
    unittest.main()
