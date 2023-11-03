import cv2
import numpy as np

# Cargar la imagen
ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Obtener las dimensiones originales de la imagen
    alto, ancho = imagen.shape[:2]

    # Definir el ángulo de rotación en grados
    angulo_rotacion = 90  # Rotar 90 grados en sentido antihorario

    # Calcular el centro de la imagen
    centro = (ancho // 2, alto // 2)

    # Crear una matriz de rotación
    matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)

    # Aplicar la transformación de rotación a la imagen
    imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, alto))

    # Guardar la imagen rotada
    ruta_imagen_rotada = R"C:\Users\Kevin\Desktop\lena_rotada.png"
    cv2.imwrite(ruta_imagen_rotada, imagen_rotada)

    # Mostrar la imagen original y la imagen rotada
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Rotada', imagen_rotada)

    # Espera hasta que se presione una tecla y luego cierra las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"La imagen rotada se ha guardado en: {ruta_imagen_rotada}")
