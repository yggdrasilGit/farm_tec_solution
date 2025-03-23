# Classe Semente que herda de Insumo
from manager.insumo_manage import Insumo


class Semente(Insumo):
    """
    Classe que representa uma semente, herda de Insumo e adiciona informações específicas sobre sementes.

    Atributos:
        nome (str): Nome da semente.
        descricao (str): Descrição da semente.
        quantidade (int): Quantidade disponível da semente.
        unidade (str): Unidade de medida da quantidade.
        tipo (str): Tipo da semente (ex: hortaliça, flor, etc).
        origem (str): Origem da semente (ex: nacional, importada).
        validade (str): Data de validade da semente.
        germinacao (str): Taxa de germinação da semente.

    Métodos:
        verificar_validade(): Retorna a data de validade da semente.
        __str__(): Representação em string da semente.
    """
    
    def __init__(self, nome, descricao, quantidade, unidade, tipo, origem, validade, germinacao):
        """
        Inicializa os atributos da classe Semente.

        Parâmetros:
            nome (str): Nome da semente.
            descricao (str): Descrição da semente.
            quantidade (int): Quantidade disponível da semente.
            unidade (str): Unidade de medida da quantidade.
            tipo (str): Tipo da semente (ex: hortaliça, flor, etc).
            origem (str): Origem da semente (ex: nacional, importada).
            validade (str): Data de validade da semente.
            germinacao (str): Taxa de germinação da semente.
        """
        super().__init__(nome, descricao, quantidade, unidade)
        self.tipo = tipo
        self.origem = origem
        self.validade = validade
        self.germinacao = germinacao

    def verificar_validade(self):
        """
        Retorna a data de validade da semente.

        Retorno:
            str: Mensagem com a data de validade da semente.
        """
        return f"Semente {self.tipo} válida até: {self.validade}"

    def __str__(self):
        """
        Retorna uma representação em string dos detalhes da semente.

        Retorno:
            str: Informações sobre a semente.
        """
        return f"Semente: {self.tipo}, Origem: {self.origem}, Validade: {self.validade}\n{super().__str__()}"
