# Segmentacion-de-heridas
Tesis segmentación y estimación de heridas crónicas con procesamiento de imágenes usando métodos tradicionales
# Marco teórico
## Imagen Digital: 
Una imagen en el procesamiento de imágenes es una representación digital que se almacena en la memoria de una computadora. Cada píxel en la imagen se representa mediante números, donde los números pueden corresponder a colores (en imágenes a color) o niveles de gris (en imágenes en blanco y negro o en escala de grises).


### Cómo cargar una imagen en OpenCV
Para cargar una imagen en OpenCV en Python, podemos utilizar el siguiente código [aquí](https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/Cargar%20imagen.py)

## Resolución: 
La resolución de una imagen se refiere a la cantidad de píxeles que contiene. Una imagen de alta resolución tiene más píxeles y, por lo tanto, puede mostrar detalles más finos que una imagen de baja resolución.

### Como cambiar la resolución en OpenCv
Para poder cambiar la resolución de una imagen con OpenCV, podemos usar el siguiente código [aquí](https://github.com/0-Baruc-1/Segmentacion-de-heridas/blob/main/Metodos/Cambiar%20resolucion.py)


## Matriz de Píxeles: 
Una imagen se organiza en una cuadrícula bidimensional de píxeles. Cada píxel tiene una posición única en la matriz y se caracteriza por su valor numérico. La matriz de píxeles es esencial para el procesamiento y análisis de imágenes, ya que permite aplicar algoritmos y operaciones matemáticas para modificar o extraer información de la imagen.

## Formatos de archivos de imagen compatibles

OpenCV es compatible con varios formatos de imagen comunes. Algunos formatos requieren bibliotecas auxiliares de terceros para su soporte. Además, la versión 3.0 de OpenCV incluye un controlador para formatos respaldados por la Biblioteca de Abstracción de Datos Geográficos (GDAL), aunque su compatibilidad en Windows aún no ha sido ampliamente probada. En sistemas operativos como Windows y OS X, los códecs que vienen con OpenCV se utilizan de manera predeterminada, mientras que Linux busca códecs instalados en el sistema.

### **Formatos soportados por OpenCV**:

- **Windows bitmaps**: 
  - Es un formato de archivo de imagen utilizado principalmente en el sistema operativo Windows. Es conocido por su simplicidad y por ser ampliamente reconocido en varias aplicaciones de Windows.

- **Portable image formats**: 
  - Estos son formatos de imagen simplificados que son parte de la familia Netpbm. Se dividen en:
    - **PBM (Portable BitMap)**: Representa una imagen en blanco y negro.
    - **PGM (Portable GrayMap)**: Representa imágenes en escala de grises.
    - **PPM (Portable PixMap)**: Representa imágenes en color.

- **Sun rasters**: 
  - Es un formato de archivo de imagen desarrollado por Sun Microsystems y se utiliza principalmente en Solaris (un sistema operativo Unix). Se caracteriza por ser simple y no comprimido.

### **Formatos que necesitan bibliotecas auxiliares**:

- **JPEG (Joint Photographic Experts Group)**: 
  - Es un método ampliamente utilizado para la compresión de imágenes fotográficas. Es adecuado para imágenes a color y para imágenes en escala de grises.

- **JPEG 2000**: 
  - Es una versión mejorada del formato JPEG estándar. Ofrece una mejor calidad de imagen y una mayor eficiencia de compresión que el JPEG tradicional.

- **Portable Network Graphics (PNG)**: 
  - Es un formato de archivo de imagen que utiliza una compresión sin pérdida para mantener la calidad de la imagen. Es el formato recomendado para imágenes que requieren transparencia.

- **TIFF (Tagged Image File Format)**: 
  - Es un formato de archivo de imagen flexible que se utiliza para manejar imágenes y datos dentro de un único archivo, con la ayuda de tags (etiquetas). Es adecuado tanto para imágenes en raster como para imágenes en vector.

- **WebP**: 
  - Desarrollado por Google, es un formato moderno que proporciona compresión sin pérdida y con pérdida para imágenes en la web. WebP permite una compresión mucho más eficiente que PNG o JPEG, lo que resulta en imágenes de menor tamaño que cargan más rápido.

