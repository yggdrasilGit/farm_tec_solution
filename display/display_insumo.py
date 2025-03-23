from manager.insumos_manager import InsumoManager

class InsumoMenu:
    """Classe para gerenciar o menu de insumos agrícolas."""
    
    def __init__(self):
        """Inicializa o gerenciador de insumos."""
        self.manager = InsumoManager()

    def exibir_menu(self):
        """Exibe o menu de opções para gerenciamento de insumos."""
        while True:
            print("\n=== Gerenciamento de Insumos ===")
            print("1. Criar Insumo")
            print("2. Listar Insumos")
            print("3. Atualizar Insumo")
            print("4. Deletar Insumo")
            print("5. Buscar Insumo")
            print("0. Sair")
            
            escolha = input("Escolha uma opção: ").strip()
            
            if escolha == "1":
                self.criar_insumo()
            elif escolha == "2":
                self.manager.list_all()
            elif escolha == "3":
                self.atualizar_insumo()
            elif escolha == "4":
                self.deletar_insumo()
            elif escolha == "5":
                self.buscar_insumo()
            elif escolha == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def criar_insumo(self):
        """Solicita ao usuário as informações para criar um insumo."""
        print("\nEscolha o tipo de insumo:")
        tipos = {"1": "fertilizante", "2": "semente", "3": "adubo", "4": "veneno", "5": "insumo"}
        for key, value in tipos.items():
            print(f"{key}. {value.capitalize()}")
        
        tipo_escolha = input("Digite o número correspondente ao tipo: ").strip()
        tipo_insumo = tipos.get(tipo_escolha, "insumo")
        
        nome = tipo_insumo.capitalize()
        descricao = input("Descrição: ").strip()
        quantidade = self.validar_inteiro("Quantidade: ")
        unidade = input("Unidade de medida por hectare: ").strip()
        
        kwargs = {}
        if tipo_insumo == "fertilizante":
            kwargs["composicao"] = input("Composição: ").strip()
            kwargs["tipo"] = input("Tipo de fertilizante: ").strip()
            kwargs["dosagem_recomendada"] = input("Dosagem recomendada: ").strip()
            kwargs["preco_unitario"] = self.validar_float("Preço unitário: ")
        elif tipo_insumo == "semente":
            kwargs["germinacao"] = input("Taxa de germinação: ").strip()
            kwargs["tipo"] = input("Tipo: ").strip()
            kwargs["origem"] = input("Origem: ").strip()
            kwargs["validade"] = input("Validade: ").strip()
        elif tipo_insumo == "adubo":
            kwargs["tipo"] = input("Tipo de adubo: ").strip()
            kwargs["forma_aplicacao"] = input("Forma de aplicação: ").strip()
            kwargs["dosagem_recomendada"] = input("Dosagem recomendada: ").strip()
        elif tipo_insumo == "veneno":
            kwargs["tipo"] = input("Tipo de veneno: ").strip()
            kwargs["toxicidade"] = input("Nível de toxicidade: ").strip()
            kwargs["area_aplicacao"] = input("Área de aplicação: ").strip()

        self.manager.create(nome, descricao, quantidade, unidade, tipo_insumo, **kwargs)
    
    def atualizar_insumo(self):
        """Atualiza um insumo existente com base no nome e campo a ser alterado."""
        nome = input("Nome do insumo a ser atualizado: ").strip()
        campo = input("Campo a ser atualizado (ex: quantidade, preco_unitario): ").strip()
        valor = input("Novo valor: ").strip()
        
        if campo == "quantidade":
            valor = self.validar_inteiro("Novo valor: ")
        elif campo == "preco_unitario":
            valor = self.validar_float("Novo valor: ")
        
        self.manager.update(nome, **{campo: valor})
    
    def deletar_insumo(self):
        """Deleta um insumo existente pelo nome."""
        nome = input("Nome do insumo a ser deletado: ").strip()
        self.manager.delete(nome)

    def buscar_insumo(self):
        """Busca e exibe insumos com base no nome e tipo."""
        nome = input("Digite o nome do insumo que deseja buscar: ").strip()
        print("\nEscolha o tipo de insumo:")
        tipos = {"1": "Fertilizante", "2": "Semente", "3": "Adubo", "4": "Veneno", "5": None}
        
        for key, value in tipos.items():
            tipo_nome = value if value else "Todos os tipos"
            print(f"{key}. {tipo_nome}")
        
        tipo_escolha = input("Digite o número correspondente ao tipo: ").strip()
        tipo_insumo = tipos.get(tipo_escolha)
        
        resultados = self.manager.buscar_produto(nome, tipo_insumo)
        
        if not resultados:
            print(f"⚠ Nenhum insumo encontrado para o nome '{nome}' e tipo '{tipo_insumo}'.")
        else:
            print(f"🔍 Resultados encontrados para '{nome}':")
            for idx, insumo in enumerate(resultados, 1):
                print(f"{idx}. {insumo}")

    @staticmethod
    def validar_inteiro(mensagem):
        """Valida a entrada de um número inteiro."""
        while True:
            try:
                return int(input(mensagem).strip())
            except ValueError:
                print("⚠ Entrada inválida! Digite um número inteiro.")

    @staticmethod
    def validar_float(mensagem):
        """Valida a entrada de um número decimal."""
        while True:
            try:
                return float(input(mensagem).strip())
            except ValueError:
                print("⚠ Entrada inválida! Digite um número válido.")