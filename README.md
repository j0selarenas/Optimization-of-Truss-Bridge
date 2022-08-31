# MCOC2021-P1
**Optimización estructural de un puente reticular**

El presente informe presenta los resultados más relevantes para el desarrollo de la entrega final del Grupo 7, la cual pide diseñar un puente, minimizando el peso y llevando el factor de utilización a valores cercanos a 1. En el transcurso de este proyecto, se logró comprender que debía tener un reticulado para lograr un buen funcionamiento. A continuación, se presentan los diseños realizados hasta llegar al más optimo. 

## Diseño Inicial:
Se utilizo un diseño similar al enseñado en las entregas anteriores, pero este contaba con una mayor longitud.
 
 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture1.png">
  <br><br>
  <b>Imagen 1: Vista en elevación del puente inicial.</b><br>
  <br><br>
 </p>

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture2.png">
  <br><br>
  <b>Imagen 2: Vista superior del puente.</b><br>
 </p>

Con este diseño inicial del puente, se logró cumplir con los requisitos de las combinaciones de carga de 1.4D y 1.2D+1.6L, con un peso total de 502 toneladas aproximadamente.

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture3.jpg">
  <br><br>
  <b>Imagen 3: Peso total del puente inicial.</b><br>
 </p>

A continuación, se muestran los factores de utilización de algunas barras del puente de reticulado junto con los desplazamientos nodales.

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture4.png">
  <br><br>
  <b>Imagen 4: Factores de utilización de algunas barras.</b><br>
  <br><br>
 </p>
 
 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture5.png">
  <br><br>
  <b>Imagen 5: Desplazamientos nodales.</b><br>
 </p>

Se puede ver que en general los FU son muy bajos, por lo que se decidió disminuir el peso de las barras que contaban con un factor de utilización menor, para así disminuir el peso de la estructura y lograr valores de FU cercanos a 1. Para esto, se modificaron las secciones (perfiles) de estas barras, disminuyendo el peso total del puente, en donde se llegó a los siguientes resultados.

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture6.jpg">
  <br><br>
  <b>Imagen 6: Peso total del segundo diseño del puente.</b><br>
  <br><br>
 </p>

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture7.png">
  <br><br>
  <b>Imagen 7: Factores de utilización del segundo diseño del puente.</b><br>
 </p>

Se puede observar que el peso total disminuye notablemente y los FU aumentaron. Sin embargo, se dio cuenta que se podía disminuir el peso de manera más brusca, colocando las secciones óptimas para cada barra según su ubicación en el puente, su factor de utilización y las cargas que están aplicadas sobre ella.

## Diseño Final:
Luego de optimizar la mayor cantidad de barras, una por una, se logró obtener el siguiente modelo.

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture8.png">
  <br><br>
  <b>Imagen 8: Peso total del diseño final del puente.</b><br>
 </p>

Con este, se obtuvieron los siguientes factores de utilización y deformaciones nodales.

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture9.png">
  <br><br>
  <b>Imagen 9: Factores de utilización del diseño final del puente.</b><br>
  <br><br>
 </p>

 <p align="center">
  <img src="https://github.com/JoseLarenas/MCOC2021-P1/blob/main/Picture10.png">
  <br><br>
  <b>Imagen 10: Desplazamiento nodales.</b><br>
 </p>

Se puede observar que en un comienzo se alcanzo un peso de 502 toneladas y finalmente se logro uno de 33 toneladas, lo cual es un valor sumamente bajo, en comparación al valor inicial. Además, es posible notar que los factores de utilización de las barras aumentaron, llegando a valores cercanos a 1, lo cual significa que están en sus condiciones óptimas de diseño para soportar las cargas aplicadas sin sufrir mayores deformaciones, manteniendo un grado de seguridad adecuado.


**Nota:**
Todos los archivos usados para obtener el Diseño Final se encuentran en la carpeta "Entrega 7".
