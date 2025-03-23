from display.display_meteriologica import Cidade

class MeteorologistApp:
    """
    Aplicação para obter informações meteorológicas de uma cidade.
    """
    def __init__(self):
        self.cidade = None

    def obter_informacoes(self):
        """
        Solicita ao usuário o nome da cidade e instancia um objeto Cidade.
        """
        nome_cidade = input("Digite o nome da cidade: ").strip().title()
        self.cidade = Cidade(nome_cidade)
        print(self.cidade.mostrar_cidade())

    def executar(self):
        """
        Inicia o processo de obtenção de informações.
        """
        self.obter_informacoes()

#if __name__ == "__main__":
#    app = MeteorologistApp()
#    app.executar()
