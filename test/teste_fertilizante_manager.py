import unittest
from manager.fertilizante_manager import Fertilizante
from manager.insumo_manage import Insumo
# Substitua pelo caminho correto para a sua classe

class TestFertilizante(unittest.TestCase):

    def setUp(self):
        # Configuração inicial dos testes
        self.fertilizante = Fertilizante(
            nome="Fertilizante A",
            descricao="Fertilizante orgânico de alta qualidade",
            quantidade=100,
            unidade="kg",
            preco_unitario=50.75,
            tipo="Orgânico",
            composicao="Nitrogênio, Fósforo, Potássio",
            dosagem_recomendada="5 kg por hectare"
        )

    def test_str(self):
        # Testa a representação em string da classe Fertilizante
        expected_str = "\n".join([
            "Fertilizante: Orgânico",
            "Composição: Nitrogênio, Fósforo, Potássio",
            "Nome: Fertilizante A",
            "Descrição: Fertilizante orgânico de alta qualidade",
            "Quantidade: 100 kg",
            "Dosagem recomendada: 5 kg por hectare",
            "Preço unitário: R$50.75"
        ])
        self.assertEqual(str(self.fertilizante), expected_str)

    def test_to_dict(self):
        # Testa a conversão de Fertilizante para um dicionário
        expected_dict = {
            "nome": "Fertilizante A",
            "descricao": "Fertilizante orgânico de alta qualidade",
            "quantidade": 100,
            "unidade": "kg",
            "preco_unitario": 50.75,
            "tipo": "Orgânico",
            "composicao": "Nitrogênio, Fósforo, Potássio",
            "dosagem_recomendada": "5 kg por hectare",
            "tipo_insumo": "fertilizante"
        }
        self.assertEqual(self.fertilizante.to_dict(), expected_dict)

    def test_heranca(self):
        # Testa se Fertilizante herda corretamente de Insumo
        self.assertTrue(issubclass(Fertilizante, Insumo))

if __name__ == "__main__":
    unittest.main()
