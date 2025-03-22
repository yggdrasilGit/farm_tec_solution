import json
from pathlib import Path
from tabulate import tabulate

class MeteorologistDataLoader:
    def __init__(self, nome_arquivo_json):
        self.json_path = self.encontrar_arquivo(nome_arquivo_json)

    def encontrar_arquivo(self, nome_arquivo, raiz_busca="."):
        """Procura recursivamente por um arquivo dentro da estrutura do projeto."""
        raiz_busca = Path(raiz_busca).resolve()

        for item in raiz_busca.rglob(nome_arquivo):
            if item.is_file():
                print(f"✅ Arquivo encontrado: {item}")
                return item

        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado dentro de {raiz_busca}")
        return None

    def carregar_arquivo_json(self):
        """Lê e exibe os dados do arquivo JSON gerado."""
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
        except Exception as e:
            print(f"❌ Erro ao carregar o arquivo JSON: {e}")
            return None



# Exemplo de uso:
if __name__ == "__main__":
    nome_arquivo = "clima_portugues.json"  # Nome do arquivo JSON
    loader = MeteorologistDataLoader(nome_arquivo)
    dados_clima = loader.carregar_arquivo_json()
