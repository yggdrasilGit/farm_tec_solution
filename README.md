```markdown
# Farm Tech Solution

## 📌 Descrição  
Este programa realiza operações de **CRUD** para gerenciar áreas de plantio, insumos, áreas plantadas e também calcula a quantidade de área plantada de acordo com figuras geométricas como quadrado, retângulo ou triângulo. Além disso, oferece relatórios das culturas e os insumos utilizados por área, calculando a média e o desvio padrão geral das áreas plantadas e insumos. Também fornece dados climáticos por meio de uma API externa.

## 🐜 Tecnologias Utilizadas  
- **Python 3.12**  
- **cffi==1.17.1**  
- **Jinja2==3.1.6**  
- **MarkupSafe==3.0.2**  
- **orjson==3.10.15**  
- **pycparser==2.22**  
- **pyfiglet==1.0.2**  
- **rpy2==3.5.17**  
- **tabulate==0.9.0**  
- **tzlocal==5.3.1**  
- **APIs**: [OpenWeatherMap](https://api.openweathermap.org/data/2.5/weather)  
- **R**  
- **jsonlite**  
- **fs**  
- **here**  
- **httr**  
- **tibble**

## 🛠 Instalação  
Siga os passos abaixo para configurar o projeto em sua máquina.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/yggdrasilGit/farm_tec_solution.git
   ```
2. **Acesse o diretório do projeto:**
   ```bash
   cd farm_tec_solution
   ```
3. **Crie um ambiente virtual e ative-o:**
   - Para Linux/macOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Para Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar  
Depois de configurar o ambiente, você pode executar o projeto com o seguinte comando:

```bash
python main.py
```

## 🧪 Testes  
Para rodar os testes automatizados, utilize o seguinte comando:

```bash
pytest
```

## 💁️ Estrutura do Projeto  
A estrutura do projeto é organizada da seguinte forma:

```plaintext
# Estrutura do Projeto: Farm Tech Solution

Abaixo está a estrutura de diretórios e arquivos do projeto:

```plaintext
├── farm_tec_solution/                         # Código-fonte principal
│   ├── __pycache__/                           # Arquivos binários compilados
│   ├── .Rproj.user                            # Arquivo de configuração R
│   ├── api_input_data/                        # Scripts para carregar dados da API
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── load_api_meteriologia.py          # Executa a API climática
│   │   ├── load_api_meteriologist.py         # Carrega dados meteorológicos
│   │   ├── load_data_statis.py               # Carrega dados estatísticos
│   │   ├── load_api_geolocalizaca.py         # Carrega dados de geolocalização
│   ├── calculo/                               # Cálculos e testes automatizados
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── calcular_area.py                  # Cálculos de áreas plantadas
│   │   ├── calcular_insumo.py                # Cálculos de insumos
│   ├── dados/                                  # Dados do projeto
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── area_plantada.json                # Dados de áreas plantadas
│   │   ├── cidade.json                       # Dados de cidades
│   │   ├── clima_portugues.json              # Dados climáticos em português
│   │   ├── culturas.json                     # Dados sobre culturas
│   │   ├── dados_climatios.json              # Dados meteorológicos
│   │   ├── insumos.json                      # Dados de insumos
│   │   ├── latitude_longitude.json           # Coordenadas geográficas
│   │   ├── resultado.json                    # Resultados de cálculos
│   ├── displays/                              # Scripts para exibição de dados
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── display_area.py                   # Exibição de áreas plantadas
│   │   ├── display_cadastro_cultura.py       # Exibição do cadastro de culturas
│   │   ├── display_cultura.py                # Exibição de culturas
│   │   ├── display_insumo.py                 # Exibição de insumos
│   │   ├── display_meteriologica.py          # Exibição de dados climáticos
│   │   ├── display_principal.py              # Tela principal
│   │   ├── display_stats.py                  # Exibição de estatísticas
│   ├── env                                     # Ambiente virtual
│   ├── manager/                                # Gerenciamento de insumos
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── adubo_manager.py                  # Gerenciamento de adubos
│   │   ├── area_manager.py                   # Gerenciamento de áreas
│   │   ├── culture_manager.py                # Gerenciamento de culturas
│   │   ├── fertilizante_manager.py           # Gerenciamento de fertilizantes
│   │   ├── insumo_manage.py                  # Gerenciamento de insumos
│   │   ├── insumos_manager.py                # Gerenciamento de insumos
│   │   ├── semente_manager.py                # Gerenciamento de sementes
│   │   ├── veneno_manager.py                 # Gerenciamento de venenos
│   ├── R/                                      # Scripts R para cálculos
│   │   ├── api_climatic.R                    # Função para chamada da API climática
│   │   ├── funcoes.R                          # Funções auxiliares
│   │   ├── script_geolocalizaton.R           # Geolocalização
│   │   ├── script_statis.R                   # Scripts para cálculos estatísticos
│   │   ├── data_visulizaton_cultura.Rmd      # Visualização de dados de cultura
│   ├── test/                                   # Testes automatizados
│   │   ├── __pycache__/                       # Arquivos binários
│   │   ├── teste_araa_manager.py             # Teste do manager de áreas
│   │   ├── teste_cultura_manager.py          # Teste do manager de culturas
│   │   ├── teste_fertilizante_manager.py     # Teste do manager de fertilizantes
│   │   ├── teste_isumo.py                    # Teste do manager de insumos
│   ├── .gitattributes                         # Arquivo de configurações do Git
│   ├── .gitignore                             # Ignora arquivos não rastreados no Git
│   ├── .RData                                 # Dados R
│   ├── .Rhistory                              # Histórico de comandos R
│   ├── enterprise_name.py                     # Nome da empresa
│   ├── farm_tec_solution.Rproj                # Arquivo do projeto R
│   ├── main.py                                # Arquivo principal para execução
│   ├── README.md                              # Documentação do projeto
│   ├── requirements.txt                       # Dependências do projeto

```

## 📄 Licença  
Este projeto está licenciado sob a **MIT License**. Para qualquer cidadao.

## 🤝 Contribuindo  
Este projeto aceita contribuições! Se você deseja contribuir, siga estas etapas:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça suas alterações.
4. Envie um pull request detalhando as mudanças.

## 📞 Contato  
Se tiver dúvidas ou sugestões, entre em contato com o mantenedor do projeto:
- **E-mail**: yggdrasil.git@gmail.com  
- **GitHub**: [@yggdrasilGit](https://github.com/yggdrasilGit)
```