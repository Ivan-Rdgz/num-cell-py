import cv2
import numpy as np
from scipy import signal

def convert2gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def transf_intensity(image, e = 5 ):
    m = np.mean(image)

    s = 1/(1+m/image)**e
    s = (s - s.min())/(s.max() - s.min())

    s = np.round(s*255).astype(np.uint8)

    return s

def fourier_lowPass(image, radius_mask = 80):
    rows, cols = image.shape
    crow, ccol = rows//2, cols//2

    mask = np.zeros((rows,cols), np.float32)
    cv2.circle(mask, (ccol, crow), radius_mask, 1, -1)
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum_1 = 20*np.log(np.abs(fshift)+1)

    fbp = fshift * mask
    img_baja = np.fft.ifft2(np.fft.ifftshift(fbp))
    img_baja = np.abs(img_baja)
    img_baja = cv2.normalize(img_baja, None, 0, 255, cv2.NORM_MINMAX)
    img_baja = np.uint8(img_baja)

    return img_baja

def filter_sobel(image, threshold_L = 50, threshold_H = 150):
    edges_canny = cv2.Canny(image, threshold_L,threshold_H) 
    return edges_canny

