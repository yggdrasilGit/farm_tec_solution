# Iplementar codigo para entrar com dados com o nome da cidade
library('jsonlite')
library('here')
library("fs")
library('httr')


# Define o caminho do arquivo de funções (utilizando 'here' para resolução do caminho)
caminho_funcoes_relativo <- here("R", "funcoes.R")  # Caminho relativo do arquivo
print(caminho_funcoes_relativo)
# Exibir o caminho absoluto antes de carregar o script
caminho_funcoes_absoluto <- path_abs(caminho_funcoes_relativo)  # Obtém o caminho absoluto
print(paste("📂 Caminho absoluto do arquivo de funções:", caminho_funcoes_absoluto))

source(caminho_funcoes_absoluto)

dados <- load_json('latitude_longitude')
dados

# receber os dados de latitude longitude para pegar a API

# Testar a função (exemplo para São Paulo, Brasil)
api_key <- "7c3d7ff9274814310963b0501025a01d"  # Substitua pela sua chave da OpenWeather
lat <- dados[["lat"]]

lon <- dados[["long"]]

previsao <- obter_previsao(lat, lon, api_key)

data_climatico <- load_json("dados_climaticos")

dados_climaticoss <- processar_dados_clima(data_climatico)
print(dados_climaticoss)

salvar <- save_json(dados_climaticoss,"clima_portugues" )

# retornar dados meteriologicos.