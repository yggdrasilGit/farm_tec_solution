import rpy2.robjects as robjects
from pathlib import Path
import json
from tabulate import tabulate

class RGeolocationLoader:
    def __init__(self, nome_script="script_geolocalizacao.R"):
        self.script_path = self.encontrar_arquivo(nome_script)
        self.json_path = None

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        raiz_busca = Path(raiz_busca).resolve()
        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                return item
        return None

    def carregar_script(self):
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
        if not self.json_path:
            print("❌ Erro: Arquivo JSON não encontrado.")
            return None
        try:
            with self.json_path.open('r') as arquivo:
                dados = json.load(arquivo)
            print(tabulate([[d["location"], d["lat"], d["long"]] for d in dados], 
                           headers=["Localização", "Latitude", "Longitude"], tablefmt="grid"))
            return dados
        except Exception as e:
            print(f"❌ Erro ao carregar JSON: {e}")
            return None

    def executar_geolocalizacao(self):
        if self.carregar_script():
            return self.carregar_arquivo_json()
        return None

if __name__ == "__main__":
    geo_loader = RGeolocationLoader()
    geo_loader.executar_geolocalizacao()

