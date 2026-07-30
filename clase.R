#A1 
horas_estudio<- read.csv("/home/dereckmera/Downloads/EJERCICIOS/A1_horas_estudio.csv")
media<- mean(horas_estudio$horas_estudio)
#estudiantes de estadistica dedican 9.16 horas a la semana a estudiar.
#mejoro la estimacion puntual
desviacion_estandar<- sd(horas_estudio$horas_estudio)
#estudiantes de estadistica dedican 9.16 horas con una desviacion estandar 
#de 2.41 horas a la semana a estudiar 

#A2
cacao<- read.csv("/home/dereckmera/Downloads/EJERCICIOS/A2_sacos_cacao.csv")
proporcion_cumple<- mean(cacao$cumple_estandar)
proporcion_cumple* 100
#el 76% de los sacos de la muestra (n=25), de la produccion cumple cin los estandares de peso

#A3
ensamblaje<- read.csv("/home/dereckmera/Downloads/EJERCICIOS/A3_ensamblaje.csv")
t_media<- mean(ensamblaje$tiempo_ensamblaje_min)
desviacion_embalaje<- max(ensamblaje$tiempo_ensamblaje_min) - min(ensamblaje$tiempo_ensamblaje_min)
var_t <- var(ensamblaje$tiempo_ensamblaje_min)
sd_t <- sd(ensamblaje$tiempo_ensamblaje_min)
#el tiempo promedio de ensamblaje de una pieza es igual a 9.16 minutos, con una variable de 2.41

#B1
bus<- read.csv("/home/dereckmera/Downloads/EJERCICIOS/B1_espera_bus.csv")
#funcion para intervalos de confianza (t.test)
resultado <- t.test(bus$tiempo_espera_min, conf.level = 0.95)
resultado$conf.int
mean(bus$tiempo_espera_min)
#el tiempo promedio de espera de los pasajeros en la parada x con una muestral
#de 12.91 esta entre 11.60 a 14.21 minutos

#B2
satisfaccion <- read.csv("/home/dereckmera/Downloads/EJERCICIOS/B2_satisfaccion_clientes.csv")
satisfechos<- mean(satisfaccion$satisfecho)
n<-nrow(satisfaccion)
resultado<- prop.test(satisfechos, n, conf.level = 0.95, correct = FALSE)
resultado$conf.int

#B3
agua<- read.csv("/home/dereckmera/Downloads/EJERCICIOS/B3_consumo_agua.csv")
consumo<- t.test(agua$consumo_agua_m3,conf.level = 0.90)
consumo_rango<- consumo$conf.int
#18 a 20.2 metros cubicos de consumo
20.2-18
#rango
consumo2<- t.test(agua$consumo_agua_m3,conf.level = 0.95)
consumo2_rango<- consumo2$conf.int
#17.8 a 20.4 metro cubicos de consumo 
20.4-17.8
#rango es de2.6 m
