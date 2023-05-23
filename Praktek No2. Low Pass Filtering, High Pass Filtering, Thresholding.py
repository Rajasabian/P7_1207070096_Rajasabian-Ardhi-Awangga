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

for i in range(4):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')  # Mengubah colormap menjadi gray untuk gambar grayscale
    plt.title(titles[i])
    plt.axis('off')

    plt.subplot(2, 4, i+5)
    plt.hist(images[i].ravel(), 256, [0, 256])
    plt.title(titles[i] + ' Histogram')

plt.show()
