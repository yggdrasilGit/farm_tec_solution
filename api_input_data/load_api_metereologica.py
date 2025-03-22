import rpy2.robjects as robjects
from pathlib import Path

class RClimateDataLoader:
    def __init__(self, nome_script="api_climatic.R"):
        self.script_path = self.encontrar_arquivo(nome_script)

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """Procura recursivamente por um arquivo dentro da estrutura do projeto."""
        raiz_busca = Path(raiz_busca).resolve()

        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                print(f"✅ Arquivo encontrado: {item}")
                return item

        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        return None

    def executar_script(self):
        """Executa o script R."""
        if not self.script_path:
            print("❌ Erro: Caminho do script R não definido.")
            return False

        print(f"📂 Executando script: {self.script_path}")
        try:
            robjects.r.source(str(self.script_path))  # Executa o script R
            print(f"✅ Script '{self.script_path.name}' executado com sucesso.")
            return True
        except Exception as e:
            print(f"❌ Erro ao executar o script R: {e}")
            return False

# Exemplo de uso:
if __name__ == "__main__":
    loader = RClimateDataLoader()
    loader.executar_script()
