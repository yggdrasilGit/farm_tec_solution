import rpy2.robjects as robjects
from pathlib import Path
import json
from tabulate import tabulate


class RScriptLoader:
    """
    Classe para carregar e executar scripts R, além de processar arquivos JSON
    gerados após a execução do script.

    Atributos:
        script_path (Path): Caminho do arquivo de script R.
        json_path (Path): Caminho do arquivo JSON gerado pelo script R.
    """

    def __init__(self, nome_script):
        """
        Inicializa a classe com o nome do script R.

        Args:
            nome_script (str): Nome do arquivo de script R a ser carregado e executado.
        """
        self.script_path = self.encontrar_arquivo(nome_script)
        self.json_path = None  # Será definido após a execução do script

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """
        Procura recursivamente por um arquivo dentro da estrutura do projeto.

        Args:
            nome_arquivo (str): Nome do arquivo a ser procurado.
            raiz_busca (str): Caminho raiz onde a busca será iniciada. O padrão é o diretório atual.

        Returns:
            Path: Caminho do arquivo encontrado ou None caso não seja encontrado.
        
        Levanta:
            FileNotFoundError: Se o arquivo não for encontrado após a busca.
        """
        raiz_busca = Path(raiz_busca).resolve()

        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                return item

        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        return None

    def carregar_script(self):
        """
        Executa o script R se ele existir.

        Returns:
            bool: True se o script R for executado corretamente e o arquivo JSON for encontrado.
                  False se ocorrer algum erro durante a execução do script.
        
        Levanta:
            RuntimeError: Se houver um erro durante a execução do script R.
        """
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
        """
        Lê e exibe os dados do arquivo JSON gerado pelo R.

        Returns:
            dict: Dados carregados do arquivo JSON ou None caso ocorra erro no carregamento.
        
        Levanta:
            JSONDecodeError: Se houver erro na decodificação do arquivo JSON.
        """
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
        except json.JSONDecodeError as e:
            print(f"❌ Erro ao decodificar o arquivo JSON: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro ao carregar o arquivo JSON: {e}")
            return None

    def chamar_estatistica(self):
        """
        Configura e executa os scripts R e processa os dados JSON gerados.

        Returns:
            dict: Dados estatísticos extraídos do arquivo JSON ou None se ocorrer erro.
        """
        sucesso = self.carregar_script()

        if sucesso:
            return self.carregar_arquivo_json()
        else:
            print("❌ Falha na execução do script R.")
            return None


# Exemplo de como usar a classe
# script_loader = RScriptLoader("R/script_statis.R")
# dados_estatisticos = script_loader.chamar_estatistica()
