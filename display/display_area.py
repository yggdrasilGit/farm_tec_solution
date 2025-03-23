from calculo.calcular_area import CalculadoraAreaCultura
from manager.area_manager import AreaPlantada

class MenuAreaPlantada:
    """
    Classe responsável por gerenciar o menu das áreas plantadas.
    Permite calcular, visualizar, atualizar e remover áreas de plantio.
    """
    
    def __init__(self):
        """
        Inicializa a classe com uma instância de AreaPlantada e CalculadoraAreaCultura.
        """
        self.area_plantada = AreaPlantada()
        self.calculadora = CalculadoraAreaCultura()
    
    def menu_area(self):
        """
        Exibe o menu interativo para o usuário e executa as ações escolhidas.
        """
        while True:
            print("\nMenu das Áreas Plantadas:")
            print("1. Calcular Área de Plantio")
            print("2. Visualizar Áreas Plantadas")
            print("3. Atualizar Área Plantada")
            print("4. Remover Área Plantada")
            print("0. Sair")
            
            opcao = input("Escolha uma opção (0-4): ").strip()
            
            if opcao == '1':
                self.calcular()
            elif opcao == '2':
                self.visualizar()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.remover()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
    
    def calcular(self):
        """
        Realiza o cálculo da área de plantio e adiciona à lista de áreas plantadas.
        """
        try:
            resultado = self.calculadora.executar()
            if isinstance(resultado, tuple) and len(resultado) == 2:
                self.area_plantada.adicionar_area(resultado[0], resultado[1])
                print("Área adicionada com sucesso!")
            else:
                print("Erro: O cálculo da área retornou um formato inválido.")
        except Exception as e:
            print(f"Erro ao calcular a área: {e}")
    
    def visualizar(self):
        """
        Exibe as áreas plantadas cadastradas.
        """
        print(f"{self.area_plantada.tipo_area}: {self.area_plantada.areas_plantadas}")
    
    def atualizar(self):
        """
        Atualiza uma área plantada existente.
        """
        try:
            self.area_plantada.atualizar_area()
            print("Área atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar a área: {e}")
    
    def remover(self):
        """
        Remove uma área plantada da lista.
        """
        try:
            self.area_plantada.remover_area()
            print("Área removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover a área: {e}")
