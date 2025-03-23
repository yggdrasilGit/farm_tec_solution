import json

class Cidade:
    """
    Representa uma cidade e permite operações básicas como exibição e salvamento de informações em JSON.
    """
    
    def __init__(self, nome: str):
        """
        Inicializa a cidade com o nome fornecido e adiciona ", Brasil" ao final.
        
        :param nome: Nome da cidade fornecida pelo usuário.
        """
        self.nome = nome.strip().title() + ", Brasil"
    
    def mostrar_cidade(self) -> str:
        """
        Retorna o nome formatado da cidade.
        
        :return: String com o nome da cidade formatado.
        """
        return f"A cidade informada é {self.nome}."
    
    def buscar_informacoes(self) -> str:
        """
        Simula a busca de informações sobre a cidade.
        
        :return: String informando que as informações estão sendo buscadas.
        """
        return f"Buscando informações sobre {self.nome}..."
    
    def salvar_em_json(self, diretorio: str = "dados/cidade.json") -> str:
        """
        Salva o nome da cidade em um arquivo JSON.
        
        :param diretorio: Caminho do arquivo onde os dados serão salvos. Padrão: "dados/cidade.json"
        :return: Caminho do arquivo salvo.
        """
        dados = {"cidade": self.nome}
        
        try:
            with open(diretorio, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return f"Informações salvas em {diretorio}"
        except Exception as e:
            return f"Erro ao salvar o arquivo: {e}"

# Exemplo de uso
#if __name__ == "__main__":
#    nome_cidade = input("Digite o nome da cidade: ")
#    cidade = Cidade(nome_cidade)
#    print(cidade.mostrar_cidade())
#    print(cidade.buscar_informacoes())
#    print(cidade.salvar_em_json())