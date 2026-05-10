import cv2
from . import data
from . import preprocesar
from . import segmentacion
from .preprocesar import filtro_pasa_bajas, intensidad_gamma, filter_sobel
from .segmentacion import umbralizar, limpieza, componentes_conectados

def count_cells(img_rgb, gamma=1.2, radio=30):
    """Funcion principal: Conteo de células, se necesita una imagen RGB"""
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img1 = filtro_pasa_bajas(img_gray, radio=radio)
    img2 = intensidad_gamma(img1, gamma=gamma)
    img3 = umbralizar(img2)
    img4 = limpieza(img3)
    img_final, conteo_final = componentes_conectados(img4, img_gray)
    return conteo_final, img_final