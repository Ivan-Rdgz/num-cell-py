import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from cell_counter.preprocesar import convert2gray, transf_intensity, fourier_lowPass, filter_sobel

img = cv2.imread("monedas.jpg")



