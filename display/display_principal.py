from display.display_cadastro_cultura import MenuCultura
from display.display_area import MenuAreaPlantada

class Menu:
    def __init__(self):
        self # Acesso à classe que gerencia o cadastro de culturas
    
    def menu_principal(self):
        while True:
            # Exibe as opções do menu
            print("\nMenu Principal:")
            print("1. Tabalhar com Cultura")
            print("2. Tabalhar com Área de Plantio")
            print("3. Trabalhar com Insumo")
            print("0. Sair")
            
            # Solicita ao usuário para escolher uma opção
            opcao = input("Escolha uma opção (1, 0): ")
            
            if opcao == '1':
                MenuCultura().menu_cultura()   # Exibe a lista de culturas
            elif opcao == '2':
                MenuAreaPlantada().menu_area()
            elif opcao == '2':
                pass
            elif opcao == '0':
                print("\nSaindo\n")
                break # Exibe as culturas cadastradas
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")