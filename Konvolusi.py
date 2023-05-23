# Memanggil library yang dibutuhkan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memuat gambar menggunakan library skimage
from skimage.io import imread
from skimage.color import rgb2gray

# Membaca gambar dan membuat grayscale gambar menggunakan OpenCV
img = cv2.imread('gambar/sadcat.jpeg', 0)

# Menampilkan dimensi gambar
print(img.shape)

plt.imshow(img, cmap='gray')

# Membuat kernel untuk operasi filter
kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

# Melakukan operasi filter 2D pada gambar menggunakan kernel
citraOutput = cv2.filter2D(img, -1, kernel)

# Menampilkan citra input dan citra output
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(img, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].imshow(citraOutput, cmap='gray')
ax[1].set_title("Citra Output")

# Menampilkan gambar
plt.show()
