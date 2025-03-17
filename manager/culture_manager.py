import json

class Cultura:
    def __init__(self):
        self._tipo_de_cultura = "Tipos de Cultura"
        self._coluna_de_culturas = self.carregar_dados()  # Tenta carregar os dados do arquivo

    def salvar_dados(self):
        # Salva os dados no arquivo JSON
        with open("dados/culturas.json", "w") as file:
            json.dump(self._coluna_de_culturas, file)
    
    def carregar_dados(self):
        # Carrega os dados do arquivo JSON, se existir
        try:
            with open("dados/culturas.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Retorna uma lista vazia caso o arquivo não exista

    def adicionar_cultura(self):
        while True:
            nova_cultura = input("Cadastre a nova cultura (ou 'sair' para voltar): ")
            if nova_cultura.lower() == 'sair':
                break
            self._coluna_de_culturas.append(nova_cultura)
            self.salvar_dados()  # Salva os dados após adicionar a cultura
            print(f"Cultura '{nova_cultura}' adicionada!")

    def atualizar_cultura(self):
        while True:
            if not self._coluna_de_culturas:
                print("Não há culturas cadastradas ainda.")
                break
            print("Culturas atuais:", self._coluna_de_culturas)
            cultura_antiga = input("Digite a cultura que deseja atualizar (ou 'sair' para voltar): ")
            if cultura_antiga.lower() == 'sair':
                break
            if cultura_antiga not in self._coluna_de_culturas:
                print(f"A cultura '{cultura_antiga}' não existe na lista.")
                continue
            nova_cultura = input(f"Digite o novo nome para a cultura '{cultura_antiga}': ")
            indice = self._coluna_de_culturas.index(cultura_antiga)
            self._coluna_de_culturas[indice] = nova_cultura
            self.salvar_dados()  # Salva os dados após atualizar a cultura
            print(f"Cultura '{cultura_antiga}' atualizada para '{nova_cultura}'.")

    def remover_cultura(self):
        while True:
            if not self._coluna_de_culturas:
                print("Não há culturas cadastradas ainda.")
                break
            print("Culturas atuais:", self._coluna_de_culturas)
            cultura_a_remover = input("Digite a cultura que deseja remover (ou 'sair' para voltar): ")
            if cultura_a_remover.lower() == 'sair':
                break
            if cultura_a_remover not in self._coluna_de_culturas:
                print(f"A cultura '{cultura_a_remover}' não existe na lista.")
                continue
            self._coluna_de_culturas.remove(cultura_a_remover)
            self.salvar_dados()  # Salva os dados após remover a cultura
            print(f"Cultura '{cultura_a_remover}' removida.")

    def mostrar_culturas(self):
        # Exibe as culturas cadastradas
        if self._coluna_de_culturas:
            print(f"{self._tipo_de_cultura}: {', '.join(self._coluna_de_culturas)}")
        else:
            print("Nenhuma cultura cadastrada.")

# Exemplo de uso:
# cultura = Cultura()
# cultura.mostrar_culturas()  # Exibe as culturas no início
# cultura.adicionar_cultura()  # Adiciona uma nova cultura
# cultura.atualizar_cultura()  # Atualiza uma cultura existente
# cultura.remover_cultura()  # Remove uma cultura existente
