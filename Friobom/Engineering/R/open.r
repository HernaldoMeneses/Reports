# caminho_para_csv <- "caminho/do/seu/arquivo.csv"
caminho_para_csv <- "L:\\Friobom\\Engineering\\data\\322_17_3809_d_Venda_Superv_RCA.csv"

# Use a função read.csv() para ler o CSV
conjunto_de_dados <- read.csv(caminho_para_csv)

# Exibindo as primeiras linhas do conjunto de dados
head(conjunto_de_dados)

library(ggplot2)
ggplot(conjunto_de_dados, aes(x = DESCRICAO, y = QTCLIPOS)) +
  geom_point() +
  ggtitle("Gráfico de Dispersão")
