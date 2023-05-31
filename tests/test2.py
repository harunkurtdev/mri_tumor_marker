import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Örnek veri boyutları
width = 100
height = 100
depth = 22
num_images = 22

# Resimleri oku ve normalize et
normalized_volumes = []
for i in range(num_images):
    # image_path = "./mri_scans/{}.jpg".format(i+1)  # Resmin dosya yolu (i+1 ile indeks 1'den başlar)
    image_path = "./mri_shoulders/Seri1/{}.jpg".format(i+1)  # Resmin dosya yolu (i+1 ile indeks 1'den başlar)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resmi yeniden boyutlandır
    image_resized = cv2.resize(image, (width, height))
    
    # Resmi normalize et
    normalized_volume = (image_resized - np.min(image_resized)) / (np.max(image_resized) - np.min(image_resized))
    normalized_volumes.append(normalized_volume)
    del(image)
    del(image_resized)
    del(normalized_volume)

# 3B görselleştirme figürünü oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tüm verileri görselleştir
for i, normalized_volume in enumerate(normalized_volumes):
    # Veriyi yeniden şekillendir
    x, y, z = np.meshgrid(np.arange(width),
                          np.arange(height),
                          np.arange(depth))
    normalized_volume_3d = np.repeat(normalized_volume[:, :, np.newaxis], depth, axis=2)
    normalized_volume_3d[normalized_volume_3d < 0.2] = np.nan
    
    # Her bir görüntüyü ayrı ayrı çiz
    # ax.scatter(x.flatten(), y.flatten(), z.flatten()+i, c=normalized_volume_3d.flatten()*np.ones_like(x.flatten()), cmap='gray', s=0.1)
    ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=normalized_volume_3d.flatten()*np.ones_like(x.flatten()), cmap='gray', s=0.1,alpha=0.5)

# Eksenleri ayarla
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_zlim(0, num_images*5)

# Görüntüle
plt.show()
