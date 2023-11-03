import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_imagen_guardada = R"C:\Users\Kevin\Desktop\lena_ecualizada.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Convertir la imagen a YCrCb
    imagen_ycrcb = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)

    # Ecualizar el canal Y (luminancia)
    imagen_ycrcb[:,:,0] = cv2.equalizeHist(imagen_ycrcb[:,:,0])

    # Convertir la imagen ecualizada de vuelta a BGR
    imagen_ecualizada = cv2.cvtColor(imagen_ycrcb, cv2.COLOR_YCrCb2BGR)

    # Guardar la imagen ecualizada en la ruta especificada
    cv2.imwrite(ruta_imagen_guardada, imagen_ecualizada)

    # Muestra la imagen original y la imagen ecualizada en ventanas separadas
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Imagen Ecualizada', imagen_ecualizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()