import unittest

from manager.area_manager import AreaPlantada

class TestAreaPlantada(unittest.TestCase):
    def setUp(self):
        """ Configura um ambiente inicial para cada teste """
        self.area_plantada = AreaPlantada(areas_plantadas=[])
        self.area_plantada.adicionar_area("Milho", 10)
        self.area_plantada.adicionar_area("Soja", 15)
        self.area_plantada.adicionar_area("Feijão", 5)
        self.area_plantada.adicionar_area("Cana", 25)

    def test_adicionar_area(self):
        """ Testa a adição de uma nova área """
        self.area_plantada.adicionar_area("Trigo", 20)
        self.assertIn({'nome': 'Trigo', 'tamanho': 20}, self.area_plantada.areas_plantadas)

    def test_atualizar_area(self):
        """ Testa a atualização de uma área existente """
        self.area_plantada.atualizar_area("Soja", "Trigo", 20)
        self.assertIn({'nome': 'Trigo', 'tamanho': 20}, self.area_plantada.areas_plantadas)
        self.assertNotIn({'nome': 'Soja', 'tamanho': 15}, self.area_plantada.areas_plantadas)

    def test_remover_area(self):
        """ Testa a remoção de uma área """
        self.area_plantada.remover_area("Cana")
        self.assertNotIn({'nome': 'Cana', 'tamanho': 25}, self.area_plantada.areas_plantadas)

if __name__ == '__main__':
    unittest.main()
