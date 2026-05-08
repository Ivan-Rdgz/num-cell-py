import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from cell_counter.preprocesar import filtro_pasa_bajas, intensidad_gamma, filter_sobel
from cell_counter.segmentacion import umbralizar, segmentar, componentes_conectados
from cell_counter import data

img = data.onion_5()
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img1 = filtro_pasa_bajas(img_gray, radio=30)
img2 = intensidad_gamma(img1, gamma = 1.2)
img3 = umbralizar(img2)
img4 = segmentar(img3)
img_final, conteo_final = componentes_conectados(img4, img_gray)

plt.close('all')
plt.figure()
plt.imshow(img_final), plt.title(f'Conteo: {conteo_final}')
plt.show()

