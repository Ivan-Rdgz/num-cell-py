import cv2
import numpy as np
from scipy import signal

def convert2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def transf_intensidad(image):
    m = 150
    e = 7

    s = 1/(1+m/image)**e
    s = (s - s.min())/(s.max() - s.min())

    s = np.round(s*255).astype(np.uint8)

    return s

def pasa_bajas_fourier(image):
    rows, cols = image.shape
    crow, ccol = rows//2, cols//2

    mask = np.zeros((rows,cols), np.float32)
    cv2.circle(mask, (ccol, crow), 75, 1, -1)
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum_1 = 20*np.log(np.abs(fshift)+1)

    fbp = fshift * mask
    img_baja = np.fft.ifft2(np.fft.ifftshift(fbp))
    img_baja = np.abs(img_baja)
    img_baja = cv2.normalize(img_baja, None, 0, 255, cv2.NORM_MINMAX)
    img_baja = np.uint8(img_baja)

    return img_baja

def filtro_sobel(image):
    kernel_sx = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]], dtype=np.float32)

    kernel_sy = np.array([[ 1,  2,  1],
                      [ 0,  0,  0],
                      [-1, -2, -1]], dtype=np.float32)
    
    edges_sx = signal.convolve2d(image, kernel_sx, mode ='same')
    edges_sy = signal.convolve2d(image, kernel_sy, mode ='same')

    sobel = cv2.magnitude(edges_sx, edges_sy)

    return sobel

