# Carregar pacotes necessários
library(jsonlite)
library(fs)
library(here)
library(dplyr)

# Função para encontrar o arquivo recursivamente
encontrar_arquivo <- function(nome_arquivo, raiz_busca=".") {
  raiz_busca <- path_abs(raiz_busca)  # Obtém o caminho absoluto da raiz de busca
  
  # Buscar recursivamente pelo arquivo
  arquivos_encontrados <- dir_ls(raiz_busca, recurse = TRUE, glob = nome_arquivo)
  
  if (length(arquivos_encontrados) > 0) {
    paste(arquivos_encontrados[1])
    return(arquivos_encontrados[1])
  } else {
    print(paste("❌ Erro: Arquivo", nome_arquivo, "não encontrado dentro de", raiz_busca))
    return(NULL)
  }
}

# Definir o caminho do arquivo de funções (utilizando 'here' para resolução do caminho)
caminho_funcoes_relativo <- here("R", "funcoes.R")  # Caminho relativo do arquivo

# Exibir o caminho absoluto antes de carregar o script
caminho_funcoes_absoluto <- path_abs(caminho_funcoes_relativo)  # Obtém o caminho absoluto
paste(caminho_funcoes_absoluto)

# Definir o caminho do arquivo JSON de entrada
arquivo_json_relativo <- here("dados", "resultado.json")  # Caminho relativo do arquivo

# Exibir o caminho absoluto do arquivo JSON
arquivo_json_absoluto <- path_abs(arquivo_json_relativo)  # Obtém o caminho absoluto
paste("📂 Caminho absoluto do arquivo JSON:", arquivo_json_absoluto)

# Ler o arquivo JSON e converter em um dataframe
df_resultado <- processar_json(arquivo_json_absoluto)
df_resultado

media = mean(df_resultado$adubo_quantidade_kg)
media
# Calcular as estatísticas
# Função para calcular as estatísticas de média e desvio padrão
calcular_estatisticas <- function(df) {
  
  # Selecionar apenas as colunas numéricas
  df_numeric <- df %>% select(where(is.numeric))
  
  # Calcular as estatísticas de média e desvio padrão
  estatisticas <- df_numeric %>%
    summarise(across(everything(), list(media = ~mean(. , na.rm = TRUE), 
                                        desvio = ~sd(. , na.rm = TRUE))))
  
  return(estatisticas)
}

# Exibir as estatísticas
estatisticas_resultado <- calcular_estatisticas(df_resultado)
estatisticas_resultado

# Converter as estatísticas para JSON
estatisticas_json <- toJSON(estatisticas_resultado, pretty = TRUE)
data <- estatisticas_json

save_json(data, "estatistica")

