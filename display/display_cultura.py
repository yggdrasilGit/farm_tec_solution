import json
from tabulate import tabulate

class RelatorioAgricola:
    """
    Classe responsável por gerar e exibir relatórios agrícolas
    a partir de um arquivo JSON contendo os dados das culturas.
    """
    
    def __init__(self, arquivo_json):
        """
        Inicializa a classe carregando os dados do arquivo JSON.
        
        :param arquivo_json: Caminho do arquivo JSON com os dados agrícolas.
        """
        self.arquivo_json = arquivo_json
        self.resultados = self.carregar_dados()

    def carregar_dados(self):
        """
        Carrega os dados do arquivo JSON.
        
        :return: Dados carregados do arquivo JSON.
        """
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar o arquivo JSON: {e}")
            return []

    def exibir_resultados(self):
        """
        Exibe os resultados do planejamento agrícola em formato tabular.
        """
        if not self.resultados:
            print("Nenhum dado disponível para exibição.")
            return
        
        if isinstance(self.resultados, list):  # Se há múltiplas culturas
            for resultado in self.resultados:
                self._exibir_cultura(resultado)
                print("\n" + "=" * 50)  # Linha separadora para culturas diferentes
        else:  # Se há apenas uma cultura
            self._exibir_cultura(self.resultados)

    def _exibir_cultura(self, resultado):
        """
        Exibe os dados de uma única cultura em formato tabular.
        
        :param resultado: Dicionário contendo os dados da cultura.
        """
        print("\n=== RESULTADO DO PLANEJAMENTO AGRÍCOLA ===\n")
        print(f"Cultura Selecionada: {resultado.get('cultura', 'Desconhecida').capitalize()}")
        print(f"Área Plantada: {resultado.get('area_plantada', 0):.2f} hectares\n")

        # Criar tabela de insumos
        insumos = resultado.get("insumos_utilizados", [])
        tabela = [[insumo.get("insumo", "N/A"), insumo.get("descricao", "N/A"), 
                   f"{insumo.get('quantidade_necessaria', 0):.2f}", insumo.get("unidade", "N/A")]
                  for insumo in insumos]

        # Exibir tabela formatada
        print(tabulate(tabela, headers=["Insumo", "Descrição", "Quantidade", "Unidade"], tablefmt="grid"))

# Executando a classe
# if __name__ == "__main__":
#   relatorio = RelatorioAgricola("dados/resultado.json")
#    relatorio.exibir_resultados()
