library(tidyverse)
library(corrplot)
library(ggplot2)

vinos <- read.csv("Datasets/0-Descargados/winequality-red.csv")


v <- cor(vinos)
corrplot(v)
view(vinos)

##########################################################
#################### Regresion Lineal ####################
##########################################################

# Regresion lineal (en el shiny las variables las pone el usuario)
R = lm(vinos$fixed.acidity~vinos$density)
# ploteal los puntos
plot(vinos$density, vinos$fixed.acidity)
# Te muestra la linea de regresion
abline(R, col="red", lwd=2)


##########################################################
############### Regresion polinomial #####################
##########################################################

# para ver la regresion del fixed.acidity en relacion a las otras 3 variables
# citric.acid, density, pH

ids <- sample(1:nrow(vinos),size=nrow(vinos)*0.7,replace = FALSE)

entrenamiento <- vinos[ids, c(1,3,8,9)] # se escogen las columnas que se evaluarán (70%)
probar <- vinos[-ids, c(1,3,8,9)] # se escogen las columnas que se evaluarán (30%)

ft = lm(fixed.acidity~ citric.acid + density + pH, data=entrenamiento)

# predecir
predict(ft, probar)
probar$prediccion <- predict(ft, probar)
probar

# Determinar la precision del modelo entrenado (porcentaje)
error <- mean(abs(100*((probar$prediccion - probar$fixed.acidity)/ probar$prediccion)))

accuracy <- 100 - error
accuracy

#############################################
################### KNN #####################
#############################################

library(ggplot2)
library(class)
plot()
# en esta parte seleccionas que variables quieres 
vinosKnn <- data.frame(vinos$fixed.acidity, vinos$density)
dat <- sample(1:nrow(vinosKnn),size=nrow(vinosKnn)*0.7,replace = FALSE)

train <- vinos[dat,] # 70%
test <- vinos[dat,] # 30%

train.labels <- vinos[dat,1]
test.labels <- vinos[-dat,1]

knn <- knn(train=train, test=test, cl=train.labels, k = 10, prob=TRUE)

accuracy.fin <- 100 * sum(train.labels == knn)/NROW(test.labels)
accuracy.fin


##############################################
################### KMeans ###################
##############################################

corrplot(v)
plot(vinos$free.sulfur.dioxide, vinos$sulphates)
df <- data.frame(vinos$free.sulfur.dioxide, vinos$sulphates)

kmeans <- kmeans(df, 7)
plot(df, col = kmeans$cluster)
points(kmeans$centers, col = 1:2, pch = 8, cex = 2)

#############################################
################### PCA #####################
#############################################

# normalizacion de los datos: estandarizacion(variables - promedio)/desv
vinosPCA <- scale(vinos)
pca <- prcomp(vinosPCA)
str(pca)
pca[[1]] # desviaciones
pca[[2]] # rotaciones
pca[[5]] # individuos

# Dependiendo de cuantas componentes se escribe abajo 
componentes <- cbind(pca[[2]][,1],pca[[2]][,2],pca[[2]][,3], pca[[2]][,4])
individuos <- pca[[5]][,c(1:4)]

#install.packages("ade4") 
library(ade4)
# analisis de cluster del componente c1 y c2
s.corcircle(componentes[,c(1,2)]) #Todos los componentes de la col 1 y 2 
s.corcircle(componentes[,c(1,3)])
s.corcircle(componentes[,c(1,4)])
s.corcircle(componentes[,c(1,1)])


#####################################################
################### Knn función #####################
#####################################################

library(ggplot2)
NROW(vinos) 
view(vinos)
x <- vinos$citric.acid # cambiar variables en el shiny
y <- vinos$density # cambiar variables en el shiny

dataframe = data.frame(x, y)

etiquetar <- function(dataframe) {
     grupos <- c()
     for (i in 1:NROW(dataframe)) {
          if(dataframe$x[i]>=min(dataframe$x) & dataframe$x[i]<(max(dataframe$x)*0.4)) {
               grupos <- c(grupos,'A')
          }
          else if(dataframe$x[i]>=(max(dataframe$x)*0.4) & dataframe$x[i]<(max(dataframe$x)*0.6)) {
               grupos <- c(grupos, 'B')
          }
          else grupos <- c(grupos, 'C')
     }
     dataframe <- cbind(dataframe, grupos)
     return(dataframe)
}
dataframe = etiquetar(dataframe)
head(dataframe)

ggplot(data = dataframe,aes(x=dataframe$x,y=dataframe$y,color=dataframe$grupos))+
     geom_point()+xlab("X")+ylab("Y")+ggtitle("Clasificador KNN")

# sacar el 70% y el 30% para entrenamiento y testeo respectivamente
ids=sample(1:nrow(dataframe),size=nrow(dataframe)*0.7,replace = FALSE)

Entrenamiento<-dataframe[ids,]
Test<-dataframe[-ids,]

ggplot(data = Entrenamiento ,aes(x=x,y=y,color=grupos))+
     geom_point()+xlab("X")+ylab("Y")+ggtitle("Clasificador KNN")

dataframe.temporal = dataframe

knn <- function(dataframe.temporal, nuevoX, nuevoY, k, metodo) {
     if (metodo == 1) {
          d <- (abs(nuevoX-dataframe.temporal$x)-abs(nuevoY-dataframe.temporal$y))
     } else {
          d <- sqrt((nuevoX-dataframe.temporal$x)^2 + (nuevoY-dataframe.temporal$y)^2)
     }
     dataframe.temporal <- cbind(dataframe.temporal, d)
     vOrden <- sort(dataframe.temporal$d)
     vecinos <- dataframe.temporal[dataframe.temporal$d %in% vOrden[1:k],3]
     return (vecinos[1:k])
}
v <- knn(dataframe, 7, 13, 1332, 1)
porc<-function(vector,value) {
     return (sum(as.integer(vector==value)))
}
a<-porc(v,"A")
b<-porc(v,"B")
c<-porc(v,"C")
total<-(a+b+c)
a*100/total
b*100/total
c*100/total
