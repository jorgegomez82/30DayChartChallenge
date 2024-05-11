# Establece el directorio de trabajo
setwd("D:\\30DayChartChallenge\\30DayChartChallenge_Collection2024\\Day21")
getwd()

# Cargar las bibliotecas necesarias
library(ggplot2)
library(dplyr)
library(scales)

# Cargar los datos desde el archivo CSV
data <- read.csv("intermittent-renewables-production-france.csv")

# Convertir la columna Date a formato de fecha
data$Date <- as.Date(data$Date)

# Filtrar los datos para incluir solo el año 2023
data_2023 <- subset(data, as.numeric(format(Date, "%Y")) == 2023)

# Calcular el promedio mensual de producción
monthly_avg <- data_2023 %>%
  group_by(Month = format(Date, "%m"), Source) %>%
  summarise(Avg_Production = mean(Production))

# Definir nombres de meses en inglés
monthly_avg$Month <- factor(monthly_avg$Month, levels = c("01", "02", "03", "04", "05", "06"),
                            labels = c("January", "February", "March", "April", "May", "June"))

# Crear el gráfico de barras
ggplot(monthly_avg, aes(x = Month, y = Avg_Production, fill = Source)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Producción Promedio Mensual de Energía Solar y Eólica en 2023 - Francia",
       x = "Mes",
       y = "Producción Promedio (MW)",
       fill = "Fuente") +
  scale_y_continuous(labels = comma) + # Formatear los números con comas para separar los miles
  theme_minimal()
