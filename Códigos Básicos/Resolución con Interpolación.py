import cv2
import numpy as np

# Cargar la imagen original
imagen_original = cv2.imread(R"C:\Users\Kevin\Desktop\lena.png")

# Definir el factor de ampliación
factor_ampliacion = 2

# Ampliar la imagen sin interpolación (nearest-neighbor upsampling)
# Repetimos cada píxel en el eje x e y de acuerdo al factor de ampliación
altura, ancho = imagen_original.shape[:2]
imagen_sin_interpolacion = np.repeat(np.repeat(imagen_original, factor_ampliacion, axis=0), factor_ampliacion, axis=1)

# Ampliar la imagen con interpolación (por ejemplo, interpolación bilineal)
nueva_ancho = ancho * factor_ampliacion
nueva_alto = altura * factor_ampliacion
imagen_con_interpolacion = cv2.resize(imagen_original, (nueva_ancho, nueva_alto), interpolation=cv2.INTER_LINEAR)

# Guardar las imágenes resultantes
cv2.imwrite(R"C:\Users\Kevin\Desktop\lena1.png", imagen_sin_interpolacion)
cv2.imwrite(R"C:\Users\Kevin\Desktop\lena2.png", imagen_con_interpolacion)

# Mostrar las imágenes
cv2.imshow('Sin Interpolacion', imagen_sin_interpolacion)
cv2.imshow('Con Interpolacion', imagen_con_interpolacion)
cv2.waitKey(0)
cv2.destroyAllWindows()

