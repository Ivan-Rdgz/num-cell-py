import cell_counter
import matplotlib.pyplot as plt

img = cell_counter.data.blood()
conteo, img = cell_counter.count_cells(img)

plt.figure(1)
plt.imshow(img)
plt.show()


