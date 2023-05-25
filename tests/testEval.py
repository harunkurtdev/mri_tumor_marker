import cv2
import numpy as np
import matplotlib.pyplot as plt

# Orijinal resmin dosya yolu
image_path = "./images/ui/main_screen.png"

# Resmi oku ve gri tonlamaya çevir
image = cv2.imread(image_path, 0)

# Histogram eşitleme uygula
equalized_image = cv2.equalizeHist(image)

# Orijinal resmin histogramını hesapla
hist_original, bins_original = np.histogram(image.flatten(), 256, [0, 256])

# Eşitleme sonrası resmin histogramını hesapla
hist_equalized, bins_equalized = np.histogram(equalized_image.flatten(), 256, [0, 256])

# Histogram grafiği
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(hist_original, color='b')
plt.title("Orijinal Resim")
plt.xlabel("Yoğunluk Değeri")
plt.ylabel("Piksel Sayısı")

plt.subplot(2, 1, 2)
plt.plot(hist_equalized, color='r')
plt.title("Eşitleme Sonrası Resim")
plt.xlabel("Yoğunluk Değeri")
plt.ylabel("Piksel Sayısı")

plt.tight_layout()
plt.show()
