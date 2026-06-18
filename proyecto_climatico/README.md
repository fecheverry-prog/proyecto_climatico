Este proyecto es para la clase de Programación Analítica II.
El objetivo del mismo, es analizar el cambio de precipitaciones y temperaturas desde 1980 a 2019 por regiones.
Como primer paso, buscamos en ERA5 los datos de estas dos variables durante este periodo de tiempo.
Luego, importamos las librerias necesarias para llevar a cabo el proyecto.
Nuestro siguiente paso fue subir el archivo a Google Collab para comenzar a analizar que datos contenia y quitar los que no nos servían.
Una vez filtradas las columnas necesarias, se dividió el archivo en 3 distintos, según las siguientes regiones: África, Sudamérica y Europa
Con el fin de comenzar a analizar los datos a profundidad, convertimos el archivo a un Datarame
Nos pareció relevante hacer Data Cleaning, donde cambiamos los nombres de algunas columnas y creamos una función para convertir la temperatura de Kalvin a Celsius.
Previo al análisis fuerte separamos el dataset en décadas para así poder observar los datos de una manera más accesible
Por último, creamos una gráfica de líneas para observar el cambio de temperatura en las distintas decadas por regiones, donde concluimos que en el transcurso de los años no hubo significantes variaciones de la temperatura. Sin embargo, se observan grandes diferencias entre las regiones.
Una vez terminado el análisis del dataset de temperatura comenzamos analizando el de precipitaciones, siguiendo el mismo proceso de Data Cleaning
En el segundo dataset creamos una función para filtrar el archivo en regiones y otro para poder observar los datos estadísticos de el dataset.
De igual manera, se creó una función lambda para convertir las precipitaciones de metros a milimetros, con el fin de facilitar el análisis.
En cuanto al análisis, realizamos un grafico de dispersión relacionando la latitud con las precipitaciones observando un gran incremento de precipitación media cerca de la linea del Ecuador.
Por último, realizamos un gráfico de barras separando la precipitación media por regiones, donde se observa a Sudamérica con la mayor media y África con la más baja.
