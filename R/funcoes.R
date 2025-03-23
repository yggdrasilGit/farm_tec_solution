# Carregar pacotes necessários
library(jsonlite)
library(fs)
library(here)
library(httr)
library(tibble)
# Se utilizar a função geocode, certifique-se de ter instalado e carregado o pacote tidygeocoder, por exemplo:
# library(tidygeocoder)

#' Ler JSON e converter para data.frame
#'
#' Lê um arquivo JSON e converte seu conteúdo para um data.frame.
#'
#' @param caminho_arquivo Caminho completo do arquivo JSON.
#' @return Um data.frame com os dados lidos.
ler_json_para_dataframe <- function(caminho_arquivo) {
  if (!file.exists(caminho_arquivo)) {
    stop("O arquivo JSON não foi encontrado.")
  }
  
  # Ler o JSON e converter para data.frame
  dados <- fromJSON(caminho_arquivo)
  df <- as.data.frame(dados)
  
  return(df)
}

#' Calcular estatísticas de colunas numéricas
#'
#' Calcula a média e o desvio padrão para colunas numéricas específicas de um data.frame.
#'
#' @param df Data.frame contendo as colunas de interesse.
#' @return Um data.frame com as estatísticas calculadas.
calcular_estatisticas <- function(df) {
  estatisticas <- data.frame(
    tipo = c("Média", "Desvio Padrão"),
    area_plantada = c(mean(df$area_plantada, na.rm = TRUE), sd(df$area_plantada, na.rm = TRUE)),
    semente_quantidade_kg = c(mean(df$semente_quantidade_kg, na.rm = TRUE), sd(df$semente_quantidade_kg, na.rm = TRUE)),
    fertilizante_quantidade_kg = c(mean(df$fertilizante_quantidade_kg, na.rm = TRUE), sd(df$fertilizante_quantidade_kg, na.rm = TRUE)),
    veneno_quantidade_litros = c(mean(df$veneno_quantidade_litros, na.rm = TRUE), sd(df$veneno_quantidade_litros, na.rm = TRUE)),
    adubo_quantidade_kg = c(mean(df$adubo_quantidade_kg, na.rm = TRUE), sd(df$adubo_quantidade_kg, na.rm = TRUE))
  )
  
  return(estatisticas)
}

#' Obter coordenadas geográficas de um local
#'
#' Utiliza a função geocode (do pacote tidygeocoder) para obter as coordenadas de uma localidade.
#'
#' @param location_name Nome do local a ser geocodificado.
#' @return Um tibble com as colunas 'location', 'lat' e 'long'.
get_geocode <- function(location_name) {
  if (!exists("geocode")) {
    stop("A função geocode não está disponível. Verifique se o pacote 'tidygeocoder' foi instalado corretamente.")
  }
  
  resultado <- tibble(location = location_name) %>%
    geocode(location, method = "osm")
  
  return(resultado)
}

#' Salvar dados em arquivo JSON
#'
#' Salva os dados fornecidos em formato JSON em um diretório específico.
#'
#' @param data Dados a serem salvos (em formato R, geralmente uma lista ou data.frame).
#' @param file_name Nome do arquivo (sem a extensão .json).
#' @return Nenhum valor de retorno; a função salva o arquivo no diretório.
save_json <- function(data, file_name) {
  directory <- get_data_directory()
  
  # Criar diretório se não existir
  if (!dir.exists(directory)) {
    dir.create(directory, recursive = TRUE)
  }
  
  # Construir caminho completo do arquivo
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  # Salvar os dados em JSON
  write_json(data, file_path, pretty = TRUE, auto_unbox = TRUE)
  
  cat("Dados salvos em:", file_path, "\n")
}

#' Carregar dados de um arquivo JSON
#'
#' Lê os dados de um arquivo JSON localizado em um diretório específico.
#'
#' @param file_name Nome do arquivo (sem a extensão .json).
#' @return Os dados lidos do arquivo ou NULL se o arquivo não for encontrado.
load_json <- function(file_name) {
  directory <- get_data_directory()
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  if (file.exists(file_path)) {
    data <- fromJSON(file_path)
    return(data)
  } else {
    cat("Arquivo não encontrado:", file_path, "\n")
    return(NULL)
  }
}

#' Obter previsão meteorológica
#'
#' Faz uma requisição à API do OpenWeatherMap para obter dados meteorológicos com base na latitude e longitude.
#'
#' @param lat Latitude do local.
#' @param lon Longitude do local.
#' @param api_key Chave de API para o OpenWeatherMap.
#' @return Dados meteorológicos em formato de texto ou mensagem de erro.
obter_previsao <- function(lat, lon, api_key) {
  url <- paste0("https://api.openweathermap.org/data/2.5/weather?",
                "lat=", lat,
                "&lon=", lon,
                "&appid=", api_key,
                "&lang=pt_br",
                "&units=metric")
  
  resposta <- GET(url)
  
  if (status_code(resposta) == 200) {
    dados <- content(resposta, as = "text", encoding = "UTF-8")
    # Salva os dados meteorológicos em um arquivo JSON (nome: "dados_climaticos.json")
    save_json(dados, "dados_climaticos")
    return(dados)
  } else {
    stop("Erro na requisição da API. Status: ", status_code(resposta))
  }
}

#' Processar dados meteorológicos
#'
#' Processa os dados meteorológicos em JSON e converte para um data.frame.
#'
#' @param json_dados Dados em JSON.
#' @return Um data.frame com os dados meteorológicos processados.
processar_dados_clima <- function(json_dados) {
  dados_lista <- fromJSON(json_dados, simplifyVector = FALSE)
  
  # Exibir a estrutura dos dados para diagnóstico
  str(dados_lista)
  
  if (!is.null(dados_lista$weather) && length(dados_lista$weather) > 0) {
    weather_list <- dados_lista$weather[[1]]
    clima_descricao <- weather_list$description
    clima_tipo <- weather_list$main
  } else {
    clima_descricao <- NA
    clima_tipo <- NA
  }
  
  dados_clima <- data.frame(
    Cidade = dados_lista$name,
    Pais = dados_lista$sys$country,
    Latitude = dados_lista$coord$lat,
    Longitude = dados_lista$coord$lon,
    Temperatura = dados_lista$main$temp,
    Sensacao_Termica = dados_lista$main$feels_like,
    Temp_Minima = dados_lista$main$temp_min,
    Temp_Maxima = dados_lista$main$temp_max,
    Pressao_Atmosferica = dados_lista$main$pressure,
    Umidade = dados_lista$main$humidity,
    Visibilidade = dados_lista$visibility,
    Velocidade_do_Vento = dados_lista$wind$speed,
    Direcao_do_Vento = dados_lista$wind$deg,
    Cobertura_de_Nuvens = dados_lista$clouds$all,
    Descricao_do_Clima = clima_descricao,
    Tipo_de_Clima = clima_tipo,
    Nascer_do_Sol = as.POSIXct(dados_lista$sys$sunrise, origin = "1970-01-01", tz = "GMT"),
    Por_do_Sol = as.POSIXct(dados_lista$sys$sunset, origin = "1970-01-01", tz = "GMT"),
    Fuso_Horario = dados_lista$timezone
  )
  
  return(dados_clima)
}

#' Obter diretório de dados
#'
#' Retorna o caminho do diretório onde os arquivos JSON serão armazenados.
#'
#' @return Caminho absoluto do diretório de dados.
get_data_directory <- function() {
  # Definir o caminho base para salvar os arquivos JSON
  base_dir <- file.path("~", "Documents", "GitHub", "farm_tec_solution", "dados")
  
  # Normalizar o caminho para compatibilidade
  normalized_dir <- normalizePath(base_dir, mustWork = FALSE)
  
  # Criar o diretório, se não existir
  dir.create(normalized_dir, showWarnings = FALSE, recursive = TRUE)
  
  return(normalized_dir)
}

