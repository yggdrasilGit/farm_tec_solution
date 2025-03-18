import json
from manager.adubo_manager import Adubo
from manager.fertilizante_manager import Fertilizante
from manager.insumo_manage import Insumo
from manager.semente_manager import Semente
from manager.veneno_manage import Veneno

class InsumoManager:
    def __init__(self, arquivo="dados/insumos.json"):
        self.arquivo = arquivo
        self.insumos = self.carregar_dados()

    def salvar_dados(self):
        """Salva os dados dos insumos no arquivo JSON."""
        with open(self.arquivo, 'w') as f:
            insumos_serializados = [insumo.__dict__ for insumo in self.insumos]
            json.dump(insumos_serializados, f, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self):
        """Carrega os dados dos insumos do arquivo JSON."""
        try:
            with open(self.arquivo, 'r') as f:
                insumos_serializados = json.load(f)
                insumos = []
                for insumo_data in insumos_serializados:
                    # Aqui, recriaremos os objetos a partir dos dados salvos
                    tipo = insumo_data.get("tipo_insumo", "insumo")
                    if tipo == "fertilizante":
                        insumo = Fertilizante(**insumo_data)
                    elif tipo == "semente":
                        insumo = Semente(**insumo_data)
                    elif tipo == "adubo":
                        insumo = Adubo(**insumo_data)
                    elif tipo == "veneno":
                        insumo = Veneno(**insumo_data)
                    else:
                        insumo = Insumo(**insumo_data)
                    insumos.append(insumo)
                return insumos
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def create(self, nome, descricao, quantidade, unidade, preco_unitario, tipo_insumo="insumo", **kwargs):
        """Cria um Insumo, Fertilizante, Semente, Adubo ou Veneno com base no tipo especificado."""
        if tipo_insumo == "fertilizante":
            novo_insumo = Fertilizante(nome, descricao, quantidade, unidade, **kwargs)
        elif tipo_insumo == "semente":
            novo_insumo = Semente(nome, descricao, quantidade, unidade, **kwargs)
        elif tipo_insumo == "adubo":
            novo_insumo = Adubo(nome, descricao, quantidade, unidade, **kwargs)
        elif tipo_insumo == "veneno":
            novo_insumo = Veneno(nome, descricao, quantidade, unidade, **kwargs)
        else:
            novo_insumo = Insumo(nome, descricao, quantidade, unidade)

        self.insumos.append(novo_insumo)
        self.salvar_dados()
        print(f"{tipo_insumo.capitalize()} '{nome}' criado com sucesso!")

    def read(self, nome):
        """Retorna um insumo pelo nome."""
        for insumo in self.insumos:
            if insumo.nome == nome:
                return insumo
        return None

    def update(self, nome, **kwargs):
        """Atualiza um insumo existente."""
        insumo = self.read(nome)
        if insumo:
            for key, value in kwargs.items():
                if hasattr(insumo, key):
                    setattr(insumo, key, value)
            self.salvar_dados()
            print(f"Insumo '{nome}' atualizado com sucesso!")
        else:
            print(f"Insumo '{nome}' não encontrado.")

    def delete(self, nome):
        """Remove um insumo pelo nome."""
        insumo = self.read(nome)
        if insumo:
            self.insumos.remove(insumo)
            self.salvar_dados()
            print(f"Insumo '{nome}' deletado com sucesso!")
        else:
            print(f"Insumo '{nome}' não encontrado.")

    def list_all(self):
        """Lista todos os insumos cadastrados."""
        if not self.insumos:
            print("Nenhum insumo registrado.")
        else:
            print("\n📋 Lista de Insumos Cadastrados:\n")
            for insumo in self.insumos:
                print(insumo)
                print(f"   💰 Valor Total: R${insumo.calcular_valor_total():.2f}\n")
