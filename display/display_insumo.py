from manager.insumos_manager import InsumoManager


class InsumoMenu:
    def __init__(self):
        self.manager = InsumoManager()

    def exibir_menu(self):
        while True:
            print("\n=== Gerenciamento de Insumos ===")
            print("1. Criar Insumo")
            print("2. Listar Insumos")
            print("3. Atualizar Insumo")
            print("4. Deletar Insumo")
            print("5. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                self.criar_insumo()
            elif escolha == "2":
                self.manager.list_all()
            elif escolha == "3":
                self.atualizar_insumo()
            elif escolha == "4":
                self.deletar_insumo()
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def criar_insumo(self):
        print("\nEscolha o tipo de insumo:")
        print("1. Fertilizante")
        print("2. Semente")
        print("3. Adubo")
        print("4. Veneno")
        print("5. Outro")
        
        tipo_escolha = input("Digite o número correspondente ao tipo: ")
        
        tipos = {"1": "fertilizante", "2": "semente", "3": "adubo", "4": "veneno", "5": "insumo"}
        tipo_insumo = tipos.get(tipo_escolha, "insumo")
        
        nome = tipo_insumo.capitalize()
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        unidade = input("Unidade de medida por hectare: ")
        
        kwargs = {}
        if tipo_insumo == "fertilizante":
            kwargs["composicao"] = input("Composição: ")
            kwargs["tipo"] = input("Tipo de fertilizante: ")
            kwargs["dosagem_recomendada"] = input("Dosagem recomendada: ")
            kwargs["preco_unitario"] = float(input("Preço unitário: "))
        elif tipo_insumo == "semente":
            kwargs["germinacao"] = input("Taxa de germinação: ")
            kwargs["tipo"] = input("Tipo: ")
            kwargs["origem"] = input("Origem: ")
            kwargs["validade"] = input("Validade: ")
        elif tipo_insumo == "adubo":
            kwargs["tipo"] = input("Tipo de adubo: ")
            kwargs["forma_aplicacao"] = input("Forma de aplicação: ")
            kwargs["dosagem_recomendada"] = input("Dosagem recomendada: ")
        elif tipo_insumo == "veneno":
            kwargs["tipo"] = input("Tipo de veneno: ")
            kwargs["toxicidade"] = input("Nível de toxicidade: ")
            kwargs["area_aplicacao"] = input("Área de aplicação: ")

        self.manager.create(nome, descricao, quantidade, unidade, tipo_insumo, **kwargs)
    
    def atualizar_insumo(self):
        nome = input("Nome do insumo a ser atualizado: ")
        campo = input("Campo a ser atualizado (ex: quantidade, preco_unitario): ")
        valor = input("Novo valor: ")
        
        if campo in ["quantidade"]:
            valor = int(valor)
        elif campo in ["preco_unitario"]:
            valor = float(valor)
        
        self.manager.update(nome, **{campo: valor})
    
    def deletar_insumo(self):
        nome = input("Nome do insumo a ser deletado: ")
        self.manager.delete(nome)
