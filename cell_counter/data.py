import os
import cv2

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, "data")

def _load_image(name):
    path = os.path.join(DATA_PATH, name)
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def sangre():
    return _load_image("img1_blood.jpg")

def protoplastos():
    return _load_image("img2_protoplasts.jpg")

def chlorella_1():
    return _load_image("img3_chlorella.jpg")

def chlorella_2():
    return _load_image("img4_chlorella.jpg")

def animal():
    return _load_image("img5_animal.png")

def onion_1():
    return _load_image("img6_onion.jpg")

def onion_2():
    return _load_image("img7_onion.jpg")

def onion_3():
    return _load_image("img8_onion.jpg")

def monocytes():
    return _load_image("img9_monocytes.jpg")

def mesothelium():
    return _load_image("img10_mesothelium.jpg")

def onion_4():
    return _load_image("img11_onion.jpg")

def onion_5():
    return _load_image("img12_onion.png")

def tissue():
    return _load_image("img13_tissue.png")

def stem():
    return _load_image("img14_stemCells.jpg")