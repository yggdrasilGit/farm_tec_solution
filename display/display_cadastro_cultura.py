# Importando a classe Cultura de manager.culture_manager
from manager.culture_manager import Cultura

class MenuCultura:
    def __init__(self):
        # Inicializando a cultura com uma lista vazia de culturas
        self.cultura = Cultura()  # Tipo de cultura fixo
    
    def menu_cultura(self):
        while True:
            # Exibe as opções do menu
            print("\nMenu das culturas:")
            print("1. Cadastrar Cultura")
            print("2. Visualizar Culturas")
            print("3. Atualizar Culturas")
            print("4. Remover Culturas")
            print("0. Sair")
            
            # Solicita ao usuário para escolher uma opção
            opcao = input("Escolha uma opção (1, 2 ou 3): ")
            
            if opcao == '1':
                self.cadastro()  # Adiciona cultura
            elif opcao == '2':
                self.visualizar() # Exibe as culturas cadastradas
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.remover()
            elif opcao == '0':
                print("Saindo...")
                break  # Sai do loop, encerrando o programa
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

    def cadastro(self):
        self.cultura.adicionar_cultura()
    
    def atualizar(self):
        self.cultura.atualizar_cultura()
    
    def remover(self):
        self.cultura.remover_cultura()
    
    def visualizar(self):
        self.cultura.mostrar_culturas()