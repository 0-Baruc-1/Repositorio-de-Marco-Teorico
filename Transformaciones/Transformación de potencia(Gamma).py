import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado = R"C:\Users\Kevin\Desktop\lena_gamma.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Especificar el valor gamma
    gamma = 2.2
    
    # Construir una tabla de búsqueda para mapear los valores de píxeles según la transformación de potencia
    tabla_gamma = np.array([((i / 255.0) ** (1.0 / gamma)) * 255
                            for i in np.arange(0, 256)]).astype("uint8")
    
    # Aplicar la corrección gamma usando la tabla de búsqueda
    imagen_gamma = cv2.LUT(imagen, tabla_gamma)
    
    # Guardar la imagen con la transformación de potencia
    cv2.imwrite(ruta_guardado, imagen_gamma)
    
    # Muestra la imagen original y la imagen con la transformación de potencia en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Corrección Gamma', imagen_gamma)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    
