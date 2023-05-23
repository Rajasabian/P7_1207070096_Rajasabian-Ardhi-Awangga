# Memanggil Library yang dibutuhkam
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra dalam mode BGR
img = cv2.imread('gambar/sadcat.jpeg')

# Mengonversi citra dari BGR ke RGB
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5, 5), np.float32) / 25
print(kernel)

# Melakukan filtering menggunakan cv2.filter2D()
kucing_filter2D = cv2.filter2D(img, -1, kernel)

# Menampilkan hasil filtering menggunakan cv2.imshow()
cv2.imshow('kucing_filter2D', kucing_filter2D)
cv2.imshow('sadcat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Membuat Blur menggunakan cv2.blur()
kucing_blur = cv2.blur(img, (5, 5))

# Menampilkan hasil Blur menggunakan cv2.imshow()
cv2.imshow('kucing_blur', kucing_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15, 15)

# Plot pertama: gambar asli
plt.subplot(121), plt.imshow(cat), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Plot kedua: hasil filter
plt.subplot(122), plt.imshow(kucing_filter2D), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Tampilkan plot
plt.show()

# Membuat kernel dengan menggunakan np.array() bukan np.matrix()
kernel = np.array([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]         
          ])/25
print(kernel)

# Melakukan filtering menggunakan cv2.filter2D()
kucing_filter = cv2.filter2D(img, -1, kernel)

# Menampilkan hasil filtering menggunakan cv2.imshow()
cv2.imshow('kucing_filter', kucing_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()

