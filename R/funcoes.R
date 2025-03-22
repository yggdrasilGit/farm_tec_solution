# Definir a função para ler JSON e converter para data.frame
ler_json_para_dataframe <- function(caminho_arquivo) {
  # Verifica se o arquivo existe
  if (!file.exists(caminho_arquivo)) {
    stop("O arquivo JSON não foi encontrado.")
  }
  
  # Lendo o arquivo JSON
  dados <- fromJSON(caminho_arquivo)
  
  # Converter para data.frame
  df <- as.data.frame(dados)
  
  return(df)
}

# Exemplo de uso:

# arquivo_json <- "/Users/francismaralvesmartinsjunior/Documents/GitHub/farm-tech-solution/farm-tech-solution-r/data/test.json"
# df_resultado <- ler_json_para_dataframe(arquivo_json)


# funcao retorna um dataframe
library(jsonlite)

processar_json <- function(arquivo) {
  dados <- fromJSON(arquivo, simplifyDataFrame = FALSE)
  
  if (!is.list(dados)) {
    stop("Os dados do JSON não estão no formato esperado.")
  }
  
  resultado <- data.frame(
    cultura = character(),
    area_plantada = numeric(),
    semente_quantidade_kg = numeric(),
    semente_tipo = character(),
    fertilizante_quantidade_kg = numeric(),
    fertilizante_tipo = character(),
    veneno_quantidade_litros = numeric(),
    veneno_tipo = character(),
    adubo_quantidade_kg = numeric(),
    adubo_tipo = character(),
    stringsAsFactors = FALSE
  )
  
  for (i in seq_along(dados)) {
    cultura <- dados[[i]]
    
    if (!is.list(cultura) || !"insumos_utilizados" %in% names(cultura)) {
      next  # Pula a iteração se os dados não estiverem no formato correto
    }
    
    insumos <- cultura$insumos_utilizados
    if (!is.list(insumos)) {
      next
    }
    
    semente_qtd <- NA; semente_tipo <- ""
    fertilizante_qtd <- NA; fertilizante_tipo <- ""
    veneno_qtd <- NA; veneno_tipo <- ""
    adubo_qtd <- NA; adubo_tipo <- ""
    
    for (j in seq_along(insumos)) {
      insumo <- insumos[[j]]
      if (!is.list(insumo) || !"insumo" %in% names(insumo) || !"quantidade_necessaria" %in% names(insumo) || !"descricao" %in% names(insumo)) {
        next
      }
      
      if (grepl("Semente", insumo$insumo)) {
        semente_qtd <- insumo$quantidade_necessaria
        semente_tipo <- insumo$descricao
      } else if (grepl("Fertilizante", insumo$insumo)) {
        fertilizante_qtd <- insumo$quantidade_necessaria
        fertilizante_tipo <- insumo$descricao
      } else if (grepl("Veneno", insumo$insumo)) {
        veneno_qtd <- insumo$quantidade_necessaria
        veneno_tipo <- insumo$descricao
      } else if (grepl("Adubo", insumo$insumo)) {
        adubo_qtd <- insumo$quantidade_necessaria
        adubo_tipo <- insumo$descricao
      }
    }
    
    resultado <- rbind(resultado, data.frame(
      cultura = cultura$cultura,
      area_plantada = cultura$area_plantada,
      semente_quantidade_kg = semente_qtd,
      semente_tipo = semente_tipo,
      fertilizante_quantidade_kg = fertilizante_qtd,
      fertilizante_tipo = fertilizante_tipo,
      veneno_quantidade_litros = veneno_qtd,
      veneno_tipo = veneno_tipo,
      adubo_quantidade_kg = adubo_qtd,
      adubo_tipo = adubo_tipo,
      stringsAsFactors = FALSE
    ))
  }
  
  return(resultado)
}


# Exemplo de uso:
# df_processado <- processar_dataframe(df)
# print(df_processado)

# Função para calcular média e desvio padrão de colunas específicas
# Assumindo que 'df' é o seu data frame carregado com as colunas
# 'area_plantada', 'semente_quantidade_kg', 'fertilizante_quantidade_kg', etc.



# Função para calcular estatísticas apenas para colunas numéricas
# Função para calcular as estatísticas
calcular_estatisticas <- function(df) {
  
  # Inicializar o data frame para armazenar as estatísticas
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

# Exemplo de como aplicar a função
estatisticas_resultado <- calcular_estatisticas(df)

# Exibir as estatísticas
print(estatisticas_resultado)



# Exemplo de uso:
# colunas_para_analisar <- c("rocas.area_plantio", 
#                           "semente_quantidade_kg", 
#                           "fertilizante_quantidade_kg", 
#                           "veneno_quantidade_litros", 
#                           "adubo_quantidade_kg")


# Definir a função para obter coordenadas de um local
get_geocode <- function(location_name) {
  # Verifica se a função geocode existe
  if (!exists("geocode")) {
    stop("A função geocode não está disponível. Verifique se o pacote 'tidygeocoder' foi instalado corretamente.")
  }
  
  # Tenta geocodificar a cidade usando OpenStreetMap (OSM)
  resultado <- tibble(location = location_name) %>%
    geocode(location, method = "osm")
  
  return(resultado)
}


# **Exemplo de uso da função**
# resultado <- get_geocode("Parauna, Brasil")
# print(resultado)




save_json <- function(data, file_name) {
  directory <- get_data_directory()  # Obtém 
  
  # Criar diretório se não existir
  if (!dir.exists(directory)) {
    dir.create(directory, recursive = TRUE)
  }
  
  # Caminho completo do arquivo JSON
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  # Salvar os dados em JSON
  write_json(data, file_path, pretty = TRUE, auto_unbox = TRUE)
  
  cat("Dados salvos em:", file_path, "\n")
}


# Função para carregar dados JSON do diretório específico
load_json <- function(file_name) {
  directory <- get_data_directory()  # Obtém o diretório correto
  
  # Caminho completo do arquivo JSON
  file_path <- file.path(directory, paste0(file_name, ".json"))
  
  # Verificar se o arquivo existe
  if (file.exists(file_path)) {
    data <- fromJSON(file_path)
    return(data)
  } else {
    cat("Arquivo não encontrado:", file_path, "\n")
    return(NULL)
  }
}


# Função para obter dados meteorológicos

# Função para obter dados meteorológicos (API gratuita)


# Função para obter dados meteorológicos
# Função para obter dados meteorológicos
obter_previsao <- function(lat, lon, api_key) {
  # Construir a URL da API
  url <- paste0("https://api.openweathermap.org/data/2.5/weather?",
                "lat=", lat,
                "&lon=", lon,
                "&appid=", api_key,
                "&lang=pt_br",
                "&units=metric")
  
  # Fazer a requisição GET
  resposta <- GET(url)
  
  # Verificar se a requisição foi bem-sucedida
  if (status_code(resposta) == 200) {
    # Obter o conteúdo da resposta
    dados <- content(resposta, as = "text", encoding = "UTF-8")
    
    # Converter o JSON para uma lista R
    dados_json <- save_json(dados, "dados_climaticos")
    
 
      return()
    
  }
}

# processamento climaticp
processar_dados_clima <- function(json_dados) {
  # Converter JSON para lista
  dados_lista <- fromJSON(json_dados, simplifyVector = FALSE)  # Desativa conversão automática para data.frame
  
  # Verificar estrutura dos dados (para diagnóstico)
  str(dados_lista)
  
  # Acessar os dados do clima de forma segura
  if (!is.null(dados_lista$weather) && length(dados_lista$weather) > 0) {
    weather_list <- dados_lista$weather[[1]]  # Pegar o primeiro item da lista
    clima_descricao <- weather_list$description
    clima_tipo <- weather_list$main
  } else {
    clima_descricao <- NA
    clima_tipo <- NA
  }
  
  # Criar data frame com os dados extraídos
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


#buscasr o diretorio data 
get_data_directory <- function() {
  # Defina o caminho base para salvar os arquivos JSON
  base_dir <- file.path("~", "Documents", "GitHub", "farm-tec-solution",)
  
  # Normalizar o caminho para garantir compatibilidade com qualquer SO
  normalized_dir <- normalizePath(base_dir, mustWork = FALSE)
  
  # Criar o diretório, se não existir
  dir.create(normalized_dir, showWarnings = FALSE, recursive = TRUE)
  
  return(normalized_dir)
}


#buscasr o diretorio data 
get_data_directory <- function() {
  # Defina o caminho base para salvar os arquivos JSON
  base_dir <- file.path("~", "Documents", "GitHub", "farm_tec_solution", "dados")
  
  # Normalizar o caminho para garantir compatibilidade com qualquer SO
  normalized_dir <- normalizePath(base_dir, mustWork = FALSE)
  
  # Criar o diretório, se não existir
  dir.create(normalized_dir, showWarnings = FALSE, recursive = TRUE)
  
  return(normalized_dir)
}


