import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado_pasa_bajas = R"C:\Users\Kevin\Desktop\lena_pasa_bajas.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Aplicar un desenfoque Gaussiano para funcionar como un filtro pasa bajas
    # El segundo argumento es el tamaño del kernel. Debe ser un número impar.
    # El tercer argumento es la desviación estándar en el eje X; si se pone 0, se calcula a partir del tamaño del kernel.
    imagen_pasa_bajas = cv2.GaussianBlur(imagen, (21, 21), 0)

    # Guardar la imagen con filtro pasa bajas
    cv2.imwrite(ruta_guardado_pasa_bajas, imagen_pasa_bajas)

    # Muestra la imagen con filtro pasa bajas en una ventana
    cv2.imshow('Filtro Pasa Bajas', imagen_pasa_bajas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




