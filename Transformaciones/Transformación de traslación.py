import cv2
import numpy as np

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado_traslacion = R"C:\Users\Kevin\Desktop\lena_trasladada.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Definir los píxeles de traslación en x e y
    tx, ty = 100, 50  # Ejemplo de traslación de 100 píxeles en x y 50 píxeles en y

    # Crear la matriz de traslación
    M = np.float32([[1, 0, tx], [0, 1, ty]])

    # Aplicar la traslación
    filas, columnas = imagen.shape[:2]
    imagen_trasladada = cv2.warpAffine(imagen, M, (columnas, filas))

    # Guardar la imagen trasladada
    cv2.imwrite(ruta_guardado_traslacion, imagen_trasladada)

    # Muestra la imagen trasladada en una ventana
    cv2.imshow('Imagen Trasladada', imagen_trasladada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


