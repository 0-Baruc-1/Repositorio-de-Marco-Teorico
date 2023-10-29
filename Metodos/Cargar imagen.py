import cv2

ruta_imagen = R"C:\Users\Kevin\Documents\train\images\0011.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verifica si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Muestra la imagen en una ventana
    cv2.imshow('Imagen Cargada', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
