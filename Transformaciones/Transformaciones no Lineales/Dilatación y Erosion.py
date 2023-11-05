import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Documents\train\mejor\best_mask_for_0111.png"
ruta_guardado_erosion = R"C:\Users\Kevin\Desktop\lena_erosionada.png"
ruta_guardado_dilatacion = R"C:\Users\Kevin\Desktop\lena_dilatada.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Definir el kernel o elemento estructurante para los filtros morfológicos
    kernel = np.ones((10,10), np.uint8)

    # Aplicar erosión
    imagen_erosionada = cv2.erode(imagen, kernel, iterations=1)
    # Guardar la imagen erosioanda
    cv2.imwrite(ruta_guardado_erosion, imagen_erosionada)

    # Aplicar dilatación
    imagen_dilatada = cv2.dilate(imagen, kernel, iterations=1)
    # Guardar la imagen dilatada
    cv2.imwrite(ruta_guardado_dilatacion, imagen_dilatada)
    
    # Muestra las imágenes en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Erosionada', imagen_erosionada)
    cv2.imshow('Imagen Dilatada', imagen_dilatada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

