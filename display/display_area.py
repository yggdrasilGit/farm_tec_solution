# Importando a classe AreaPlantada de manager.area_plantada_manager
from calculo.calcular_area import CalculadoraAreaCultura
from manager.area_manager import AreaPlantada

class MenuAreaPlantada:
    def __init__(self):
        # Inicializando a área plantada com uma lista vazia de áreas
        self.area_plantada = AreaPlantada()  # Tipo de área fixo
        self.calculadora = CalculadoraAreaCultura()
    
    def menu_area(self):
        while True:
            # Exibe as opções do menu
            print("\nMenu das Áreas Plantadas:")
            print("1. Calcular Área de Plantio")
            print("2. Visualizar Áreas Plantadas")
            print("3. Atualizar Área Plantada")
            print("4. Remover Área Plantada")
            print("0. Sair")
            
            # Solicita ao usuário para escolher uma opção
            opcao = input("Escolha uma opção (1, 2 ou 3): ")
            
            if opcao == '1':
                self.calculador()  # Cadastra nova área
            elif opcao == '2':
                self.printt()  # Exibe as áreas plantadas cadastradas
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.remover()
            elif opcao == '0':
                print("Saindo...")
                break  # Sai do loop, encerrando o programa
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
    
    def atualizar(self):
        self.area_plantada.atualizar_area()
    
    def remover(self):
        self.area_plantada.remover_area()
    
    def printt(self):
        # Exibindo as áreas plantadas cadastradas
        print(f"{self.area_plantada.tipo_area}: {self.area_plantada.areas_plantadas}")
    
    def calculador(self):
        executar = self.calculadora.executar() 
        print(executar)
        self.area_plantada.adicionar_area(executar[0], executar[1])
