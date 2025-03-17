import json

class AreaPlantada:
    """
    Representa uma área plantada com culturas.
    
    Atributos:
        tipo_area (str): Tipo de área (não será alterado).
        areas_plantadas (list): Lista das áreas plantadas inseridas.
    """

    def __init__(self, areas_plantadas=None):
        if areas_plantadas is None:
            areas_plantadas = []  # Lista vazia por padrão
        self._tipo_area = "Tipo de Área Plantada"  # Tipo de área fixo
        self._areas_plantadas = areas_plantadas
        self.carregar_dados()  # Carrega os dados ao iniciar a classe
    
    def salvar_dados(self):
        """
        Salva os dados das áreas plantadas no arquivo JSON.
        """
        with open("dados/areas_plantadas.json", "w") as file:
            json.dump(self._areas_plantadas, file)
    
    def carregar_dados(self):
        """
        Carrega os dados das áreas plantadas a partir do arquivo JSON, se existir.
        """
        try:
            with open("dados/areas_plantadas.json", "r") as file:
                self._areas_plantadas = json.load(file)
        except FileNotFoundError:
            self._areas_plantadas = []  # Caso o arquivo não exista, inicializa com lista vazia

    @property
    def tipo_area(self):
        """
        Getter para o tipo de área (fixo, não pode ser alterado).
        """
        return self._tipo_area
    
    @property
    def areas_plantadas(self):
        """
        Getter para a lista de áreas plantadas.
        """
        return self._areas_plantadas
    
    @areas_plantadas.setter
    def areas_plantadas(self, lista):
        """
        Setter para a lista de áreas plantadas.
        """
        if isinstance(lista, list):
            self._areas_plantadas = lista
        else:
            raise ValueError("areas_plantadas deve ser uma lista.")
    
    def __str__(self):
        return f"{self._tipo_area}: {self._areas_plantadas}"
    
    def adicionar_area(self, nome_area, tamanho):
        """
        Permite adicionar uma nova área plantada.
        """
        # Verifica se o tamanho da área é válido
        try:
            tamanho_area = float(tamanho)  # Converte o tamanho para número
            if tamanho_area <= 0:
                print("O tamanho da área deve ser maior que zero.")
                return  # Sai da função se o tamanho for inválido
        except ValueError:
            print("Por favor, insira um número válido para o tamanho da área.")
            return  # Sai da função se o tamanho não for válido

            # Adiciona a nova área à lista
        self.areas_plantadas.append({'nome': nome_area, 'tamanho': tamanho_area})
        self.salvar_dados()  # Salva os dados após adicionar
        print(f"Área '{nome_area}' com tamanho {tamanho_area} hectares adicionada!")

    
    def atualizar_area(self):
        """
        Permite ao usuário atualizar uma área plantada existente.
        """
        while True:
            print("Áreas plantadas atuais:", self.areas_plantadas)
            area_antiga = input("Digite o nome da área que deseja atualizar (ou digite 'sair' para finalizar): ")
            if area_antiga.lower() == 'sair':
                print("Atualização de áreas plantadas finalizada.")
                break  # Sai do loop se o usuário digitar 'sair'
            # Verifica se a área existe na lista
            area_encontrada = next((area for area in self.areas_plantadas if area['nome'] == area_antiga), None)
            if not area_encontrada:
                print(f"A área '{area_antiga}' não existe na lista.")
                continue  # Continua a pedir se a área não estiver na lista
            novo_nome = input(f"Digite o novo nome para a área '{area_antiga}': ")
            novo_tamanho = input(f"Digite o novo tamanho da área '{novo_nome}' em hectares: ")
            try:
                novo_tamanho = float(novo_tamanho)  # Converte o tamanho para número
                if novo_tamanho <= 0:
                    print("O tamanho da área deve ser maior que zero.")
                    continue  # Recomeça o loop caso o tamanho seja inválido
            except ValueError:
                print("Por favor, insira um número válido para o tamanho da área.")
                continue  # Recomeça o loop caso o tamanho não seja válido
            # Atualiza a área na lista
            indice = self.areas_plantadas.index(area_encontrada)
            self.areas_plantadas[indice] = {'nome': novo_nome, 'tamanho': novo_tamanho}
            self.salvar_dados()  # Salva os dados após atualizar
            print(f"A área '{area_antiga}' foi atualizada para '{novo_nome}' com {novo_tamanho} hectares.")
    
    def remover_area(self):
        """
        Permite ao usuário remover uma área plantada existente.
        """
        while True:
            print("Áreas plantadas atuais:", self.areas_plantadas)
            area_a_remover = input("Digite o nome da área que deseja remover (ou digite 'sair' para finalizar): ")
            if area_a_remover.lower() == 'sair':
                print("Remoção de áreas plantadas finalizada.")
                break  # Sai do loop se o usuário digitar 'sair'
            # Verifica se a área existe na lista
            area_encontrada = next((area for area in self.areas_plantadas if area['nome'] == area_a_remover), None)
            if not area_encontrada:
                print(f"A área '{area_a_remover}' não existe na lista.")
                continue  # Continua a pedir se a área não estiver na lista
            self.areas_plantadas.remove(area_encontrada)  # Remove a área da lista
            self.salvar_dados()  # Salva os dados após remover
            print(f"A área '{area_a_remover}' foi removida.")
    
    def mostrar_areas(self):
        """
        Exibe as áreas plantadas.
        """
        if self.areas_plantadas:
            print(f"{self._tipo_area}:")
            for area in self.areas_plantadas:
                print(f"Nome: {area['nome']}, Tamanho: {area['tamanho']} hectares")
        else:
            print("Nenhuma área plantada registrada.")

# Exemplo de uso:
# area_plantada = AreaPlantada()
# area_plantada.mostrar_areas()  # Exibe as áreas plantadas no início
# area_plantada.adicionar_area()  # Adiciona uma nova área plantada
# area_plantada.atualizar_area()  # Atualiza uma área existente
# area_plantada.remover_area()  # Remove uma área existente

