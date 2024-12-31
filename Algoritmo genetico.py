import random
import numpy as np
import cv2
import os
from deap import base, creator, tools, algorithms
from functools import partial

# Directorios para imágenes y máscaras de referencia
image_folder = r"C:\Users\Kevin\Desktop\Data\Otra Data\Granulatorio"
mask_folder = r"C:\Users\Kevin\Desktop\Data\Otra Data\Etiquetas Granulatorio"

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

# Cargar imágenes y máscaras de referencia
images = load_images_from_folder(image_folder)
masks = load_images_from_folder(mask_folder)

def threshold_segmentation(image, lower_bound1, upper_bound1, lower_bound2, upper_bound2):
    """Realiza la segmentación basada en dos rangos HSV."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Crear máscaras para ambos rangos
    mask1 = cv2.inRange(hsv, np.array(lower_bound1, dtype=np.uint8), np.array(upper_bound1, dtype=np.uint8))
    mask2 = cv2.inRange(hsv, np.array(lower_bound2, dtype=np.uint8), np.array(upper_bound2, dtype=np.uint8))
    
    # Combinar las máscaras
    combined_mask = cv2.bitwise_or(mask1, mask2)
    return combined_mask

def calculate_jaccard_index(segmented_image, reference_mask):
    """Calcula el índice de Jaccard entre la imagen segmentada y la máscara de referencia."""
    # Convertir la máscara de referencia a escala de grises si tiene tres canales
    if len(reference_mask.shape) == 3:
        reference_mask = cv2.cvtColor(reference_mask, cv2.COLOR_BGR2GRAY)
    
    # Binarizar ambas imágenes
    segmented_image = (segmented_image > 0).astype(np.uint8)
    reference_mask = (reference_mask > 0).astype(np.uint8)

    # Calcular la intersección y la unión
    intersection = np.logical_and(segmented_image, reference_mask)
    union = np.logical_or(segmented_image, reference_mask)

    # Calcular el índice de Jaccard (intersección sobre unión)
    jaccard_index = np.sum(intersection) / np.sum(union)
    
    return jaccard_index


def evaluate_individual(individual, images, masks):
    """Evalúa un individuo calculando el índice de Jaccard promedio para todas las imágenes."""
    # Extraer los dos rangos HSV
    lower_bound1 = [individual[0], individual[1], individual[2]]
    upper_bound1 = [individual[3], individual[4], individual[5]]
    lower_bound2 = [individual[6], individual[7], individual[8]]
    upper_bound2 = [individual[9], individual[10], individual[11]]
    
    total_jaccard = 0

    for image, mask in zip(images, masks):
        segmented_image = threshold_segmentation(image, lower_bound1, upper_bound1, lower_bound2, upper_bound2)
        jaccard_index = calculate_jaccard_index(segmented_image, mask)
        total_jaccard += jaccard_index

    return total_jaccard / len(images),


# Configuración del algoritmo genético
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Inicialización con rangos más acotados
def init_hsv_rango1():
    return random.randint(0, 15)  # Rango inicial para H (0-15)
def init_s_rango1():
    return random.randint(40, 255)  # Rango inicial para S (40-255)
def init_v_rango1():
    return random.randint(40, 255)  # Rango inicial para V (40-255)
def init_hsv_rango2():
    return random.randint(165, 180)  # Rango inicial para H (165-180)
def init_s_rango2():
    return random.randint(40, 255)  # Rango inicial para S (40-255)
def init_v_rango2():
    return random.randint(40, 255)  # Rango inicial para V (40-255)

# Registrar atributos con inicialización acotada
toolbox.register("attr_hsv_rango1", init_hsv_rango1)
toolbox.register("attr_s_rango1", init_s_rango1)
toolbox.register("attr_v_rango1", init_v_rango1)
toolbox.register("attr_hsv_rango2", init_hsv_rango2)
toolbox.register("attr_s_rango2", init_s_rango2)
toolbox.register("attr_v_rango2", init_v_rango2)

# Generar individuos
toolbox.register("individual", tools.initCycle, creator.Individual, 
                 (toolbox.attr_hsv_rango1, toolbox.attr_s_rango1, toolbox.attr_v_rango1, 
                  toolbox.attr_hsv_rango1, toolbox.attr_s_rango1, toolbox.attr_v_rango1,
                  toolbox.attr_hsv_rango2, toolbox.attr_s_rango2, toolbox.attr_v_rango2,
                  toolbox.attr_hsv_rango2, toolbox.attr_s_rango2, toolbox.attr_v_rango2), n=1)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", partial(evaluate_individual, images=images, masks=masks))
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=255, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    """Ejecuta el algoritmo genético para optimizar dos rangos HSV."""
    population = toolbox.population(n=50)  # Tamaño de la población
    hof = tools.HallOfFame(1, similar=np.array_equal)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, 
                        stats=stats, halloffame=hof, verbose=True)

    best_individual = hof[0]
    print("Mejor individuo (dos rangos HSV):", best_individual)

    # Evaluar con el mejor individuo
    lower_bound1 = best_individual[:3]
    upper_bound1 = best_individual[3:6]
    lower_bound2 = best_individual[6:9]
    upper_bound2 = best_individual[9:]
    
    for i, (image, mask) in enumerate(zip(images, masks)):
        segmented_image = threshold_segmentation(image, lower_bound1, upper_bound1, lower_bound2, upper_bound2)
        cv2.imwrite(f"resultado_segmentado_{i}.png", segmented_image)

    return best_individual

if __name__ == "__main__":
    best_hsv = main()
    print("Rangos HSV óptimos:")
    print(f"Rango 1: {best_hsv[:3]} - {best_hsv[3:6]}")
    print(f"Rango 2: {best_hsv[6:9]} - {best_hsv[9:]}")
