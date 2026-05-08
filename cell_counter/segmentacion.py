import cv2
import numpy as np
from scipy import signal

from cell_counter.preprocesar import intensidad_gamma

def umbralizar(img):
        # UMBRALIZACIÓN MANUAL (Lógica de comparación manual)
    # En lugar de np.where, usamos una máscara simple que es más fácil de explicar
    umbral_propio = np.mean(img) - 10
    binaria = np.zeros(img.shape, dtype=np.uint8)
    # Si el pixel es más oscuro que el umbral, ponlo blanco (255)
    binaria[img < umbral_propio] = 255
    return binaria

def segmentar(img):
    filtro_limpieza = np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]], dtype=np.float32) / 9

    # Pasamos el filtro 2 veces para limpiar el ruido
    limpia = signal.convolve2d(img, filtro_limpieza, mode='same')
    limpia = signal.convolve2d(limpia, filtro_limpieza, mode='same')

    binaria_final = np.zeros(limpia.shape, dtype=np.uint8)
    binaria_final[limpia > 127] = 255
    return binaria_final

def componentes_conectados(img, img_gray):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, 8)
    resultado_vis = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    conteo_final = 0
    
    for i in range(1, num_labels): 
        x, y, w, h, area = stats[i]
        
        # Filtro de área básico que tenías originalmente
        if area > 150:
            conteo_final += 1
            cv2.rectangle(resultado_vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(resultado_vis, str(conteo_final), (x, y-5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                        
    return resultado_vis, conteo_final
