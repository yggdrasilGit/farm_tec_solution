# Carregar pacotes necessários
library(jsonlite)
library(fs)
library(here)

#' Encontrar arquivo recursivamente
#'
#' Procura por um arquivo dentro da estrutura do projeto a partir de uma raiz especificada.
#'
#' @param nome_arquivo Nome do arquivo a ser encontrado.
#' @param raiz_busca Diretório raiz para iniciar a busca (padrão é ".").
#' @return Caminho absoluto do arquivo se encontrado, ou NULL se não encontrado.
encontrar_arquivo <- function(nome_arquivo, raiz_busca = ".") {
  raiz_busca <- path_abs(raiz_busca)  # Obtém o caminho absoluto da raiz de busca
  
  # Buscar recursivamente pelo arquivo usando glob
  arquivos_encontrados <- dir_ls(raiz_busca, recurse = TRUE, glob = nome_arquivo)
  
  if (length(arquivos_encontrados) > 0) {
    caminho <- arquivos_encontrados[1]
    message("✅ Arquivo encontrado: ", caminho)
    return(caminho)
  } else {
    message("❌ Erro: Arquivo ", nome_arquivo, " não encontrado dentro de ", raiz_busca)
    return(NULL)
  }
}

#' Calcular estatísticas de um dataframe
#'
#' Seleciona as colunas numéricas de um dataframe e calcula a média e o desvio padrão.


# --- Execução do Script ---

# Definir o caminho do arquivo de funções (utilizando 'here' para resolução do caminho)
caminho_funcoes_relativo <- here("R", "funcoes.R")  # Caminho relativo do arquivo
caminho_funcoes_absoluto <- path_abs(caminho_funcoes_relativo)  # Obtém o caminho absoluto
message("📂 Caminho absoluto do arquivo de funções: ", caminho_funcoes_absoluto)

# Definir o caminho do arquivo JSON de entrada
arquivo_json_relativo <- here("dados", "resultado.json")  # Caminho relativo do arquivo
arquivo_json_absoluto <- path_abs(arquivo_json_relativo)  # Obtém o caminho absoluto
message("📂 Caminho absoluto do arquivo JSON: ", arquivo_json_absoluto)

# Ler o arquivo JSON e converter em um dataframe
# (A função 'processar_json' deve estar definida em 'funcoes.R' ou em outro local)
df_resultado <- processar_json(arquivo_json_absoluto)

# Selecionar apenas as colunas numéricas
colunas_numericas <- sapply(df_resultado, is.numeric)

# Criar um dataframe para armazenar os resultados
resultados <- data.frame(
  coluna = names(df_resultado)[colunas_numericas],  # Nomes das colunas numéricas
  media = sapply(df_resultado[colunas_numericas], function(x) mean(x, na.rm = TRUE)),  # Média
  desvio_padrao = sapply(df_resultado[colunas_numericas], function(x) sd(x, na.rm = TRUE))  # Desvio padrão
)

# Exibir os resultados
print(resultados)


# Converter as estatísticas para JSON
estatisticas_json <- toJSON(resultados, pretty = TRUE, auto_unbox = TRUE)

# Salvar o JSON gerado (a função 'save_json' deve estar definida em 'funcoes.R' ou em outro script)
save_json(estatisticas_json, "estatistica")
