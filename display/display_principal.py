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
    """
    Classe para exibição do menu principal do sistema de gestão agrícola.
    """
    def __init__(self):
        pass  # Nenhuma inicialização necessária no momento
    
    def menu_principal(self):
        """
        Exibe o menu principal e processa as opções escolhidas pelo usuário.
        """
        while True:
            print("\n=== Menu Principal ===")
            print("1. Trabalhar com Cultura")
            print("2. Trabalhar com Área de Plantio")
            print("3. Trabalhar com Insumo")
            print("4. Calcular Cultura")
            print("5. Relatório Cultura")
            print("6. Relatório Climático")
            print("7. Relatório Estatístico")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                MenuCultura().menu_cultura()
            elif opcao == '2':
                MenuAreaPlantada().menu_area()
            elif opcao == '3':
                InsumoMenu().exibir_menu()
            elif opcao == '4':
                try:
                    plantio = Plantio("dados/areas_plantadas.json", "dados/insumos.json")
                    plantio.calcular()
                except Exception as e:
                    print(f"Erro ao calcular cultura: {e}")
            elif opcao == '5':
                try:
                    relatorio = RelatorioAgricola("dados/resultado.json")
                    relatorio.exibir_resultados()
                except Exception as e:
                    print(f"Erro ao exibir relatório: {e}")
            elif opcao == '6':
                nome_cidade = input("Digite o nome da cidade: ").strip().title()
                cidade = Cidade(nome_cidade)
                print(cidade.mostrar_cidade())
                print(cidade.buscar_informacoes())
                caminho_arquivo = cidade.salvar_em_json()
                print(f"Informações salvas em {caminho_arquivo}")
                
                try:
                    geo_loader = RGeolocationLoader()
                    geo_loader.executar_geolocalizacao()
                    loader = RClimateDataLoader()
                    loader.executar_script()
                    
                    nome_arquivo = "clima_portugues.json"
                    loader = MeteorologistDataLoader(nome_arquivo)
                    dados_clima = loader.carregar_arquivo_json()
                except Exception as e:
                    print(f"Erro ao carregar dados climáticos: {e}")
            elif opcao == '7':
                try:
                    estatistica = RScriptLoader("R/script_statis.R")
                    estatistica.carregar_script()
                except Exception as e:
                    print(f"Erro ao carregar relatório estatístico: {e}")
            elif opcao == '0':
                print("\nSaindo...\n")
                break
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")

# Exemplo de uso:
# menu = Menu()
# menu.menu_principal()
