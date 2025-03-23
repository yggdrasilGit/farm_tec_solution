from manager.culture_manager import Cultura

class MenuCultura:
    """
    Classe responsável por gerenciar o menu de culturas.
    Permite cadastrar, visualizar, atualizar e remover culturas.
    """
    
    def __init__(self):
        """
        Inicializa a classe com uma instância de Cultura.
        """
        self.cultura = Cultura()
    
    def menu_cultura(self):
        """
        Exibe o menu interativo para o usuário e executa as ações escolhidas.
        """
        while True:
            print("\nMenu das Culturas:")
            print("1. Cadastrar Cultura")
            print("2. Visualizar Culturas")
            print("3. Atualizar Cultura")
            print("4. Remover Cultura")
            print("0. Sair")
            
            opcao = input("Escolha uma opção (0-4): ").strip()
            
            if opcao == '1':
                self.cadastrar()
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
    
    def cadastrar(self):
        """
        Adiciona uma nova cultura.
        """
        try:
            self.cultura.adicionar_cultura()
            print("Cultura cadastrada com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar cultura: {e}")
    
    def atualizar(self):
        """
        Atualiza uma cultura existente.
        """
        try:
            self.cultura.atualizar_cultura()
            print("Cultura atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar cultura: {e}")
    
    def remover(self):
        """
        Remove uma cultura cadastrada.
        """
        try:
            self.cultura.remover_cultura()
            print("Cultura removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover cultura: {e}")
    
    def visualizar(self):
        """
        Exibe todas as culturas cadastradas.
        """
        try:
            self.cultura.mostrar_culturas()
        except Exception as e:
            print(f"Erro ao visualizar culturas: {e}")