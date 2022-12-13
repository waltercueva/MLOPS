# Librerias
library(dplyr)

# Cargamos los data.frames
licenciamiento <- read.csv("Datasets/2-Preprocesados/licenciamiento.csv")
carnes <- read.csv("Datasets/2-Preprocesados/carnes.csv")
programas <- read.csv("Datasets/2-Preprocesados/programas.csv")
resumen_sunedu <- read.csv("Datasets/3-Generado/resumen_sunedu.csv")

# Estadistica Descriptiva
# Media, Maximo, Minimo, Cuartil y Percentil de los Programas Universitarios en total de cada universidad
estadistica_programas <- resumen_sunedu %>% summarise(Cantidad = n(),
			Media = mean(PROGRAMAS_TOTAL, na.rm = TRUE),
			Maximo = max(PROGRAMAS_TOTAL, na.rm = TRUE),
			Minimo = min(PROGRAMAS_TOTAL, na.rm = TRUE),
			Q25 = quantile(PROGRAMAS_TOTAL, .25, na.rm = TRUE),
			Q50 = quantile(PROGRAMAS_TOTAL, .50, na.rm = TRUE),
			Q75 = quantile(PROGRAMAS_TOTAL, .75, na.rm = TRUE),)
estadistica_programas

# Media, Maximo, Minimo, Cuartil y Percentil de los Carnes Universitarios en total de cada universidad
estadistica_carnes <- resumen_sunedu %>% summarise(Cantidad = n(),
			Media = mean(CANTIDAD_CARNES, na.rm = TRUE),
			Maximo = max(CANTIDAD_CARNES, na.rm = TRUE),
			Minimo = min(CANTIDAD_CARNES, na.rm = TRUE),
			Q25 = quantile(CANTIDAD_CARNES, .25, na.rm = TRUE),
			Q50 = quantile(CANTIDAD_CARNES, .50, na.rm = TRUE),
			Q75 = quantile(CANTIDAD_CARNES, .75, na.rm = TRUE),)
estadistica_carnes

query <- programas %>%
					filter(NIVEL_ACADEMICO == "DOCTORADO") %>%
					group_by(NOMBRE,NIVEL_ACADEMICO) %>%
					summarize(PROGRAMAS = n()) %>%
					inner_join(licenciamiento %>%
											filter(ESTADO_LICENCIAMIENTO == "LICENCIA OTORGADA") %>%
											select(NOMBRE, ESTADO_LICENCIAMIENTO),
								by=c("NOMBRE"="NOMBRE")) %>%
					inner_join(carnes %>%
										group_by(NOMBRE_UNIVERSIDAD) %>%
										summarize(CANTIDAD_CARNES = sum(Cant_Carnes)),
								by=c("NOMBRE"="NOMBRE_UNIVERSIDAD")) %>%
					select(NOMBRE, NIVEL_ACADEMICO, ESTADO_LICENCIAMIENTO, PROGRAMAS, ALUMNOS = CANTIDAD_CARNES)	
head(query)

query <- licenciamiento %>%
						select(NOMBRE, ESTADO_LICENCIAMIENTO, PERIODO_LICENCIAMIENTO) %>% 
						filter(ESTADO_LICENCIAMIENTO == 'LICENCIA OTORGADA', PERIODO_LICENCIAMIENTO >= 7)
head(query)

query <- programas %>%
					select(NOMBRE, TIPO_GESTION,DENOMINACION_PROGRAMA) %>%
					filter(TIPO_GESTION == 'PUBLICO', DENOMINACION_PROGRAMA == 'INGENIERIA MECANICA')
head(query)
query <- licenciamiento %>% 
						filter(TIPO_GESTION == "PUBLICO", 
								ESTADO_LICENCIAMIENTO == "LICENCIA OTORGADA",
								DEPARTAMENTO_LOCAL != "LIMA") %>%
						select(NOMBRE,TIPO_GESTION,ESTADO_LICENCIAMIENTO,DEPARTAMENTO_LOCAL) %>%
						inner_join(carnes %>%
										filter(NOMBRE_CLASE_PROGRAMA != "SALUD")%>%
										group_by(NOMBRE_UNIVERSIDAD, ) %>%
										summarize(ESTUDIANTES = sum(Cant_Carnes)),
									by=c("NOMBRE"="NOMBRE_UNIVERSIDAD")) %>%
						arrange(desc(ESTUDIANTES))
head(query)

query <- licenciamiento %>%
						select(NOMBRE, DEPARTAMENTO_LOCAL, ESTADO_LICENCIAMIENTO) %>%
						filter(DEPARTAMENTO_LOCAL == 'ICA', ESTADO_LICENCIAMIENTO == 'LICENCIA DENEGADA')
head(query)

query <- licenciamiento %>% 
						filter(DEPARTAMENTO_LOCAL != "LIMA", ESTADO_LICENCIAMIENTO!="LICENCIA OTORGADA") %>%
						group_by(DEPARTAMENTO_LOCAL) %>%
						summarize(UNIVERSIDADES = n()) %>%
						filter(UNIVERSIDADES == first(licenciamiento %>% 
												filter(DEPARTAMENTO_LOCAL != "LIMA",
														ESTADO_LICENCIAMIENTO!="LICENCIA OTORGADA") %>%
												group_by(DEPARTAMENTO_LOCAL) %>%
												summarize(UNIVERSIDADES = n()) %>%
												summarize (MAX = max(UNIVERSIDADES))))
head(query)

