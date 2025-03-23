# Farm Tech Soluiton

## 📌 Descrição  
Este programa faz operacoes de CRUD, de área de plantio, insumos, area plantadas e tambem calcula 
a quantidade de area plantada de acordo com a figura geometrica quadrado, retangulo ou triângulo 
alem disso oferece relatorios das culturas e o insumo que ira utilizar por area a media e o desvio
padrao geral das areas plantadas e insumos, alem de fornecer dados climaticos

## 🐜 Tecnologias Utilizadas  
- Python 3.12 
- cffi==1.17.1
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- orjson==3.10.15
- pycparser==2.22
- pyfiglet==1.0.2
- rpy2==3.5.17
- tabulate==0.9.0
- tzlocal==5.3.1
- APIs == "https://api.openweathermap.org/data/2.5/weather?
- R 
- jsonlite
- fs
- here
- httr
- tibble

## 🛠 Instalação  
1. Clone o repositório:
   ```bash
   git clone https://github.com/yggdrasilGit/farm_tec_solution.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd farm_tec_solution
   ```
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Usar  
Explique como executar o projeto com exemplos de código:  

```bash
python main.py
```

## 🧪 Testes  
Caso haja testes automatizados, explique como executá-los:  
```bash
pytest
```

## 💁️ Estrutura do Projeto  
```plaintext
├── farm_tec_solution/                 # Código-fonte
│   ├── __pycache__/          # arquivo binario
│   ├── .Rproj.user         # estencao r
│   ├── api_input_data/   # arquivos de carregar os scripts R
|   │   ├── __pycache__
|   │   ├── load_api_meteriologia.py # Executa a api climatica          
│   ├── calculo           # Testes automatizados
|   │   ├── __pycache__
│   ├── dados  
|   │   ├── __pycache__
│   ├── displays  
|   │   ├── __pycache__
│   ├── env                 # ambientevirtual
│   ├── manager/
|   │   ├── __pycache__
│   ├── R/
|   │   ├── __pycache__
│   ├── test
|   │   ├── __pycache__
│   ├── .gitattributes
│   ├── .gitiginore
│   ├── .RData
│   ├── .Rhistory
│   ├── enterprise_name.py
│   ├── farm_tec_solution.Rproj
│   ├── main.py
│   ├── README.md        # Documentação
│   ├── requirements.txt # Dependências do projeto
```

## 📄 Licença  
Informe a licença do projeto, por exemplo:  

> Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo  
Se o projeto aceita contribuições, adicione diretrizes para colaboradores.

## 📞 Contato  
Se desejar, adicione informações para contato ou links úteis.

