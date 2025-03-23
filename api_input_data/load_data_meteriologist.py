import json
from pathlib import Path
from tabulate import tabulate


class MeteorologistDataLoader:
    """
    Classe para carregar e exibir dados meteorológicos a partir de um arquivo JSON.

    Atributos:
        json_path (Path): Caminho para o arquivo JSON encontrado no projeto.

    Métodos:
        encontrar_arquivo(nome_arquivo, raiz_busca): Procura recursivamente por um arquivo JSON
                                                    dentro da estrutura do projeto.
        carregar_arquivo_json(): Carrega e exibe os dados do arquivo JSON em formato de tabela.
    """

    def __init__(self, nome_arquivo_json):
        """
        Inicializa a classe MeteorologistDataLoader, procurando pelo arquivo JSON especificado.

        Args:
            nome_arquivo_json (str): Nome do arquivo JSON a ser procurado.
        """
        self.json_path = self.encontrar_arquivo(nome_arquivo_json)

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """
        Procura recursivamente por um arquivo dentro da estrutura do projeto.

        Args:
            nome_arquivo (str): Nome do arquivo JSON a ser procurado.
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

    def carregar_arquivo_json(self):
        """
        Lê e exibe os dados do arquivo JSON gerado.

        Retorna:
            dict: Dados climáticos extraídos do JSON ou None se houver erro no arquivo.
        
        Levanta:
            JSONDecodeError: Caso haja um erro ao decodificar o JSON.
        """
        if not self.json_path:
            print("❌ Erro: Arquivo JSON não encontrado.")
            return None

        print(f"📂 Caminho do arquivo JSON: {self.json_path}")
        try:
            with self.json_path.open('r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            if not isinstance(dados, list) or not dados:
                print("❌ Erro: O JSON não contém uma lista válida de dados.")
                return None

            # Pegando o primeiro elemento da lista
            clima = dados[0]

            # Criando uma tabela formatada
            tabela = [
                ["Cidade", clima["Cidade"]],
                ["País", clima["Pais"]],
                ["Latitude", clima["Latitude"]],
                ["Longitude", clima["Longitude"]],
                ["Temperatura (°C)", clima["Temperatura"]],
                ["Sensação Térmica (°C)", clima["Sensacao_Termica"]],
                ["Temperatura Mínima (°C)", clima["Temp_Minima"]],
                ["Temperatura Máxima (°C)", clima["Temp_Maxima"]],
                ["Pressão Atmosférica (hPa)", clima["Pressao_Atmosferica"]],
                ["Umidade (%)", clima["Umidade"]],
                ["Visibilidade (m)", clima["Visibilidade"]],
                ["Velocidade do Vento (m/s)", clima["Velocidade_do_Vento"]],
                ["Direção do Vento (°)", clima["Direcao_do_Vento"]],
                ["Cobertura de Nuvens (%)", clima["Cobertura_de_Nuvens"]],
                ["Descrição do Clima", clima["Descricao_do_Clima"]],
                ["Tipo de Clima", clima["Tipo_de_Clima"]],
                ["Nascer do Sol", clima["Nascer_do_Sol"]],
                ["Pôr do Sol", clima["Por_do_Sol"]],
                ["Fuso Horário (s)", clima["Fuso_Horario"]],
            ]

            headers = ["Parâmetro", "Valor"]
            print("\n📊 Dados Meteorológicos\n")
            print(tabulate(tabela, headers=headers, tablefmt="grid"))
            print("\n")

            return clima
        except json.JSONDecodeError as e:
            print(f"❌ Erro ao decodificar o arquivo JSON: {e}")
            return None
        except Exception as e:
            print(f"❌ Erro ao carregar o arquivo JSON: {e}")
            return None


# Exemplo de uso:
# if __name__ == "__main__":
#     nome_arquivo = "clima_portugues.json"  # Nome do arquivo JSON
#     loader = MeteorologistDataLoader(nome_arquivo)
#     dados_clima = loader.carregar_arquivo_json()
