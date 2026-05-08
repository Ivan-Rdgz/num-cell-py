import cv2
import numpy as np
from scipy import signal

def umbralizar(img):
        # UMBRALIZACIÓN MANUAL (Lógica de comparación manual)
    # En lugar de np.where, usamos una máscara simple que es más fácil de explicar
    umbral_propio = np.mean(img) - 10
    binaria = np.zeros(img.shape, dtype=np.uint8)
    # Si el pixel es más oscuro que el umbral, ponlo blanco (255)
    binaria[img < umbral_propio] = 255
    return binaria

def segmentar(img):
    # Usamos un kernel un poco más grande para cerrar huecos dentro de los núcleos
    filtro_limpieza = np.ones((5, 5), dtype=np.float32) / 25
    
    # Aplicamos una vez para suavizar
    limpia = signal.convolve2d(img, filtro_limpieza, mode='same')
    
    # Umbralizamos para recuperar la binaria
    binaria_final = np.zeros(limpia.shape, dtype=np.uint8)
    binaria_final[limpia > 150] = 255 # Subimos un poco el umbral de limpieza
    return binaria_final

def componentes_conectados(img, img_gray):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img, 8)
    resultado_vis = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    conteo_final = 0
    
    alto_max, ancho_max = img.shape[:2]

    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]
        
        # --- FILTRO INTELIGENTE ---
        # 1. El área debe ser razonable (ni muy pequeña ni gigante)
        # 2. El ancho y alto no pueden ser más de la mitad de la imagen (adiós líneas largas)
        if 200 < area < (alto_max * ancho_max * 0.1): 
            if w < (ancho_max * 0.5) and h < (alto_max * 0.5):
                conteo_final += 1
                cv2.rectangle(resultado_vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(resultado_vis, str(conteo_final), (x, y-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                            
    return resultado_vis, conteo_final