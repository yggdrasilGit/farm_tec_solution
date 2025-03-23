import rpy2.robjects as robjects
from pathlib import Path
import json
from tabulate import tabulate

class RScriptLoader:
    """
    Classe para carregar e executar scripts R, além de processar arquivos JSON
    gerados após a execução do script.
    """
    
    def __init__(self, nome_script):
        """Inicializa a classe com o nome do script R."""
        self.script_path = self.encontrar_arquivo(nome_script)
        self.json_path = None  # Definido depois da execução do script

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """Procura recursivamente por um arquivo dentro da estrutura do projeto."""
        raiz_busca = Path(raiz_busca).resolve()

        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                return item

        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        return None

    def carregar_script(self):
        """Executa o script R se ele existir."""
        if not self.script_path:
            print("❌ Erro: Caminho do script R não definido.")
            return False

        try:
            robjects.r.source(str(self.script_path))  # Executa o script R
            
            # Encontrar o arquivo JSON gerado após execução do script
            self.json_path = self.encontrar_arquivo("dados/estatistica.json")
            if self.json_path:
                return True
            else:
                print("❌ Erro: Arquivo JSON não encontrado após execução do script.")
                return False
        except Exception as e:
            print(f"❌ Erro ao carregar o script R: {e}")
            return False

    def carregar_arquivo_json(self):
        """Lê e exibe os dados do arquivo JSON gerado pelo R."""
        if not self.json_path:
            print("❌ Erro: Arquivo JSON não encontrado após execução do script.")
            return None

        try:
            with self.json_path.open('r') as arquivo:
                dados = json.load(arquivo)

            # Exibir dados formatados em tabela
            tabela = [[chave, valores["media"][0], valores["desvio_padrao"][0]] 
                      for chave, valores in dados.items()]

            headers = ["Parâmetro", "Média", "Desvio Padrão"]
            print("\n📊 Dados estatísticos das áreas plantadas")
            print(tabulate(tabela, headers=headers, tablefmt="grid"))
            print("\n")

            return dados
        except Exception as e:
            print(f"❌ Erro ao carregar o arquivo JSON: {e}")
            return None

    def chamar_estatistica(self):
        """Configura e executa os scripts R e processa os dados JSON gerados."""
        sucesso = self.carregar_script()

        if sucesso:
            return self.carregar_arquivo_json()
        else:
            print("❌ Falha na execução do script R.")
            return None

# Exemplo de como usar a classe
# script_loader = RScriptLoader("R/script_statis.R")
# dados_estatisticos = script_loader.carregar_script()
