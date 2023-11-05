from PIL import Image

# Función para calcular la densidad de píxeles
def calcular_densidad_pixeles(ruta_imagen, ancho_fisico, alto_fisico):
    # Cargar la imagen
    with Image.open(ruta_imagen) as img:
        # Obtener dimensiones en píxeles
        ancho_px, alto_px = img.size
    
    # Calcular la densidad de píxeles
    ppi_x = ancho_px / ancho_fisico
    ppi_y = alto_px / alto_fisico
    
    return ppi_x, ppi_y

# Ruta a la imagen
ruta_imagen = R"C:\Users\Kevin\Desktop\lena1.png"

# Dimensiones físicas de la imagen (en pulgadas)
ancho_fisico = 6  # ancho en pulgadas
alto_fisico = 6   # alto en pulgadas

# Calcular densidad de píxeles
densidad_x, densidad_y = calcular_densidad_pixeles(ruta_imagen, ancho_fisico, alto_fisico)

print(f"Densidad de píxeles horizontal: {densidad_x} PPI")
print(f"Densidad de píxeles vertical: {densidad_y} PPI")

