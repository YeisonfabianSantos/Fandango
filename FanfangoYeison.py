# creado por Yeison Fabian santos
# Analisis de Fandango
# Abril - 2018


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy import division

######## Codigo de analisis de datos de encuentas de peliculas catalogadas por estrellas ######
######## en el codigo se realiza por medio de los siguientes pasos                    
######## 1) se llama la tabla y se le asigna un nombre
######## 2) de la tabla seleccionamos una columna 'votes' cuyos valores sean mayores a 30
######## 3) nombramos ecuaciones para cada estrella por aparte
######## 4) calculamos el porcentaje de las peliculas en cada estrella 
######## 5) Graficamos porcentaje vs estrellas
######## 6) Analisis en los datos IMDB 


df = pd.read_csv('C:/Users/Yeison/Documents/libros/metodos matematicos/fandango/fandango_scrape.csv')  # Llamamos las tablas
df2 = pd.read_csv('C:/Users/Yeison/Documents/libros/metodos matematicos/fandango/fandango_score_comparison.csv')


votes_over_30 = df[df['VOTES']>30]  # Seleccione los fimls con más de 30 vistas de usuario


#Eleijimos la cantidad de votos en cada  estrellas 
num1 = votes_over_30[votes_over_30['STARS']<=3] 
num2 = votes_over_30[votes_over_30['STARS']<=3.5]
num3 = votes_over_30[votes_over_30['STARS']<=4] 
num4 = votes_over_30[votes_over_30['STARS']<=4.5]
num5 = votes_over_30[votes_over_30['STARS']<=5] 
num6 = votes_over_30[votes_over_30['STARS']<=2] 
num7 = votes_over_30[votes_over_30['STARS']<=1]


# Elija la cantidad de películas en un intervalo determinado
num6 = len(num2)-len(num1)       # Intervalo 3<value<=3.5
num7 = len(num3)-(len(num2))     # Intervalo 3.5<value<=4
num8 = len(num4)-(len(num3))	 # Intervalo 4<value<=4.5
num9 = len(num5)-(len(num4))	 # Intervalo 4.5<value<=5


# Calcule el porcentaje de las PELÍCULAS entre cada rango de número de estrellas
porc_star_3 = (len(num1)/len(votes_over_30))*100
porc_star_35 = (num6/len(votes_over_30))*100
porc_star_4 = (num7/len(votes_over_30))*100
porc_star_45 = (num8/len(votes_over_30))*100
porc_star_5 = (num9/len(votes_over_30))*100


percentage = Series([0.0,0.0,0.0,0.0,0.0,0.0,porc_star_3,porc_star_35,porc_star_4,porc_star_45,porc_star_5]) 


df['Porcentaje'] = pd.Series(['0','','10',' ','20',' ','30',' ','40%',' ']) #definimos los item que van en el eje y
df['Stars'] = pd.Series(["nan"," ","*","** ","*** ","**** ","***** "])  #definimos los item que van en el eje x


percentage.plot(title='Rating for 209 films that played in theaters in 2015 and received 30+ reviews',color='r',figsize=(9,7.5))
ax = plt.axes()
ax.set_xticklabels(df['Stars'],size=15) # Colocamos las etiquetas de estrellas
ax.set_yticklabels(df['Porcentaje'],size=15) # colocamos las etiquetas de porcentaje
plt.suptitle('Fandango´s Lopsided Ratings Curve', size=18)
#plt.legend(['Fandango present rating '],loc = 'upper left')
# definimos los puntos donde ira nuestro mensaje
plt.text(6,28,r"Fandango ",fontsize=12, color="black")   
plt.text(6,26.5,r"presented",fontsize=12, color="black")
plt.text(6,24.8,r"rating",fontsize=12, color="black")
plt.grid()



# analizaremos el numero de votos obtenidos en Metacritic, IMDB y Fandango 


votos_metacritic = df2[df2['Metacritic_user_vote_count']>30] # llamamos todos los votos de metacritic mayores a 30
votos_imdb=df2[df2['IMDB_user_vote_count']>30] #llamamos todos los votos de imdb y lo guardamos en la variable voto_imdb
votos_Fandango=df2[df2['Fandango_votes']>30] #llamamos todos los votos de fandango y lo guardados en la variable voto_fandango


#Declaramos la suma de cada columna y sumamos todos los votos 
A=votos_metacritic.loc[:,'Metacritic_user_vote_count']
B=votos_imdb.loc[:,'IMDB_user_vote_count']
C=votos_Fandango.loc[:,'Fandango_votes']
w=A.sum()+B.sum()+C.sum()


#calculamos el porcentaje para cada uno

porc_votosm = (A.sum()/w)*100
porc_votosi = (B.sum()/w)*100
porc_votosF = (C.sum()/w)*100


por = Series([porc_votosm,porc_votosi,porc_votosF]) # definimos el porcentaje
plt.pie(por,labels=['Metacritic','IMDB','Fandango'])  #escogemos el tipo de grafico
plt.text(0.5,-0.23,r"8,2% ",fontsize=12, color="black")    #localizamos los porcentajes
plt.text(0.5,-0.01,r"0.4%",fontsize=12, color="black")
plt.text(-0.5,0,r"91.4%",fontsize=12, color="black")


# identificamos la cantidad de votos en cada estrellas por separado
n1 = votos_imdb[votos_imdb['IMDB_norm_round']<=2]
n2 = votos_imdb[votos_imdb['IMDB_norm_round']<=2.5] 
n3 = votos_imdb[votos_imdb['IMDB_norm_round']<=3] 
n4 = votos_imdb[votos_imdb['IMDB_norm_round']<=3.5]
n5 = votos_imdb[votos_imdb['IMDB_norm_round']<=4] 
n6 = votos_imdb[votos_imdb['IMDB_norm_round']<=4.5]
n7 = votos_imdb[votos_imdb['IMDB_norm_round']<=5] 
# Elija la cantidad de películas en un intervalo determinado
nu1 = len(n2)-(len(n1))	    # Intervalo 2<value<=2.5 
nu2 = len(n3)-(len(n2))       # intervalo 2.5<value<=3
nu3 = len(n4)-(len(n3))       # Intervalo 3<value<=3.5
nu4 = len(n5)-(len(n4))     # Intervalo 3.5<value<=4
nu5 = len(n6)-(len(n5))	    # Intervalo 4<value<=4.5
nu6 = len(n7)-(len(n6))	    # Intervalo 4.5<value<=5
# Calcule el porcentaje de las PELÍCULAS entre cada rango de número de estrellas
porc_2 = (nu1/len(votos_imdb))*100
porc_25 = (nu2/len(votos_imdb))*100
porc_3 = (nu3/len(votos_imdb))*100
porc_35 = (nu4/len(votos_imdb))*100
porc_4 = (nu5/len(votos_imdb))*100
porc_45 = (nu5/len(votos_imdb))*100
porc_5 = (nu6/len(votos_imdb))*100  
# procentaje
per = Series([0.0,0.0,0.0,porc_2,porc_25,porc_3,porc_35,porc_4,porc_45])



per.plot(title='Rating of IMDB and received 30+ reviews',color='y',figsize=(9,7.5))
ax = plt.axes()
df['Porcentaje'] = pd.Series(['0','0','10','20 ','30','40%','']) #definimos los item que van en el eje y
df['Stars'] = pd.Series([" "," ","*"," ","** "" ","*** "," "," ****"," ","***** ",])  #definimos los item que van en el eje x
ax.set_xticklabels(df['Stars'],size=15) # Colocamos las etiquetas de estrellas
ax.set_yticklabels(df['Porcentaje'],size=15) # colocamos las etiquetas de porcentaje
plt.suptitle('IMDB', size=18)
plt.text(3,28,r"IMDB ",fontsize=12, color="red")
plt.grid()



# La IMDB cueta con un mayor numero de votos para cada estrella, esto ayuda a tener una mejor estadistica de los 
# datos analisados y la aporximacion en los datos es mejor que la ralizada por fandango
# tambien podemos decir que IMDB tiene un mayor numero de seguidores 

