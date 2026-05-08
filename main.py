import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from cell_counter.preprocesar import convert2gray, transf_intensity, fourier_lowPass, filter_sobel
from cell_counter.segmentacion import segment_otsu
from cell_counter.analisis import count_cells_by_regions

img = cv2.imread("data/cells_4.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_gray = convert2gray(img)
img_trans = transf_intensity(img_gray,5)
img_f = fourier_lowPass(img_trans,80)
img_sobel = filter_sobel(img_f)
img_seg = segment_otsu(img_sobel)

x, y ,z = count_cells_by_regions(img_seg)
print("cells: ", x)

plt.figure(1)
plt.subplot(2,2,1), plt.imshow(img_trans, cmap='gray'), plt.title('Transformación')
plt.subplot(2,2,2), plt.imshow(img_f, cmap='gray'), plt.title('fourier')
plt.subplot(2,2,3), plt.imshow(img_sobel, cmap='gray'), plt.title('segmentar')
plt.subplot(2,2,4), plt.imshow(img_sobel, cmap='gray'), plt.title('sobel')
plt.figure(2)
plt.imshow(y, cmap='gray')
plt.show()