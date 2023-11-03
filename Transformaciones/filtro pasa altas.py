import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado_pasa_altas = R"C:\Users\Kevin\Desktop\lena_pasa_altas.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Primero, aplicamos un desenfoque Gaussiano para obtener la versión de baja frecuencia de la imagen
    imagen_desenfocada = cv2.GaussianBlur(imagen, (21, 21), 0)
    
    # Restamos la imagen desenfocada de la original para obtener el filtro de alta frecuencia (pasa altas)
    imagen_pasa_altas = cv2.subtract(imagen, imagen_desenfocada)
    
    # Incrementar el contraste para visualizar mejor el efecto del filtro pasa altas
    imagen_pasa_altas = cv2.convertScaleAbs(imagen_pasa_altas, alpha=1.5, beta=0)

    # Guardar la imagen con filtro pasa altas
    cv2.imwrite(ruta_guardado_pasa_altas, imagen_pasa_altas)

    # Muestra la imagen con filtro pasa altas en una ventana
    cv2.imshow('Filtro Pasa Altas', imagen_pasa_altas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()







