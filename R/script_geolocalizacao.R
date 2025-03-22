# Carregar as bibliotecas necessárias
library('tidygeocoder')
library('tibble')
library('jsonlite')
library('here')
library("fs")

# Define o caminho do arquivo de funções (utilizando 'here' para resolução do caminho)
caminho_funcoes_relativo <- here("R/", "funcoes.R")  # Caminho relativo do arquivo
print(caminho_funcoes_relativo)
# Exibir o caminho absoluto antes de carregar o script
caminho_funcoes_absoluto <- path_abs(caminho_funcoes_relativo)  # Obtém o caminho absoluto
print(paste("📂 Caminho absoluto do arquivo de funções:", caminho_funcoes_absoluto))

source(caminho_funcoes_absoluto)

cidade_json = load_json("cidade")
print(cidade_json[[1]])

cidade <- get_geocode(cidade_json[[1]])

salvar <- save_json(cidade, "latitude_longitude")






