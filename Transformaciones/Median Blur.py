import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado = R"C:\Users\Kevin\Desktop\lena_filtrada.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Aplicar el filtro de mediana con un tamaño de kernel 5x5
    imagen_filtrada = cv2.medianBlur(imagen, 5)
    
    # Guardar la imagen con el filtro de mediana aplicado
    cv2.imwrite(ruta_guardado, imagen_filtrada)
    
    # Muestra la imagen original y la imagen filtrada en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen con Filtro de Mediana', imagen_filtrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

