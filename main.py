from display.display_principal import Menu

import os

def limpar_tela():
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix (Linux/macOS)
        os.system('clear')

if __name__ == "__main__":
    # Instanciando o menu e testando as funcionalidades
    menu = Menu()
    menu.menu_principal()
    limpar_tela()


