import sys
from PyQt5.QtCore import Qt,QVariant,QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# QtQuick uygulamasını başlat
app = QGuiApplication(sys.argv)

# QQmlApplicationEngine oluştur
engine = QQmlApplicationEngine()

# Ana QML dosyasını yükle
engine.load("main.qml")

engine.load(QUrl.fromLocalFile("./main.qml"))


# Örnek veri boyutları
width = 100
height = 100
# depth = 50
depth = 22
num_images = 22

# Resimleri oku ve normalize et
normalized_volumes = []
for i in range(num_images):
    i+=1
    image = cv2.imread("../mri_shoulders/Seri1/"+str(i)+".jpg", cv2.IMREAD_GRAYSCALE)
    image_resized = cv2.resize(image, (width, height))

    # Resmi normalize et
    normalized_volume = (image_resized - np.min(image_resized)) / (np.max(image_resized) - np.min(image_resized))
    normalized_volumes.append(normalized_volume)




# Canvas3D elemanını bul
root_obj = engine.rootObjects()[0]
canvas3d_item = root_obj.findChild(QObject, "canvas3D")

# 3D verileri hazırla (normalized_volumes listesini kullanarak)
data_list = []
for normalized_volume in normalized_volumes:
    data_list.append(QVariant.fromList(normalized_volume.flatten().tolist()))


# Canvas3D elemanına verileri aktar
canvas3d_item.setProperty("data", data_list)

# Uygulamayı çalıştır
sys.exit(app.exec())
