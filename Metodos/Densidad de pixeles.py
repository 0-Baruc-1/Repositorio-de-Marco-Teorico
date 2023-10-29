import cv2

# Cargar la imagen
ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Obtener las dimensiones de la imagen
    alto, ancho = imagen.shape[:2]

    # Calcular el área de la imagen (en píxeles cuadrados)
    area_imagen = alto * ancho

    # Calcular el número total de píxeles
    num_pixeles = alto * ancho

    # Calcular la densidad de píxeles
    densidad_pixeles = num_pixeles / area_imagen

    # Mostrar la información
    print(f"Dimensiones de la imagen: {ancho}x{alto}")
    print(f"Área de la imagen: {area_imagen} píxeles cuadrados")
    print(f"Número total de píxeles: {num_pixeles} píxeles")
    print(f"Densidad de píxeles: {densidad_pixeles:.2f} píxeles por unidad de área")

    # Mostrar la imagen
    cv2.imshow('Imagen', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
