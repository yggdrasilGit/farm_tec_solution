# farm_tec_solution
 
# Gerenciador de Insumos Agrícolas

Este projeto fornece um sistema simples para gerenciamento de insumos agrícolas, incluindo adubos, sementes e culturas. O objetivo é facilitar a administração desses recursos, permitindo cadastro, atualização e remoção de dados relacionados à agricultura.

## Estrutura do Projeto

O sistema é composto pelos seguintes módulos:

1. **`insumo_manage.py`**: Classe base para representar insumos agrícolas.
2. **`adubo_manager.py`**: Classe para gerenciar adubos.
3. **`semente_manager.py`**: Classe para gerenciar sementes.
4. **`culture_manager.py`**: Classe para gerenciar culturas agrícolas, armazenando informações em um arquivo JSON.

## Dependências

- Python 3.x
- Biblioteca `json` (embutida no Python)

## Instalação

Nenhuma instalação específica é necessária além do Python 3.x.

## Uso

### 1. Insumo Base (`insumo_manage.py`)

A classe `Insumo` define a estrutura básica de um insumo agrícola, contendo:
- `nome`: Nome do insumo.
- `descricao`: Descrição do insumo.
- `quantidade`: Quantidade disponível.
- `unidade`: Unidade de medida.

Exemplo de uso:
```python
from insumo_manage import Insumo

insumo = Insumo("Fertilizante A", "Melhora a qualidade do solo", 100, "kg")
print(insumo)
```

### 2. Gerenciamento de Adubo (`adubo_manager.py`)

A classe `Adubo` herda de `Insumo` e adiciona atributos específicos:
- `tipo`: Tipo de adubo (Orgânico, Mineral, etc.).
- `forma_aplicacao`: Forma de aplicação (Granulado, Líquido, etc.).
- `dosagem_recomendada`: Quantidade recomendada de uso.

Exemplo de uso:
```python
from adubo_manager import Adubo

adubo = Adubo("Composto Orgânico", "Adubo natural", 50, "kg", "Orgânico", "Granulado", "300g/m²")
print(adubo.verificar_dosagem())
```

### 3. Gerenciamento de Sementes (`semente_manager.py`)

A classe `Semente` também herda de `Insumo` e adiciona atributos como:
- `tipo`: Tipo de semente.
- `origem`: Origem da semente.
- `validade`: Data de validade.
- `germinacao`: Taxa de germinação.

Exemplo de uso:
```python
from semente_manager import Semente

semente = Semente("Milho", "Semente híbrida", 200, "unidades", "Híbrida", "Brasil", "2025-12-31", "85%")
print(semente.verificar_validade())
```

### 4. Gerenciamento de Culturas (`culture_manager.py`)

A classe `Cultura` permite cadastrar, atualizar e remover culturas agrícolas armazenadas em um arquivo JSON.

Exemplo de uso:
```python
from culture_manager import Cultura

cultura = Cultura()
cultura.adicionar_cultura()
cultura.mostrar_culturas()
```

## Contribuição

Se quiser contribuir com melhorias ou novas funcionalidades, sinta-se à vontade para enviar sugestões!

## Licença

Este projeto está sob a licença MIT.

