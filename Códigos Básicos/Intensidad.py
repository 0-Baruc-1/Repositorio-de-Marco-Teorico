import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen original
imagen = cv2.imread(R"C:\Users\Kevin\Desktop\lena.png")

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aumentar la intensidad de la imagen en escala de grises
intensidad_aumentada = cv2.add(imagen_gris, 100)  # Aumenta la intensidad en 50 unidades

# Disminuir la intensidad de la imagen en escala de grises
intensidad_disminuida = cv2.subtract(imagen_gris, 100)  # Disminuye la intensidad en 50 unidades

# Mostrar las imágenes
plt.figure(figsize=(10, 7))

plt.subplot(1, 3, 1)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Imagen Original en Escala de Grises')

plt.subplot(1, 3, 2)
plt.imshow(intensidad_aumentada, cmap='gray')
plt.title('Intensidad Aumentada')

plt.subplot(1, 3, 3)
plt.imshow(intensidad_disminuida, cmap='gray')
plt.title('Intensidad Disminuida')

plt.show()
