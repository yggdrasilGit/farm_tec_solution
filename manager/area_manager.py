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

        
    def atualizar_area(self, area_antiga=None, novo_nome=None, novo_tamanho=None):
        """
        Atualiza uma área plantada existente.
        Se os parâmetros não forem fornecidos, solicita entrada do usuário.
        """
        if area_antiga is None:
            area_antiga = input("Digite o nome da área que deseja atualizar: ").strip().lower()
        
        area_encontrada = next((area for area in self.areas_plantadas if area['nome'] == area_antiga), None)
        if not area_encontrada:
            print(f"A área '{area_antiga.title()}' não existe na lista.")
            return

        if novo_nome is None:
            novo_nome = input(f"Digite o novo nome para a área '{area_antiga.title()}': ").strip().lower()
        
        if novo_tamanho is None:
            try:
                novo_tamanho = float(input(f"Digite o novo tamanho da área '{novo_nome.title()}': "))
                if novo_tamanho <= 0:
                    print("O tamanho da área deve ser maior que zero.")
                    return
            except ValueError:
                print("Por favor, insira um número válido para o tamanho da área.")
                return

        indice = self.areas_plantadas.index(area_encontrada)
        self.areas_plantadas[indice] = {'nome': novo_nome, 'tamanho': novo_tamanho}
        self.salvar_dados()
        
        print(f"A área '{area_antiga.title()}' foi atualizada para '{novo_nome.title()}' com {novo_tamanho} hectares.")


    def remover_area(self, area_a_remover=None):
        """
        Remove uma área plantada existente.
        Se o nome não for fornecido, solicita entrada do usuário.
        """
        if area_a_remover is None:
            area_a_remover = input("Digite o nome da área que deseja remover: ")

        area_encontrada = next((area for area in self.areas_plantadas if area['nome'] == area_a_remover), None)
        if not area_encontrada:
            print(f"A área '{area_a_remover}' não existe na lista.")
            return

        self.areas_plantadas.remove(area_encontrada)
        self.salvar_dados()
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

