import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import nibabel as nib

# MR verisini yükle
# data = nib.load('path_to_mri_file.nii.gz')
# volume = data.get_fdata()

import numpy as np

# Örnek veri boyutları
width = 100
height = 100
depth = 50

# Örnek beyin MR verisi oluştur
volume = np.random.rand(width, height, depth)

# Veriyi normalize et
normalized_volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))


# Veriyi normalize et
# normalized_volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))

# # Bir kesit seç
# slice_index = 49
# slice_data = normalized_volume[:, :, slice_index]

# # Veriyi 3B olarak yeniden şekillendir
# x, y, z = np.meshgrid(np.arange(slice_data.shape[0]),
#                       np.arange(slice_data.shape[1]),
#                       np.arange(slice_data.shape[2]))

# # 3B görselleştirme figürünü oluştur
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Veriyi görselleştir
# ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=slice_data.flatten(), cmap='gray', s=0.1)

# # Eksenleri ayarla
# ax.set_xlim(0, slice_data.shape[0])
# ax.set_ylim(0, slice_data.shape[1])
# ax.set_zlim(0, slice_data.shape[2])

# # Görüntüle
# plt.show()
# slice_index = 49  # Önceki hata düzeltildi

# # Seçilen kesiti al
# slice_data = normalized_volume[:, :, slice_index]

# # Kesiti görselleştir
# plt.imshow(slice_data, cmap='gray')
# plt.axis('off')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Örnek veri boyutları
width = 100
height = 100
depth = 50

# Örnek beyin MR verisi oluştur
volume = np.random.rand(width, height, depth)

# Veriyi normalize et
normalized_volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))

# Veriyi 3B olarak yeniden şekillendir
x, y, z = np.meshgrid(np.arange(width),
                      np.arange(height),
                      np.arange(depth))

# 3B görselleştirme figürünü oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Veriyi görselleştir
ax.scatter(x.flatten(), y.flatten(), z.flatten(), c=normalized_volume.flatten(), cmap='gray', s=0.1)

# Eksenleri ayarla
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_zlim(0, depth)

# Görüntüle
plt.show()
