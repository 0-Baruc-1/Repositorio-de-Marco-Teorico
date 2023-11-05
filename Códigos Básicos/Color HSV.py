import cv2
import matplotlib.pyplot as plt

# Cargar la imagen original en modo color
imagen = cv2.imread(R"C:\Users\Kevin\Desktop\lena.png")

# Convertir la imagen de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2HSV)

# Mostrar la imagen en RGB y HSV
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.imshow(imagen_rgb)
plt.title('Imagen Original en RGB')

plt.subplot(1, 2, 2)
plt.imshow(imagen_hsv)
plt.title('Imagen en HSV')

plt.show()

