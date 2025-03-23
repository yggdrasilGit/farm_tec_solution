import rpy2.robjects as robjects
from pathlib import Path


class RClimateDataLoader:
    """
    Classe para carregar e executar scripts R relacionados a dados climáticos.
    
    Esta classe busca e executa um script R dentro de um diretório ou estrutura
    de diretórios fornecida, utilizando a biblioteca rpy2 para interagir com o R.
    
    Atributos:
        script_path (Path): Caminho para o script R encontrado no projeto.
    
    Métodos:
        encontrar_arquivo(nome_arquivo, raiz_busca): Procura recursivamente por um arquivo
                                                  R na estrutura do projeto.
        executar_script(): Executa o script R encontrado utilizando rpy2.
    """

    def __init__(self, nome_script="api_climatic.R"):
        """
        Inicializa a classe RClimateDataLoader, procurando pelo script R especificado.
        
        Args:
            nome_script (str): Nome do script R a ser procurado. O padrão é "api_climatic.R".
        """
        self.script_path = self.encontrar_arquivo(nome_script)

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """
        Procura recursivamente por um arquivo dentro da estrutura do projeto.
        
        Args:
            nome_arquivo (str): Nome do arquivo R a ser procurado.
            raiz_busca (str): Caminho raiz onde a busca será iniciada. O padrão é o diretório atual.
        
        Returns:
            Path: Caminho do arquivo encontrado ou None caso não seja encontrado.
        
        Levanta:
            FileNotFoundError: Caso o arquivo não seja encontrado após a busca.
        """
        raiz_busca = Path(raiz_busca).resolve()

        try:
            for item in raiz_busca.rglob(nome_arquivo):
                if item.is_file():
                    print(f"✅ Arquivo encontrado: {item}")
                    return item
            raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        except Exception as e:
            print(f"❌ Erro durante a busca do arquivo: {e}")
            return None

    def executar_script(self):
        """
        Executa o script R encontrado.

        Retorna:
            bool: True se o script foi executado com sucesso, False caso contrário.
        
        Levanta:
            RuntimeError: Caso haja falha na execução do script R.
        """
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
            raise RuntimeError(f"Falha na execução do script R: {e}")
            return False


# Exemplo de uso:
# if __name__ == "__main__":
#     loader = RClimateDataLoader()
#     loader.executar_script()
