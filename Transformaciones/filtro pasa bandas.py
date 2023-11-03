import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado_pasa_banda = R"C:\Users\Kevin\Desktop\lena_pasa_banda.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Filtro pasa bajos - Desenfoque Gaussiano
    baja_frecuencia = cv2.GaussianBlur(imagen_gris, (21, 21), 0)

    # Filtro pasa altos - Restar el desenfoque del original
    alta_frecuencia = cv2.subtract(imagen_gris, baja_frecuencia)
    
    # Combinar los dos para crear un filtro pasa banda
    # Aquí, puedes ajustar cómo de fuerte quieres que cada componente contribuya
    # Esto se puede hacer ajustando los pesos en la función addWeighted
    pasa_banda = cv2.addWeighted(imagen_gris, 0.5, alta_frecuencia, 0.5, 0)

    # Guardar la imagen filtrada
    cv2.imwrite(ruta_guardado_pasa_banda, pasa_banda)

    # Muestra la imagen filtrada en una ventana
    cv2.imshow('Filtro Pasa Banda', pasa_banda)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






