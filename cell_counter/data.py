import os
import cv2

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, 'data')

def _load_image(name):
    path = os.path.normpath(os.path.join(DATA_PATH, name))
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró la imagen en: {path}")
    
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Error al leer la imagen (posible formato corrupto): {path}")
            
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def blood():
    return _load_image("img1_blood.jpg")

def chlorella():
    return _load_image("img2_chlorella.jpg")

def animal():
    return _load_image("img3_animal.png")

def onion_1():
    return _load_image("img4_onion.jpg")

def onion_2():
    return _load_image("img5_onion.jpg")

def monocytes():
    return _load_image("img6_monocytes.jpg")

def onion_3():
    return _load_image("img7_onion.jpg")

def onion_4():
    return _load_image("img8_onion.png")

def stem():
    return _load_image("img9_stemCells.jpg")

def tissue():
    return _load_image("img10_tissue.jpg")

def onion_5():
    return _load_image("img11_onion.jpeg")

def dna():
    return _load_image("img12_dna.jpg")

def onion_6():
    return _load_image("img13_onion.jpg")

def human():
    return _load_image("img14_human.jpg")

def onion_7():
    return _load_image("img15_onion.jpg")
