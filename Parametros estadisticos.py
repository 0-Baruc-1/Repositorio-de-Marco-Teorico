import cv2
import numpy as np
import os
from skimage.io import imread
import matplotlib.pyplot as plt


# Definimos los valores mínimos y máximos teóricos para HSV
valores_minimos_posibles_hsv = [0, 0, 0]   # H, S, V
valores_maximos_posibles_hsv = [179, 255, 255]  # H, S, V

def obtener_coordenadas_herida(mascara_referencia):
    contornos, _ = cv2.findContours(mascara_referencia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contornos:
        raise ValueError("No se encontraron contornos en la máscara de referencia.")
    
    contorno_mas_grande = max(contornos, key=cv2.contourArea)
    x, y, ancho, alto = cv2.boundingRect(contorno_mas_grande)
    
    return x, y, ancho, alto

def graficar_media_desviacion(medias, desviaciones, nombre_imagen, dir_salida):
    componentes = ['Hue', 'Saturation', 'Value']
    x = np.arange(len(componentes))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - 0.2, medias, 0.4, label='Media', color='blue')
    ax.bar(x + 0.2, desviaciones, 0.4, label='Desviación Estándar', color='orange')
    
    ax.set_xlabel('Componentes HSV')
    ax.set_ylabel('Valor')
    ax.set_title(f'Media y Desviación Estándar - {nombre_imagen}')
    ax.set_xticks(x)
    ax.set_xticklabels(componentes)
    ax.legend()
    
    plt.savefig(os.path.join(dir_salida, f"media_desviacion_{nombre_imagen}.png"))
    plt.show()

# Función para graficar un boxplot con los datos de HSV
def graficar_boxplot(herida_recortada, herida_mascara, nombre_imagen, dir_salida):
    herida_hsv = cv2.cvtColor(herida_recortada, cv2.COLOR_RGB2HSV)
    
    # Filtrar los píxeles válidos usando la máscara
    mascara_valida = herida_mascara > 0
    herida_hsv_valida = herida_hsv[mascara_valida]

    if herida_hsv_valida.size == 0:
        print(f"No hay píxeles válidos para graficar el boxplot en {nombre_imagen}.")
        return

    # Definir propiedades para resaltar la media
    meanprops = dict(marker='o', markerfacecolor='red', markeredgecolor='black', markersize=8)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot([herida_hsv_valida[:, 0], 
                herida_hsv_valida[:, 1], 
                herida_hsv_valida[:, 2]],
               labels=['Hue', 'Saturation', 'Value'],
               showmeans=True,  
               meanprops=meanprops)  
    
    ax.set_title(f'Distribución de HSV - {nombre_imagen}')
    ax.set_ylabel('Valor')

    plt.savefig(os.path.join(dir_salida, f"boxplot_{nombre_imagen}.png"))
    plt.show()

def generar_graficas_comparativas(vectores_min_max, dir_salida):
    # Colores para cada tipo de tejido
    colores = {
        'granulatorio': 'red',
        'esfacelo': 'yellow',
        'necrotico': 'black'
    }

    # Listas de valores para cada canal y su respectivo mínimo y máximo
    parametros = ['h_min', 'h_max', 's_min', 's_max', 'v_min', 'v_max']
    nombres_graficas = {
        'h_min': 'Comparación de H_min por Tejido',
        'h_max': 'Comparación de H_max por Tejido',
        's_min': 'Comparación de S_min por Tejido',
        's_max': 'Comparación de S_max por Tejido',
        'v_min': 'Comparación de V_min por Tejido',
        'v_max': 'Comparación de V_max por Tejido'
    }

    # Crear una gráfica para cada parámetro
    for parametro in parametros:
        plt.figure(figsize=(10, 6))
        for tejido, color in colores.items():
            if parametro in vectores_min_max[tejido]:
                plt.plot(vectores_min_max[tejido][parametro], label=tejido.capitalize(), color=color)

        plt.xlabel('Índice de Imagen')
        plt.ylabel('Valor HSV')
        plt.title(nombres_graficas[parametro])
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(dir_salida, f"{parametro}_comparativa.png"))
        plt.show()

def calcular_z_scores(herida_hsv_valida, medias, desviaciones):
    # Calcular Z-Scores para cada canal HSV
    z_scores_hue = (herida_hsv_valida[:, 0] - medias[0]) / desviaciones[0]
    z_scores_saturation = (herida_hsv_valida[:, 1] - medias[1]) / desviaciones[1]
    z_scores_value = (herida_hsv_valida[:, 2] - medias[2]) / desviaciones[2]
    
    return z_scores_hue, z_scores_saturation, z_scores_value

def calcular_media_desviacion(herida_recortada, herida_mascara):
    herida_hsv = cv2.cvtColor(herida_recortada, cv2.COLOR_RGB2HSV)
    
    mascara_valida = herida_mascara > 0
    herida_hsv_valida = herida_hsv[mascara_valida]

    herida_hsv_valida = np.where(herida_hsv_valida == 0, np.nan, herida_hsv_valida)

    medias = np.nanmean(herida_hsv_valida, axis=0)
    desviaciones = np.nanstd(herida_hsv_valida, axis=0)

    rangos_min = medias - desviaciones
    rangos_max = medias + desviaciones

    condicion = (
        (herida_hsv_valida >= rangos_min) &
        (herida_hsv_valida <= rangos_max) &
        (herida_hsv_valida >= [0, 0, 0]) &
        (herida_hsv_valida <= [179, 255, 255])
    )
    condicion = np.all(condicion, axis=1)
    pixels_within_ranges = herida_hsv_valida[condicion]

    if pixels_within_ranges.size == 0:
        print("No hay píxeles válidos que cumplan con las condiciones para esta imagen.")
        min_hsv = [np.nan, np.nan, np.nan]
        max_hsv = [np.nan, np.nan, np.nan]
    else:
        min_hsv = np.nanmin(pixels_within_ranges, axis=0)
        max_hsv = np.nanmax(pixels_within_ranges, axis=0)

    return medias, desviaciones, rangos_min, rangos_max, min_hsv, max_hsv

def procesar_imagenes_por_tejido(dir_entrada, dir_referencia, dir_salida):
    if not os.path.exists(dir_salida):
        os.makedirs(dir_salida)

    vectores_min_max = {
        'granulatorio': {'h_min': [], 'h_max': [], 's_min': [], 's_max': [], 'v_min': [], 'v_max': []},
        'esfacelo': {'h_min': [], 'h_max': [], 's_min': [], 's_max': [], 'v_min': [], 'v_max': []},
        'necrotico': {'h_min': [], 'h_max': [], 's_min': [], 's_max': [], 'v_min': [], 'v_max': []}
    }

    for filename in os.listdir(dir_entrada):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            base_name, ext = os.path.splitext(filename)  
            parts = base_name.split('_')
            if len(parts) < 2:
                print(f"Formato de nombre incorrecto en el archivo {filename}, ignorando.")
                continue
            
            tissue_type = parts[-1].lower()  
            if tissue_type not in vectores_min_max:
                print(f"Tejido desconocido en el archivo {filename}, ignorando.")
                continue

            ruta_imagen = os.path.join(dir_entrada, filename)
            ruta_referencia = os.path.join(dir_referencia, filename)

            if not os.path.exists(ruta_referencia):
                print(f"Etiqueta no encontrada para la imagen {filename}.")
                continue

            imagen = imread(ruta_imagen)
            mascara_referencia = imread(ruta_referencia, as_gray=True)
            mascara_referencia = (mascara_referencia > 0).astype(np.uint8) * 255

            try:
                x, y, ancho, alto = obtener_coordenadas_herida(mascara_referencia)
            except ValueError as e:
                print(f"Error en {filename}: {e}")
                continue

            herida = imagen[y:y+alto, x:x+ancho]
            herida_mascara = mascara_referencia[y:y+alto, x:x+ancho]
            herida_recortada = cv2.bitwise_and(herida, herida, mask=herida_mascara)

            plt.imshow(herida_recortada)
            plt.title(f"Región de la Herida - {filename}")
            plt.savefig(os.path.join(dir_salida, f"region_herida_{filename}.png"))
            plt.show()

            medias, desviaciones, rangos_min, rangos_max, min_hsv, max_hsv = calcular_media_desviacion(
                herida_recortada, herida_mascara)

            graficar_media_desviacion(medias, desviaciones, filename, dir_salida)
            graficar_boxplot(herida_recortada, herida_mascara, filename, dir_salida)

            if not np.isnan(min_hsv).any() and not np.isnan(max_hsv).any():
                vectores_min_max[tissue_type]['h_min'].append(min_hsv[0])
                vectores_min_max[tissue_type]['h_max'].append(max_hsv[0])
                vectores_min_max[tissue_type]['s_min'].append(min_hsv[1])
                vectores_min_max[tissue_type]['s_max'].append(max_hsv[1])
                vectores_min_max[tissue_type]['v_min'].append(min_hsv[2])
                vectores_min_max[tissue_type]['v_max'].append(max_hsv[2])

            with open(os.path.join(dir_salida, f"resultados_{filename}.txt"), 'w') as f:
                f.write(f"Imagen: {filename}\n")
                f.write(f"Tejido: {tissue_type.capitalize()}\n")
                f.write(f"Medias (H, S, V): {medias}\n")
                f.write(f"Desviaciones (H, S, V): {desviaciones}\n")
                f.write(f"Rangos Mínimos (H, S, V): {rangos_min}\n")
                f.write(f"Rangos Máximos (H, S, V): {rangos_max}\n")
                f.write(f"Valores Mínimos (H, S, V): {min_hsv}\n")
                f.write(f"Valores Máximos (H, S, V): {max_hsv}\n")

    with open(os.path.join(dir_salida, "vectores_min_max_por_tejido.txt"), 'w') as f:
        for tissue, data in vectores_min_max.items():
            f.write(f"Tejido: {tissue}\n")
            f.write(f"H_min: {data['h_min']}\n")
            f.write(f"H_max: {data['h_max']}\n")
            f.write(f"S_min: {data['s_min']}\n")
            f.write(f"S_max: {data['s_max']}\n")
            f.write(f"V_min: {data['v_min']}\n")
            f.write(f"V_max: {data['v_max']}\n\n")

    print("Procesamiento completado. Resultados guardados en 'vectores_min_max_por_tejido.txt'.")

    generar_graficas_comparativas(vectores_min_max, dir_salida)


if __name__ == "__main__":
    dir_entrada = r"C:\Users\Kevin\Desktop\Data\Desviación y media HSV\Heridas"
    dir_referencia = r"C:\Users\Kevin\Desktop\Data\Desviación y media HSV\Etiquetas"
    dir_salida = r"C:\Users\Kevin\Desktop\Data\Desviación y media HSV\Nuevos Resultados"

    procesar_imagenes_por_tejido(dir_entrada, dir_referencia, dir_salida)
