from api_input_data.load_api_metereologica import RClimateDataLoader
from api_input_data.load_data_meteriologist import MeteorologistDataLoader
from api_input_data.load_data_statis import RScriptLoader
from api_input_data.loard_api_geolocalizacao import RGeolocationLoader
from calculo.calcular_insumo import Plantio
from display.display_cadastro_cultura import MenuCultura
from display.display_area import MenuAreaPlantada
from display.display_cultura import RelatorioAgricola
from display.display_insumo import InsumoMenu
from display.display_meteriologica import Cidade


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
            print("4. Calcular Cultura")
            print("5. Relatorio Cultura")
            print("6. Relatorio Climatico")
            print("7. Relatorio Estatistica")
            print("0. Sair")
            
            # Solicita ao usuário para escolher uma opção
            opcao = input("Escolha uma opção (1, 0): ")
            
            if opcao == '1':
                MenuCultura().menu_cultura()   # Exibe a lista de culturas
            elif opcao == '2':
                MenuAreaPlantada().menu_area()
            elif opcao == '3':
                InsumoMenu().exibir_menu()
            elif opcao == '4':
                plantio = Plantio("dados/areas_plantadas.json", "dados/insumos.json")
                plantio.calcular()
            elif opcao == '5':
                relatorio = RelatorioAgricola("dados/resultado.json")
                relatorio.exibir_resultados()
            elif opcao == '6':
                nome_cidade = input("Digite o nome da cidade: ")
                cidade = Cidade(nome_cidade)
                print(cidade.mostrar_cidade())
                print(cidade.buscar_informacoes())
                caminho_arquivo = cidade.salvar_em_json()
                print(f"Informações salvas em {caminho_arquivo}")
                geo_loader = RGeolocationLoader()
                geo_loader.executar_geolocalizacao()
                loader = RClimateDataLoader()
                loader.executar_script()
                nome_arquivo = "clima_portugues.json"  # Nome do arquivo JSON
                loader = MeteorologistDataLoader(nome_arquivo)
                dados_clima = loader.carregar_arquivo_json()
            elif opcao == '7':
                estatistica = RScriptLoader("R/script_statis.R")
                estatistica.carregar_script()
            elif opcao == '0':
                print("\nSaindo\n")
                break # Exibe as culturas cadastradas
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")