import unittest
from unittest.mock import patch, mock_open
from io import StringIO

from manager.culture_manager import Cultura
# Substitua pelo caminho correto para a sua classe

class TestCultura(unittest.TestCase):
    def setUp(self):
        # Configuração inicial dos testes
        self.cultura = Cultura()

    @patch("builtins.open", new_callable=mock_open, read_data="['Soja', 'Milho']")
    def test_carregar_dados(self, mock_file):
        # Testa o carregamento de dados do arquivo
        cultura = Cultura()  # Carrega o arquivo (mockado)
        self.assertEqual(cultura._coluna_de_culturas, ['Soja', 'Milho'])
        mock_file.assert_called_once_with("dados/culturas.json", "r")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_carregar_dados_arquivo_vazio(self, mock_file):
        # Testa o comportamento ao carregar um arquivo vazio
        cultura = Cultura()  # Carrega o arquivo vazio (mockado)
        self.assertEqual(cultura._coluna_de_culturas, [])
        mock_file.assert_called_once_with("dados/culturas.json", "r")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["Arroz", "sair"])
    def test_adicionar_cultura(self, mock_input, mock_file):
        # Testa a adição de uma cultura
        self.cultura.adicionar_cultura()
        self.assertIn("Arroz", self.cultura._coluna_de_culturas)
        mock_file.assert_called_once_with("dados/culturas.json", "w", encoding="utf-8")
        mock_file().write.assert_called_with('["Arroz"]\n')

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["Soja", "Cevada", "sair"])
    def test_atualizar_cultura(self, mock_input, mock_file):
        # Testa a atualização de uma cultura
        self.cultura._coluna_de_culturas = ["Soja", "Milho"]
        self.cultura.atualizar_cultura()
        self.assertIn("Cevada", self.cultura._coluna_de_culturas)
        self.assertNotIn("Soja", self.cultura._coluna_de_culturas)
        mock_file.assert_called_once_with("dados/culturas.json", "w", encoding="utf-8")
        mock_file().write.assert_called_with('["Cevada", "Milho"]\n')

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["Milho", "sair"])
    def test_remover_cultura(self, mock_input, mock_file):
        # Testa a remoção de uma cultura
        self.cultura._coluna_de_culturas = ["Soja", "Milho"]
        self.cultura.remover_cultura()
        self.assertNotIn("Milho", self.cultura._coluna_de_culturas)
        mock_file.assert_called_once_with("dados/culturas.json", "w", encoding="utf-8")
        mock_file().write.assert_called_with('["Soja"]\n')

    @patch("builtins.print")
    def test_mostrar_culturas(self, mock_print):
        # Testa a exibição das culturas
        self.cultura._coluna_de_culturas = ["Soja", "Milho"]
        self.cultura.mostrar_culturas()
        mock_print.assert_called_once_with("Tipos de Cultura: Soja, Milho")

    @patch("builtins.print")
    def test_mostrar_culturas_vazio(self, mock_print):
        # Testa a exibição quando não há culturas
        self.cultura._coluna_de_culturas = []
        self.cultura.mostrar_culturas()
        mock_print.assert_called_once_with("Nenhuma cultura cadastrada.")

if __name__ == "__main__":
    unittest.main()
