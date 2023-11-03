import cv2

ruta_imagen = R"C:\Users\Kevin\Desktop\lena.png"
ruta_guardado_canny = R"C:\Users\Kevin\Desktop\lena_canny.png"

# Cargar la imagen desde la ruta especificada
imagen = cv2.imread(ruta_imagen)

# Verificar si la carga de la imagen fue exitosa
if imagen is None:
    print("No se pudo cargar la imagen. Verifica la ruta o el formato de archivo.")
else:
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar detección de bordes usando Canny
    bordes = cv2.Canny(imagen_gris, 100, 200)  # Los umbrales pueden ser ajustados

    # Guardar la imagen con bordes detectados
    cv2.imwrite(ruta_guardado_canny, bordes)

    # Muestra la imagen de bordes en una ventana
    cv2.imshow('Detección de Bordes Canny', bordes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



