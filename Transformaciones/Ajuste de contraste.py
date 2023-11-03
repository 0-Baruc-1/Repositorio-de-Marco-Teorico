import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado = R"C:\Users\Kevin\Desktop\lena_contrast.png"  # Ruta donde se guardará la imagen modificada

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Ajustar el contraste de la imagen (por ejemplo, factor 1.5)
    factor_contraste = 1.5
    imagen_contraste = cv2.convertScaleAbs(imagen, alpha=factor_contraste, beta=0)

    # Guardar la imagen con contraste ajustado en la ruta especificada
    cv2.imwrite(ruta_guardado, imagen_contraste)

    # Muestra la imagen original y la imagen con contraste ajustado en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen con Contraste Ajustado', imagen_contraste)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
