library(ggplot2)
#install.packages("plotly")
library(plotly)
library(dplyr)
#Francescco y Renzo 
# Cargamos los data.frames
licenciamiento <- read.csv("Datasets/2-Preprocesados/licenciamiento.csv")
carnes <- read.csv("Datasets/2-Preprocesados/carnes.csv")
programas <- read.csv("Datasets/2-Preprocesados/programas.csv")
resumen_sunedu <- read.csv("Datasets/3-Generado/resumen_sunedu.csv")


# 1- Tipo de departamento filial segun universidades publicas con carrera en Ingenieria Mecánica
q3 <- programas %>% select(CODIGO_ENTIDAD, NOMBRE, NOMBRE_FILIAL, NIVEL_ACADEMICO) %>% 
            filter(programas$TIPO_GESTION == 'PUBLICO', 
            programas$DENOMINACION_PROGRAMA == 'INGENIERIA MECANICA')
grafico <- ggplot(q3, aes(y=NOMBRE, x=NOMBRE_FILIAL)) + 
            theme_minimal() + geom_point(color="red",size=7) + 
            labs(y="Universidades", x="Departamento Filial", 
            title="A que departamento Filial pertenecen las Universidades publicas con Mecánica")
grafico
# Interpretacion: Muestra que filia esta asociada a las universidades publicas con la carrea Mecatronica

# 2- grafico de pie de licenciamiento de universidades
grafico2 <- ggplot(licenciamiento, aes(x='', y=ESTADO_LICENCIAMIENTO, fill=ESTADO_LICENCIAMIENTO)) + 
                        geom_bar(stat='identity', color='white') + coord_polar(theta='y') + labs(title='Pie de Licenciamiento')
grafico2
# Interpretacion: Muestra un pie con los percentajes de las licencias otorgadas (o denegadas) a las Universidades segun la SUNEDU
# Se puede ver como la mayoria de universidades fueron licenciadas, con mas del 55% son solo licenciaturas otorgadas.


# 3- Cuantas universidades por departamento hay
grafico3 <- ggplot(licenciamiento, aes(x=licenciamiento$NOMBRE, y=licenciamiento$DEPARTAMENTO_LOCAL, fill=DEPARTAMENTO_LOCAL)) + 
                geom_bar(stat='identity', color='white') + labs(y = "Departamentos", x = "Universidades",
                title='Universidades por departamento')
grafico3
# Interpretacion: Cuantas universidades hay por departamento con barras. Se puede ver como LIMA es la que cuenta con mas universidades.
# Sin embargo es complicado ver las demas, por lo que se creo el grafico de pie.

# 4- Cuantas universidades por departamento hay en porcentaje (pie)
grafico4 <- ggplot(licenciamiento, aes(x=DEPARTAMENTO_LOCAL, y='', fill=DEPARTAMENTO_LOCAL)) + 
                geom_bar(stat='identity', color='white') + coord_polar(theta='x') + 
                 labs(y='',x='Departamentos', 
                        title='Universidades según departamento')
grafico4
# Interpretacion: Se puede ver como en segundo lugar esta La Libertad y Junin empatados, y en tercer lugar esta Arequipa

# 5- Porcentaje de periodos de licenciamiento
y <- licenciamiento %>% group_by(PERIODO_LICENCIAMIENTO, ESTADO_LICENCIAMIENTO) %>% summarise(suma_lic=sum(PERIODO_LICENCIAMIENTO))
grafico5 <- ggplot(y, aes(y='',x=suma_lic, fill=PERIODO_LICENCIAMIENTO)) + 
                geom_bar(stat="identity", color='white') + coord_polar(theta='x') + 
                        labs(y='Publico vs Privado',x='Numero de años totales en licenciamiento', 
                        title='Periodo de licenciamiento de Universidades')
grafico5
