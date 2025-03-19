import json
from tabulate import tabulate

class RelatorioAgricola:
    def __init__(self, arquivo_json):
        self.arquivo_json = arquivo_json
        self.resultados = self.carregar_dados()

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON"""
        with open(self.arquivo_json, "r", encoding="utf-8") as f:
            return json.load(f)

    def exibir_resultados(self):
        """Exibe os resultados de forma tabular"""
        if isinstance(self.resultados, list):  # Se há múltiplas culturas
            for resultado in self.resultados:
                self._exibir_cultura(resultado)
                print("\n" + "=" * 50)  # Linha separadora para culturas diferentes
        else:  # Se há apenas uma cultura
            self._exibir_cultura(self.resultados)

    def _exibir_cultura(self, resultado):
        """Exibe os dados de uma única cultura"""
        print("\n=== RESULTADO DO PLANEJAMENTO AGRÍCOLA ===\n")
        print(f"Cultura Selecionada: {resultado['cultura'].capitalize()}")
        print(f"Área Plantada: {resultado['area_plantada']:.2f} hectares\n")

        # Criar tabela de insumos
        tabela = [[insumo["insumo"], insumo["descricao"], f"{insumo['quantidade_necessaria']:.2f}", insumo["unidade"]]
                  for insumo in resultado["insumos_utilizados"]]

        # Exibir tabela formatada
        print(tabulate(tabela, headers=["Insumo", "Descrição", "Quantidade", "Unidade"], tablefmt="grid"))

# Executando a classe
if __name__ == "__main__":
     relatorio = RelatorioAgricola("dados/resultado.json")
     relatorio.exibir_resultados()
