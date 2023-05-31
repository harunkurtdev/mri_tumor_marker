import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Örnek veri boyutları
width = 100
height = 100
# depth = 50
depth = 22
num_images = 22

# Resimleri oku ve normalize et
normalized_volumes = []
for i in range(num_images):
    # Resmi oku
    i+=1
    image_path = f"./mri_shoulders/Seri1/{i}.jpg"  # Resmin dosya yolu
    # print(i)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # image = cv2.imread("./mri_shoulders/Seri1/"+str(i)+".jpg", cv2.IMREAD_UNCHANGED)
    # print(image)
    # Resmi yeniden boyutlandır
    image_resized = cv2.resize(image, (width, height))

    # Resmi normalize et
    normalized_volume = (image_resized - np.min(image_resized)) / (np.max(image_resized) - np.min(image_resized))
    # normalized_volume[normalized_volume < 0.01] = 0  # 0'a yakın değerleri 0 olarak ayarla
    normalized_volumes.append(normalized_volume)
normalized_volumes.reverse()
# Verileri 3B olarak yeniden şekillendir
x, y, z = np.meshgrid(np.arange(width),
                      np.arange(height),
                      np.arange(depth))

# Tüm verileri görselleştir
# Verileri 3B olarak yeniden şekillendir
x, y, z = np.meshgrid(np.arange(width),
                      np.arange(height),
                      np.arange(depth))

# 3B görselleştirme figürünü oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tüm verileri görselleştir
for normalized_volume in normalized_volumes:
    # Veriyi yeniden şekillendir
    normalized_volume_3d = np.repeat(normalized_volume[:, :, np.newaxis], depth, axis=2)
     # Siyah olan kısımları transparan yap
    normalized_volume_3d[normalized_volume_3d <0.095] = np.nan
    
    ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=normalized_volume_3d.flatten(), cmap='gray', s=0.1,alpha=0.5)
    # ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=normalized_volume_3d.reshape(-1, 4), cmap='gray', s=0.1)

# Eksenleri ayarla
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_zlim(0, depth)

# Görüntüle
plt.show()

