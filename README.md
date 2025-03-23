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
├── farm_tec_solution/                 # Código-fonte
│   ├── __pycache__/                   # Arquivos binários
│   ├── .Rproj.user                    # Extensão R
│   ├── api_input_data/                # Scripts para carregar dados da API
│   │   ├── __pycache__/               # Arquivos binários
│   │   ├── load_api_meteriologia.py   # Executa a API climática
│   ├── calculo/                       # Testes automatizados
│   │   ├── __pycache__/               # Arquivos binários
│   ├── dados/                          # Dados do projeto
│   │   ├── __pycache__/               # Arquivos binários
│   ├── displays/                       # Exibição de dados
│   │   ├── __pycache__/               # Arquivos binários
│   ├── env                             # Ambiente virtual
│   ├── manager/                        # Gerenciamento de insumos
│   │   ├── __pycache__/               # Arquivos binários
│   ├── R/                              # Scripts R para cálculos
│   │   ├── __pycache__/               # Arquivos binários
│   ├── test/                           # Testes
│   │   ├── __pycache__/               # Arquivos binários
│   ├── .gitattributes                 # Configurações do Git
│   ├── .gitignore                     # Ignora arquivos não desejados no Git
│   ├── .RData                         # Dados R
│   ├── .Rhistory                      # Histórico R
│   ├── enterprise_name.py             # Nome da empresa
│   ├── farm_tec_solution.Rproj        # Projeto R
│   ├── main.py                        # Arquivo principal do projeto
│   ├── README.md                      # Documentação
│   ├── requirements.txt               # Dependências do projeto
```

## 📄 Licença  
Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo  
Este projeto aceita contribuições! Se você deseja contribuir, siga estas etapas:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça suas alterações.
4. Envie um pull request detalhando as mudanças.

## 📞 Contato  
Se tiver dúvidas ou sugestões, entre em contato com o mantenedor do projeto:
- **E-mail**: exemplo@email.com  
- **GitHub**: [@yggdrasilGit](https://github.com/yggdrasilGit)
```