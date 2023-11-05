import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen en modo color
imagen = cv2.imread(R"C:\Users\Kevin\Desktop\lena.png")

# OpenCV carga las imágenes en formato BGR, así que la convertimos a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Separar los canales de color
canal_rojo, canal_verde, canal_azul = cv2.split(imagen_rgb)

# Crear una imagen para cada canal de color
imagen_solo_rojo = cv2.merge([canal_rojo, np.zeros_like(canal_verde), np.zeros_like(canal_azul)])
imagen_solo_verde = cv2.merge([np.zeros_like(canal_rojo), canal_verde, np.zeros_like(canal_azul)])
imagen_solo_azul = cv2.merge([np.zeros_like(canal_rojo), np.zeros_like(canal_verde), canal_azul])

# Mostrar la imagen original y los canales separados
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(imagen_rgb)
plt.title('Imagen Original')

plt.subplot(2, 2, 2)
plt.imshow(imagen_solo_rojo)
plt.title('Canal Rojo')

plt.subplot(2, 2, 3)
plt.imshow(imagen_solo_verde)
plt.title('Canal Verde')

plt.subplot(2, 2, 4)
plt.imshow(imagen_solo_azul)
plt.title('Canal Azul')

plt.show()
