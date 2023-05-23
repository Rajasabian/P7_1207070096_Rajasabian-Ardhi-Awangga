# Memanggil Library yang dibutuhkan
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Memanggil citra dalam mode grayscale (argument 0)
img = cv2.imread('gambar/kucingpisang.jpeg', 0)

#Menampilkan citra asli
cv2.imshow('Original', img)
cv2.waitKey(0)

# Memanggil fungsi Canny Edges dengan argumen (citra, nilai_min, nilai_max)
edges = cv2.Canny(img, 100, 200)

# Menerapkan algoritma high-pass filtering: Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# Perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (20, 20)

# Menampilkan hasil filter
plt.subplot(2, 2, 1), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])  # Hasil filter Laplacian
plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])  # Hasil filter Sobel X
plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])  # Hasil filter Sobel Y
plt.subplot(2, 2, 4), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([]) #Hasil filter Edge

plt.show()
