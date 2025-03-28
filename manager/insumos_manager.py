import json
from manager.adubo_manager import Adubo
from manager.fertilizante_manager import Fertilizante
from manager.insumo_manage import Insumo
from manager.semente_manager import Semente
from manager.veneno_manage import Veneno

class InsumoManager:
    def __init__(self, arquivo="dados/insumos.json"):
        self.arquivo = arquivo
        self.insumo_salvar = "dados/resultados.json"
        self.insumos = self.carregar_dados()

    def salvar_dados(self):
        """Salva os dados dos insumos no arquivo JSON."""
        with open(self.insumo_salvar, 'w') as f:
            # Convertendo a lista de objetos para um dicionário serializável
            insumos_serializados = {insumo.nome: insumo.to_dict() for insumo in self.insumos}
            json.dump(insumos_serializados, f, indent=4)
        print("📂 Dados salvos com sucesso!")

    def carregar_dados(self):
        """Carrega os dados dos insumos do arquivo JSON."""
        try:
            with open(self.arquivo, 'r') as f:
                insumos_serializados = json.load(f)
                insumos = []

                for nome, insumo_data in insumos_serializados.items():
                    tipo = insumo_data.get("tipo_insumo", "insumo")  # Obtém o tipo original

                    # Formatação apenas para exibição (não altera os dados do JSON)
                    tipo_formatado = tipo.title()
                    descricao_formatada = insumo_data.get("descricao", "").title()

                    # Criar uma cópia para evitar alterar o JSON original em memória
                    insumo_data = insumo_data.copy()
                    insumo_data.pop("tipo_insumo", None)  
                    insumo_data["descricao"] = descricao_formatada 

                    # Instancia os objetos de acordo com o tipo original
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

                return insumos  # Retorna a lista de objetos
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def create(self, nome, descricao, quantidade, unidade, tipo_insumo="insumo", **kwargs):
        """Cria um novo insumo e salva no arquivo."""
        nome = nome.lower()

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

        # Adiciona à lista de insumos e salva no JSON
        self.insumos.append(novo_insumo)
        self.salvar_dados()
        print(f"✅ {tipo_insumo.capitalize()} '{nome}' criado com sucesso!")

    def read(self, nome):
        """Retorna um insumo pelo nome."""
        return next((insumo for insumo in self.insumos if insumo.nome == nome), None)

    def update(self, nome, **kwargs):
        """Atualiza um insumo existente."""
        insumo = self.read(nome)
        if insumo:
            for key, value in kwargs.items():
                if hasattr(insumo, key):
                    setattr(insumo, key, value)
            self.salvar_dados()
            print(f"🔄 Insumo '{nome}' atualizado com sucesso!")
        else:
            print(f"⚠ Insumo '{nome}' não encontrado.")

    def delete(self, nome):
        """Remove um insumo pelo nome."""
        nome = nome.lower()
        insumo = self.read(nome)
        if insumo:
            self.insumos.remove(insumo)
            self.salvar_dados()
            print(f"🗑 Insumo '{nome}' deletado com sucesso!")
        else:
            print(f"⚠ Insumo '{nome}' não encontrado.")

    def list_all(self):
        """Lista todos os insumos cadastrados."""
        if not self.insumos:
            print("📭 Nenhum insumo registrado.")
        else:
            print("\n📋 Lista de Insumos Cadastrados:\n")
            for insumo in self.insumos:
                insumo.nome = insumo.nome.title()
                print(insumo)
                print()

    # Função para buscar por nome
    def buscar_produto(self, nome, tipo_insumo=None):
        """Busca um insumo pelo nome e, opcionalmente, pelo tipo."""
        resultados = []
        for insumo in self.insumos:
            if insumo.nome.strip().lower() == nome.strip().lower():
                # Se um tipo for especificado, verifica se o insumo corresponde ao tipo
                if tipo_insumo:
                    if isinstance(insumo, tipo_insumo):  # Verifique se insumo é uma instância de tipo_insumo
                        resultados.append(insumo)
                else:
                    # Caso não seja especificado o tipo, adiciona qualquer insumo com o nome correspondente
                    resultados.append(insumo)
        return resultados