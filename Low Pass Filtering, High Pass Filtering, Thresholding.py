# Memanggil Library yang dibutuhkam
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra dalam mode grayscale
image = cv2.imread('gambar/kucing-menangis.jpg', 0)

# Melakukan low pass filtering dengan Gaussian Blur
blur = cv2.GaussianBlur(image, (5, 5), 0)

# Melakukan high pass filtering dengan kernel khusus
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
high_pass = cv2.filter2D(image, -1, kernel)

# Melakukan image thresholding
ret, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Tampilkan citra dan histogramnya
images = [image, blur, high_pass, threshold]
titles = ['Original', 'Low Pass Filtering', 'High Pass Filtering', 'Thresholding']

# Loop digunakan untuk mengulangi gambar dan judulnya
# Loop ini berulang dari 0 hingga 3 (inklusif) karena range(4) menghasilkan urutan angka dari 0 hingga 3
for i in range(4):

    plt.subplot(2, 4, i+1) # Membuat subplot dalam kisi 2 baris dan 4 kolom
    plt.imshow(images[i], cmap='gray')  # Mengubah colormap menjadi gray untuk gambar grayscale
    plt.title(titles[i]) # Menampilkan Title
    plt.axis('off')

    plt.subplot(2, 4, i+5) # Membuat subplot di baris kedua kisi, dimulai dari posisi kelima
    plt.hist(images[i].ravel(), 256, [0, 256]) # Menghitung dan memplot histogram gambar,ravel() digunakan untuk meratakan gambar menjadi larik 1D
    plt.title(titles[i] + ' Histogram') # Menetapkan judul subplot histogram dengan menambahkan Histogram ke judul yang sesuai dari daftar titles

# Menampilkan hasil subplot dan histogram yg dibuat 
plt.show()
