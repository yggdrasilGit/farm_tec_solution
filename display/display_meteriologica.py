import json

class Cidade:
    def __init__(self, nome):
        self.nome = nome + ", Brasil"
    
    def mostrar_cidade(self):
        return f"A cidade informada é {self.nome}."
    
    # Método para expandir a funcionalidade, como buscar informações sobre a cidade
    def buscar_informacoes(self):
        return f"Buscando informações sobre {self.nome}..."
    
    def salvar_em_json(self):
        diretorio = "dados/cidade.json"
        
        dados = {"cidade": self.nome}


        with open(diretorio, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        
        return diretorio  # Retorna o caminho salvo

# Exemplo de uso
# nome_cidade = input("Digite o nome da cidade: ")
# cidade = Cidade(nome_cidade)
# print(cidade.mostrar_cidade())
# print(cidade.buscar_informacoes())

# Salvar no arquivo JSON e exibir o caminho salvo
# caminho_arquivo = cidade.salvar_em_json()
# print(f"Informações salvas em {caminho_arquivo}")

