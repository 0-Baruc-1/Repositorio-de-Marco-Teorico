import cv2

# Cargar la imagen
ruta_imagen = R"C:\Users\Kevin\Documents\train\images\0011.png"
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Mostrar la resolución original
    alto, ancho = imagen.shape[:2]
    print(f"Resolución original: {ancho}x{alto}")

    # Definir la nueva resolución deseada
    nueva_resolucion = (1024, 1024)  # Cambiar a 1024x1024

    # Redimensionar la imagen a la nueva resolución
    imagen_redimensionada = cv2.resize(imagen, nueva_resolucion)

    # Mostrar la nueva resolución
    alto, ancho = imagen_redimensionada.shape[:2]
    print(f"Nueva resolución: {ancho}x{alto}")

    # Mostrar la imagen redimensionada
    cv2.imshow('Imagen Redimensionada', imagen_redimensionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
