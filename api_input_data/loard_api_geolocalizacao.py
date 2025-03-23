import rpy2.robjects as robjects
from pathlib import Path
import json
from tabulate import tabulate


class RGeolocationLoader:
    """
    Classe para carregar e executar um script R de geolocalização e processar
    o arquivo JSON gerado contendo informações de latitude e longitude.
    """

    def __init__(self, nome_script="script_geolocalizacao.R"):
        """
        Inicializa a classe com o nome do script R.

        :param nome_script: Nome do script R a ser executado.
        """
        self.script_path = self.encontrar_arquivo(nome_script)
        self.json_path = None

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """
        Procura recursivamente por um arquivo dentro da estrutura do projeto.

        :param nome_arquivo: Nome do arquivo a ser encontrado.
        :param raiz_busca: Diretório raiz onde iniciar a busca.
        :return: Caminho do arquivo encontrado ou None se não encontrado.
        """
        raiz_busca = Path(raiz_busca).resolve()

        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                print(f"✅ Arquivo encontrado: {item}")
                return item

        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        return None

    def carregar_script(self):
        """
        Executa o script R e localiza o arquivo JSON gerado.

        :return: True se o script for executado e o arquivo JSON for encontrado,
                 False caso contrário.
        """
        if not self.script_path:
            print("❌ Erro: Script R não encontrado.")
            return False

        try:
            robjects.r.source(str(self.script_path))
            self.json_path = self.encontrar_arquivo("latitude_longitude.json")
            return bool(self.json_path)
        except Exception as e:
            print(f"❌ Erro ao executar o script R: {e}")
            return False

    def carregar_arquivo_json(self):
        """
        Lê o arquivo JSON gerado e exibe os dados em formato de tabela.

        :return: Dados extraídos do arquivo JSON ou None em caso de erro.
        """
        if not self.json_path:
            print("❌ Erro: Arquivo JSON não encontrado.")
            return None

        try:
            with self.json_path.open('r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            tabela = [
                [d["location"], d["lat"], d["long"]]
                for d in dados
            ]
            headers = ["Localização", "Latitude", "Longitude"]
            print("\n📊 Dados de Geolocalização")
            print(tabulate(tabela, headers=headers, tablefmt="grid"))
            print("\n")
            return dados
        except Exception as e:
            print(f"❌ Erro ao carregar JSON: {e}")
            return None

    def executar_geolocalizacao(self):
        """
        Executa o processo completo de geolocalização:
        - Executa o script R.
        - Carrega e exibe o arquivo JSON gerado.

        :return: Dados extraídos do JSON ou None se ocorrer algum erro.
        """
        if self.carregar_script():
            return self.carregar_arquivo_json()
        return None


# if __name__ == "__main__":
#    geo_loader = RGeolocationLoader()
#    geo_loader.executar_geolocalizacao()
