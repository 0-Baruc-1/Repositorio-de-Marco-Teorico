import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado = R"C:\Users\Kevin\Desktop\lena_suavizada.png"  # Ruta donde se guardará la imagen suavizada

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Aplicar suavizado con Filtro Gaussiano a la imagen
    tamaño_kernel = (5, 5)  # Tamaño del kernel para el filtro. Puedes ajustar este valor según tus necesidades.
    desviacion_estandar = 0  # OpenCV calculará automáticamente la desviación estándar basándose en el tamaño del kernel.
    imagen_suavizada = cv2.GaussianBlur(imagen, tamaño_kernel, desviacion_estandar)

    # Guardar la imagen suavizada en la ruta especificada
    cv2.imwrite(ruta_guardado, imagen_suavizada)

    # Muestra la imagen original y la imagen suavizada en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Suavizada', imagen_suavizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()