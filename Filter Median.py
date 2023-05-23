# Memanggil library yang dibutuhkan
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memuat gambar menggunakan library skimage
from skimage.io import imread
from skimage.color import rgb2gray

# Membaca gambar
img1 = cv2.imread('gambar/kucingpisang.jpeg')
img2 = cv2.imread('gambar/kucing-menangis.jpg')

# Menampilkan dimensi gambar
print('Shape img 1 : ', img1.shape)
print('Shape img 2 : ', img2.shape)

# Menampilkan kedua gambar menggunakan matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(img1, cmap='gray')
ax[0].set_title("img 1")
ax[1].imshow(img2, cmap='gray')
ax[1].set_title("img 2")

# Mengubah gambar ke grayscale
gray1 = rgb2gray(img1)
gray2 = rgb2gray(img2)

# Meng-copy gambar ke array baru dengan tipe data float
copyimg1 = gray1.copy().astype(float)
copyimg2 = gray2.copy().astype(float)

# Mendapatkan dimensi gambar yang dicopy
m1, n1 = copyimg1.shape
output1 = np.empty([m1, n1])

m2, n2 = copyimg2.shape
output2 = np.empty([m2, n2])

# Menampilkan informasi dimensi dan ukuran gambar
print('Shape copy img 1 : ', copyimg1.shape)
print('Shape output img 1 : ', output1.shape)
print('m1 : ', m1)
print('n1 : ', n1)
print()

print('Shape copy img 2 : ', copyimg2.shape)
print('Shape output img 3 : ', output2.shape)
print('m2 : ', m2)
print('n2 : ', n2)
print()

# Melakukan operasi filter rata-rata pada gambar pertama
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        dataA = [copyimg1[a1-1, b1-1], copyimg1[a1-1, b1], copyimg1[a1-1, b1+1], \
              copyimg1[a1, b1-1], copyimg1[a1, b1], copyimg1[a1, b1+1], \
              copyimg1[a1+1, b1-1], copyimg1[a1+1, b1], copyimg1[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j]= tmpA
        
        output1[a1, b1] = dataA[5]

# Melakukan operasi filter rata-rata pada gambar kedua
for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris
        b1 = kolom
        dataA = [copyimg2[a1-1, b1-1], copyimg2[a1-1, b1], copyimg2[a1-1, b1+1], \
              copyimg2[a1, b1-1], copyimg2[a1, b1], copyimg2[a1, b1+1], \
              copyimg2[a1+1, b1-1], copyimg2[a1+1, b1], copyimg2[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j]= tmpA
        
        output2[a1, b1] = dataA[5]

# Menampilkan gambar asli dan hasil filter rata-rata
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(gray1, cmap='gray')
ax[0].set_title("Input img 1")
ax[1].imshow(gray2, cmap='gray')
ax[1].set_title("Input img 2")
ax[2].imshow(output1, cmap='gray')
ax[2].set_title("Output img 1")
ax[3].imshow(output2, cmap='gray')
ax[3].set_title("Output img 2")

plt.show()
