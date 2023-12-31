import cv2

# Cargar la imagen
ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Mostrar la resolución original
    alto, ancho = imagen.shape[:2]
    print(f"Resolución original: {ancho}x{alto}")

    # Definir la nueva resolución deseada
    nueva_resolucion = (624, 624)  # Cambiar a 624x624

    # Redimensionar la imagen a la nueva resolución
    imagen_redimensionada = cv2.resize(imagen, nueva_resolucion)

    # Mostrar la nueva resolución
    alto, ancho = imagen_redimensionada.shape[:2]
    print(f"Nueva resolución: {ancho}x{alto}")

    # Guardar la imagen redimensionada con un nuevo nombre y ruta
    ruta_imagen_redimensionada = R"C:\Users\Kevin\Desktop\lena_redimensionada.png"
    cv2.imwrite(ruta_imagen_redimensionada, imagen_redimensionada)

    # Mostrar la imagen redimensionada
    cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


