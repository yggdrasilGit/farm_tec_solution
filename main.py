import os
from display.display_principal import Menu
from enterprise_name import EnterpriseName

def limpar_tela():
    """Função para limpar a tela do terminal."""
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix (Linux/macOS)
        os.system('clear')

def main():
    """Função principal para iniciar o programa."""
    limpar_tela()
    enterprise = EnterpriseName()
    print(enterprise.display_company_name())  # Exibe o nome da empresa
    menu = Menu()
    menu.menu_principal()

if __name__ == "__main__":
    main()
