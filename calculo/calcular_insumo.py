import json

class Plantio:
    def __init__(self, areas_plantadas_file, insumos_file, resultado_file="dados/resultado.json"):
        # Carregar os dados dos arquivos
        with open(areas_plantadas_file, "r") as f:
            self.areas_plantadas = json.load(f)
        
        with open(insumos_file, "r") as f:
            self.insumos = json.load(f)
        
        self.resultado_file = resultado_file

    def exibir_culturas(self):
        print("\n=== CULTURAS DISPONÍVEIS ===")
        for i, cultura in enumerate(self.areas_plantadas, 1):
            print(f"{i}. {cultura['nome'].capitalize()} - {cultura['tamanho']:.2f} hectares")

    def escolher_cultura(self):
        while True:
            try:
                escolha = int(input("\nDigite o número da cultura que deseja plantar: "))
                if 1 <= escolha <= len(self.areas_plantadas):
                    cultura_escolhida = self.areas_plantadas[escolha - 1]["nome"]
                    area_plantada = self.areas_plantadas[escolha - 1]["tamanho"]
                    return cultura_escolhida, area_plantada
                else:
                    print("Número inválido! Escolha um número da lista.")
            except ValueError:
                print("Entrada inválida! Digite um número válido.")

    def escolher_insumos(self, tipo):
        print(f"\n=== {tipo.upper()} DISPONÍVEIS ===")
        insumo_numerado = {}
        contador = 1

        for chave, insumo in self.insumos.items():
            if tipo.lower() in insumo["nome"].lower():
                print(f"{contador}. {insumo['nome']} - {insumo['descricao']} ({insumo['unidade']})")
                insumo_numerado[contador] = chave
                contador += 1

        if not insumo_numerado:
            print(f"Nenhum {tipo.lower()} disponível.")
            return {}

        escolhas = input(f"\nDigite os números dos {tipo.lower()} que deseja utilizar, separados por vírgula: ").strip()
        escolhas_indices = [int(x) for x in escolhas.split(",") if x.isdigit() and int(x) in insumo_numerado]

        return {insumo_numerado[i]: self.insumos[insumo_numerado[i]] for i in escolhas_indices}

    def definir_quantidade(self, insumos_escolhidos, categoria):
        quantidades = {}
        for nome, insumo in insumos_escolhidos.items():
            while True:
                try:
                    quantidade = float(input(f"Digite a quantidade de '{insumo['descricao']}' ({insumo['unidade']}) por hectare para {categoria}: "))
                    if quantidade > 0:
                        quantidades[nome] = quantidade
                        break
                    else:
                        print("A quantidade deve ser maior que zero!")
                except ValueError:
                    print("Entrada inválida! Digite um número válido.")
        return quantidades

    def adicionar_insumos(self, insumos_escolhidos, quantidades, area_plantada, resultado):
        # Verifique se "insumos_utilizados" está sendo inicializado corretamente como lista
        if "insumos_utilizados" not in resultado:
            resultado["insumos_utilizados"] = []  # Inicializa como uma lista, caso ainda não tenha sido inicializado
        
        for nome, insumo in insumos_escolhidos.items():
            quantidade_total = quantidades[nome] * area_plantada
            resultado["insumos_utilizados"].append({
                "insumo": nome,
                "descricao": insumo["descricao"],
                "quantidade_necessaria": quantidade_total,
                "unidade": insumo["unidade"]
            })

    def salvar_resultado(self, resultado):
        try:
            # Carregar os resultados existentes, se houver
            with open(self.resultado_file, "r", encoding="utf-8") as f:
                resultados_anteriores = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            resultados_anteriores = []  # Se o arquivo não existir ou estiver vazio, inicia uma lista vazia
        
        # Adicionar o novo resultado à lista existente
        resultados_anteriores.append(resultado)

        # Salvar os resultados atualizados
        with open(self.resultado_file, "w", encoding="utf-8") as f:
            json.dump(resultados_anteriores, f, indent=4, ensure_ascii=False)

        print("\nCálculo concluído! Os dados foram adicionados ao arquivo 'resultado.json'.")

    def calcular(self):
        # Exibir e escolher a cultura
        self.exibir_culturas()
        cultura_escolhida, area_plantada = self.escolher_cultura()

        # Escolher insumos
        fertilizantes = self.escolher_insumos("Fertilizante")
        adubos = self.escolher_insumos("Adubo")
        venenos = self.escolher_insumos("Veneno")
        sementes = self.escolher_insumos("Semente")

        if not sementes:
            print("\nVocê deve escolher pelo menos uma semente para plantar.")
            return

        # Pedir as quantidades para cada insumo
        quantidade_fertilizantes = self.definir_quantidade(fertilizantes, "Fertilizante")
        quantidade_adubos = self.definir_quantidade(adubos, "Adubo")
        quantidade_venenos = self.definir_quantidade(venenos, "Veneno")
        quantidade_sementes = self.definir_quantidade(sementes, "Semente")

        # Calcular quantidade total para a área plantada
        resultado = {"cultura": cultura_escolhida, "area_plantada": area_plantada, "insumos_utilizados": []}
        
        # Adicionar os insumos ao resultado
        self.adicionar_insumos(fertilizantes, quantidade_fertilizantes, area_plantada, resultado)
        self.adicionar_insumos(adubos, quantidade_adubos, area_plantada, resultado)
        self.adicionar_insumos(venenos, quantidade_venenos, area_plantada, resultado)
        self.adicionar_insumos(sementes, quantidade_sementes, area_plantada, resultado)

        # Salvar o resultado no arquivo
        self.salvar_resultado(resultado)

# Criar uma instância da classe e rodar o cálculo
#plantio = Plantio("dados/areas_plantadas.json", "dados/insumos.json")
#plantio.calcular()
