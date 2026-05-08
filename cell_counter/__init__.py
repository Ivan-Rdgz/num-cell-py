from . import data
from . import preprocesar
from . import segmentacion
import cv2
from .data import sangre, protoplastos, chlorella_1, chlorella_2, animal, onion_1, onion_2, onion_3, monocytes, mesothelium, onion_4, onion_5, tissue, stem
from .preprocesar import filtro_pasa_bajas, intensidad_gamma, filter_sobel
from .segmentacion import umbralizar, segmentar, componentes_conectados

def count_cells(img_rgb, gamma=1.2, radio=30):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img1 = filtro_pasa_bajas(img_gray, radio=radio)
    img2 = intensidad_gamma(img1, gamma = gamma)
    img3 = umbralizar(img2)
    img4 = segmentar(img3)
    img_final, conteo_final = componentes_conectados(img4, img_gray)
    return conteo_final, img_final