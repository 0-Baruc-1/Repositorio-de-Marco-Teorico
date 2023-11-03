import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado = R"C:\Users\Kevin\Desktop\lena_logaritmica.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)  # Asumiendo que queremos trabajar con escala de grises

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Convertir la imagen a un rango de flotantes de 32 bits para evitar problemas de underflow
    imagen_flotante = np.float32(imagen)
    
    # Normalizar la imagen para que los valores estén entre 1 y la máxima intensidad de un pixel (255 para 8 bits por canal)
    imagen_normalizada = imagen_flotante + 1  # Agregamos 1 para evitar el logaritmo de cero
    
    # Aplicar la transformación logarítmica
    imagen_logaritmica = cv2.log(imagen_normalizada)

    # Escalar el resultado para que esté en el rango de 0 a 255
    imagen_logaritmica = cv2.normalize(imagen_logaritmica, None, 0, 255, cv2.NORM_MINMAX)

    # Convertir de vuelta a 8 bits
    imagen_logaritmica = np.uint8(imagen_logaritmica)
    
    # Guardar la imagen transformada en la ruta especificada
    cv2.imwrite(ruta_guardado, imagen_logaritmica)
    
    # Muestra la imagen original y la imagen transformada en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Transformación Logarítmica', imagen_logaritmica)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
