# **WeedTips**

![](gettyimages-1074231984-612x612.jpg)





****WeedTips es un sistema de recomendación de marihuana medicinal basado en contenidos.** 

Este sistema de recomendación tiene como objetivo, dar a conocer cepas de marihuana para las condiciones particulares que demanda el usuario de marihuana medicinal debido a que existen más de 2,000 cepas diferentes. Por lo tanto, el systema ahorra tiempo y disminuye las opciones de cepas, las cuales se perfilan como las mejores opciones para el usuario.

# Sistema de recomendación.

Para lograr el sistema de recomendación se ralizó lo siguiente:

## Paso 1 - Obtencion de datos 

Los datos utilizados para el sistema, es un conjunto de datos obtenidos de Kaggle y Leafly. 

(La licencia se encuentra en la carpeta de datos)

## Paso 2 - Limpieza y preparación de datos

Para poder utilizar los datos que obtuvimos, se límito a q todas las cepas que tuvieran la información de: Efecto, Tratamiento y Sabor, las cuales después de la limpieza no presentaron datos nulos. Además se imputaron datos de concetraciones de THC y CBD.

Por otro Lado los datos con los que se pretendía trabajar eran solamente palabras, por lo que se realizó un porcesamiento de lenguaje natural (NLP) donde las palabras fueron tokenizadas, lematizadas y vectorizadas para poder utilizarlas en el modelo de machine learning. 

## Paso 3 - K-Nearest-Neighbor

Para poder realizar una recomendación, se utilizó KNN de la librería Scikit-Learn, un modelo de machine learning no supervisado el cual calcula la las distancias entre un nuevo punto dado -que para el sistema puede ser el tratamiento para el que utiliza la marihuana, el efecto y el sabor- y los puntos con los que se entrenó el modelo para saber cuales son los puntos más cercanos y realizar una recomendación al usuario. 

## Paso 4 - Web app

Realicé una webb app en flask, con su respectivo HTML donde se puede probar el sistema de recomendación. 

Para poder probar el systema, se tiene que ejecutar las lineas de codigo de "Recomendacin con KNN.ipynb" que se encuentra en el repositorio. 

## Perspectivas

WeedTip es un prototipo el cuál puede crecer enormemente junto con quien se animé a aplicarlo en su negocio de Marihuana Medicinal, este sistema tiene la capacidad de escalar a un sistema de recomendación donde se tome en cuenta a los usuarios y se puedan realizar recomendaciones basados en usuarios, objetos, etc... Además me encuentro trabajando en realizar sistemas de recomendación a mano comparando la similtud de los cosenos de las palabras vectorizadas y con otros modelos de machine learning.



WeedTips fue presentado en el HackShow del bootcamp de Data Analytics de Ironhack, el cual fué seleccionado como proyecto ganador. 

Puede ver la transimsión del Facebook Live aquí: 

https://www.facebook.com/ironhackMEX/videos/256610985542359/

