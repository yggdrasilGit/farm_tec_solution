from display.display_meteriologica import Cidade

class MeteorologistApp:
    def __init__(self):
        self.cidade = None

    def obter_informacoes(self):
        nome_cidade = input('Digite o nome da cidade: ')
        self.cidade = Cidade(nome_cidade)
        self.cidade.mostrar_cidade()

    def executar(self):
        self.obter_informacoes()
        

#if __name__ == "__main__":
#    app = MeteorologistApp()
#    app.executar()



