import cv2
import numpy as np
from scipy import signal

def filtro_pasa_bajas(img, radio=30):
    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    f = np.fft.fft2(np.float32(img))
    fshift = np.fft.fftshift(f)
    mask = np.zeros((rows, cols), np.float32)
    cv2.circle(mask, (ccol, crow), radio, 1, -1)
    f_filtrada = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(f_filtrada))
    img_suave = np.abs(img_back)
    img_suave = cv2.normalize(img_suave, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    return img_suave

def intensidad_gamma(img, gamma =1.2):
    img_gamma = (np.power(img / 255.0, gamma) * 255).astype(np.uint8)
    return img_gamma

def filter_sobel(img):

    kernel_sx = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], dtype=np.float32)

    kernel_sy = np.array([[ 1,  2,  1],
                        [ 0,  0,  0],
                        [-1, -2, -1]], dtype=np.float32)

    edges_sx = signal.convolve2d(img, kernel_sx, mode ='same')
    edges_sy = signal.convolve2d(img, kernel_sy, mode ='same')

    bordes_sobel = np.sqrt(edges_sx**2 + edges_sy**2)
    bordes_sobel = cv2.normalize(bordes_sobel, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
    return bordes_sobel
