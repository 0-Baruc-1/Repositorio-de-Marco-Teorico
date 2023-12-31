# Marco teórico

## Pixel:

Un píxel, abreviatura de "elemento de imagen" en inglés (picture element), es la unidad más pequeña de una imagen digital o de pantalla. Es un punto individual en una cuadrícula bidimensional que representa un color o una parte de una imagen. Los píxeles son los bloques fundamentales de construcción de imágenes digitales y se utilizan para representar todo, desde texto y gráficos hasta fotografías y videos en formatos digitales.

Cada píxel en una imagen digital contiene información sobre su color, que puede expresarse mediante valores numéricos, como los componentes de color rojo, verde y azul (RGB) en imágenes en color. En imágenes en blanco y negro, un píxel puede representar niveles de gris en una escala de 0 (negro) a 255 (blanco).

La resolución de una imagen se mide en términos de la cantidad de píxeles en ancho y alto, como "1920x1080", que indica una imagen de 1920 píxeles de ancho por 1080 píxeles de alto. Cuanto mayor sea la cantidad de píxeles por unidad de área en una imagen, mayor será su calidad y nitidez cuando se visualice o imprima. Los monitores, pantallas de teléfonos, cámaras digitales y otros dispositivos visuales utilizan matrices de píxeles para crear representaciones visuales de información.

## Imagen Digital: 
Una imagen en el procesamiento de imágenes es una representación digital que se almacena en la memoria de una computadora. Cada píxel en la imagen se representa mediante números, donde los números pueden corresponder a colores (en imágenes a color) o niveles de gris (en imágenes en blanco y negro o en escala de grises).

## Matriz de Píxeles: 
Una imagen se organiza en una cuadrícula bidimensional de píxeles. Cada píxel tiene una posición única en la matriz y se caracteriza por su valor numérico. La matriz de píxeles es esencial para el procesamiento y análisis de imágenes, ya que permite aplicar algoritmos y operaciones matemáticas para modificar o extraer información de la imagen.

### Cómo cargar una imagen en OpenCV
Para cargar una imagen en OpenCV en Python, podemos utilizar el siguiente código de [aquí](https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/Cargar%20imagen.py)

## Resolución: 
La resolución de una imagen se refiere a la cantidad de píxeles que contiene. Una imagen de alta resolución tiene más píxeles y, por lo tanto, puede mostrar detalles más finos que una imagen de baja resolución.

### Transformación de escala para cambiar la resolución

La transformación de escala es una técnica fundamental en el procesamiento de imágenes que permite cambiar el tamaño de una imagen, ya sea para hacerla más grande (ampliación) o más pequeña (reducción). Esta operación es comúnmente utilizada para adaptar imágenes a diferentes tamaños de visualización, ajustar la resolución o preparar datos para análisis y procesamiento.

### Interpolación en la Transformación de Escala

La transformación de escala implica ajustar las coordenadas de los píxeles en la imagen original para que se ajusten a las nuevas dimensiones. Esto a menudo implica la necesidad de calcular valores de píxeles en coordenadas no enteras. Para hacerlo, se utiliza la técnica de interpolación, que estima los valores de píxeles intermedios en función de los valores de píxeles conocidos.

Existen diferentes métodos de interpolación, siendo los más comunes:

- **Interpolación Nearest-Neighbor:** Este método asigna a cada píxel en la imagen redimensionada el valor del píxel más cercano en la imagen original. Es el método más simple pero puede producir resultados pixelados.

- **Interpolación Bilineal:** Este método calcula el valor de un píxel intermedio como una combinación ponderada de los valores de los píxeles vecinos en la imagen original. Produce resultados más suaves que la interpolación Nearest-Neighbor.

- **Interpolación Bicúbica:** Este método utiliza una función cúbica para calcular valores de píxeles intermedios, lo que resulta en una suavidad aún mayor en la imagen redimensionada. Es útil para aplicaciones que requieren una alta calidad de interpolación.

### Proceso de Escala

El proceso de escala se puede dividir en los siguientes pasos:

1. **Definir la Nueva Resolución:** Se especifican las dimensiones deseadas de la imagen redimensionada, es decir, el nuevo ancho y alto.

2. **Calcular la Relación de Escala:** Se calcula la relación entre la nueva resolución y la resolución original. Esta relación determina cómo se estirarán o comprimirán los píxeles en la imagen.

3. **Aplicar la Interpolación:** Para cada píxel en la imagen redimensionada, se calculan sus nuevas coordenadas en la imagen original utilizando la relación de escala. Luego, se utiliza la técnica de interpolación elegida para calcular el valor del píxel en las coordenadas no enteras.

4. **Creación de la Imagen Redimensionada:** Se crea una nueva imagen que contiene los píxeles resultantes del proceso de escala.
Para poder cambiar la resolución de una imagen con OpenCV, podemos usar el siguiente código de [aquí](https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/Cambiar%20resolucion.py). Lo cual queda de la siguiente manera:

<table>
  <tr>
    <td align="center">Imagen con resolución de 512x512</td>
    <td align="center">Imagen con resolución cambiada a 624x624</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/lena.png" alt="Imagen de Ejemplo" width="512"></td>
    <td align="center"><img src="https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/lena_redimensionada.png" alt="Imagen de Ejemplo" width="624"></td>
  </tr>
</table>

### Como calcular la densidad de pixeles

Dimensiones de la imagen: 512x512
Área de la imagen: 262144 píxeles cuadrados
Número total de píxeles: 262144 píxeles
Densidad de píxeles: 1.00 píxeles por unidad de área

## Transformación de Rotación en Procesamiento de Imágenes

La transformación de rotación es una técnica fundamental en el procesamiento de imágenes que permite girar una imagen alrededor de un punto de referencia. Esta operación es útil para corregir la orientación de una imagen, cambiar su perspectiva o realizar análisis en ángulos específicos. En el procesamiento de imágenes, la rotación se realiza utilizando una matriz de transformación que aplica una serie de operaciones geométricas a los píxeles de la imagen.

### Matriz de Rotación

La matriz de rotación es el corazón de la transformación de rotación. Se utiliza para calcular las nuevas coordenadas de los píxeles de la imagen rotada en función de las coordenadas originales y el ángulo de rotación. La matriz tiene la siguiente forma general:

```
| cos(θ)  -sin(θ) |
| sin(θ)   cos(θ) |
```

Donde:
- θ es el ángulo de rotación en sentido antihorario.
- cos(θ) y sin(θ) son las funciones trigonométricas cuyo valor depende del ángulo θ.

### Proceso de Rotación

El proceso de rotación se puede dividir en los siguientes pasos:

1. **Selección del Punto de Rotación:** Se elige un punto central alrededor del cual se realizará la rotación. Este punto puede estar en cualquier lugar de la imagen, pero es común utilizar el centro de la imagen.

2. **Cálculo de la Matriz de Rotación:** Se calcula la matriz de rotación utilizando la fórmula mencionada anteriormente. La matriz se construye en función del ángulo de rotación θ.

3. **Aplicación de la Matriz de Rotación:** Para cada píxel en la imagen original, se calculan sus nuevas coordenadas en la imagen rotada utilizando la matriz de rotación. Esto se hace mediante una multiplicación de matrices.

4. **Interpolación de Píxeles:** Debido a que las coordenadas resultantes de la rotación pueden no ser números enteros, se utiliza la interpolación para calcular el valor de píxel en las coordenadas no enteras. La interpolación puede ser bilineal o basada en otros métodos, y su objetivo es suavizar la imagen rotada.

5. **Creación de la Imagen Rotada:** Se crea una nueva imagen que contiene los píxeles resultantes del proceso de rotación.

Para poder hacer la rotación de una imagen podemos utilizar el siguiente código de [aquí](https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/Transformaci%C3%B3n%20de%20rotaci%C3%B3n.py).

Aquí se puede ver como se aplica en la siguiente imagen:

<table>
  <tr>
    <td align="center">Imagen con resolución de 512x512</td>
    <td align="center">Imagen con resolución cambiada a 624x624</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/lena.png" alt="Imagen de Ejemplo" width="200"></td>
    <td align="center"><img src="https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/lena_rotada.png" alt="Imagen de Ejemplo" width="200"></td>
  </tr>
</table>



## Formatos de archivos de imagen compatibles

OpenCV es compatible con varios formatos de imagen comunes. Algunos formatos requieren bibliotecas auxiliares de terceros para su soporte. Además, la versión 3.0 de OpenCV incluye un controlador para formatos respaldados por la Biblioteca de Abstracción de Datos Geográficos (GDAL), aunque su compatibilidad en Windows aún no ha sido ampliamente probada. En sistemas operativos como Windows y OS X, los códecs que vienen con OpenCV se utilizan de manera predeterminada, mientras que Linux busca códecs instalados en el sistema.

### **Formatos soportados por OpenCV**:

- **Windows bitmaps**: 
  Es un formato de archivo de imagen utilizado principalmente en el sistema operativo Windows. Es conocido por su simplicidad y por ser ampliamente reconocido en varias aplicaciones de Windows.

- **Portable image formats**: 
  Estos son formatos de imagen simplificados que son parte de la familia Netpbm. Se dividen en:
    - **PBM (Portable BitMap)**: Representa una imagen en blanco y negro.
    - **PGM (Portable GrayMap)**: Representa imágenes en escala de grises.
    - **PPM (Portable PixMap)**: Representa imágenes en color.

- **Sun rasters**: 
  Es un formato de archivo de imagen desarrollado por Sun Microsystems y se utiliza principalmente en Solaris (un sistema operativo Unix). Se caracteriza por ser simple y no comprimido.

### **Formatos que necesitan bibliotecas auxiliares**:

- **JPEG (Joint Photographic Experts Group)**: 
  Es un método ampliamente utilizado para la compresión de imágenes fotográficas. Es adecuado para imágenes a color y para imágenes en escala de grises.

- **JPEG 2000**: 
  Es una versión mejorada del formato JPEG estándar. Ofrece una mejor calidad de imagen y una mayor eficiencia de compresión que el JPEG tradicional.

- **Portable Network Graphics (PNG)**: 
  Es un formato de archivo de imagen que utiliza una compresión sin pérdida para mantener la calidad de la imagen. Es el formato recomendado para imágenes que requieren transparencia.

- **TIFF (Tagged Image File Format)**: 
  Es un formato de archivo de imagen flexible que se utiliza para manejar imágenes y datos dentro de un único archivo, con la ayuda de tags (etiquetas). Es adecuado tanto para imágenes en raster como para imágenes en vector.

- **WebP**: 
  Desarrollado por Google, es un formato moderno que proporciona compresión sin pérdida y con pérdida para imágenes en la web. WebP permite una compresión mucho más eficiente que PNG o JPEG, lo que resulta en imágenes de menor tamaño que cargan más rápido.

