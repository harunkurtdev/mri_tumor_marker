
import flet as ft
import core.models.model as model

import base64
import cv2
import numpy as np
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# from flet.matplotlib_chart import MatplotlibChart


class HomeViewModel(model.Proccess4Draw):
    def __init__(self, page: ft.Page):
        model.Proccess4Draw.__init__(self)
        imageBase64 = "iVBORw0KGgoAAAANSUhEUgAAABkAAAAgCAYAAADnnNMGAAAACXBIWXMAAAORAAADkQFnq8zdAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA6dJREFUSImllltoHFUYx3/fzOzm0lt23ZrQ1AQbtBehNpvQohgkBYVo410RwQctNE3Sh0IfiiBoIAjqi6TYrKnFy4O3oiiRavDJFi3mXomIBmOxNZe63ay52GR3Zj4f2sTEzmx3m//TYf7/c35zvgPnO6KqrESXqpq3muocAikv6m+/zytj3ejik1VN21G31YA9CgJ6xC+bMyQZPVCuarciPAMYC99V6Vw5pLbFSibHmlVoRVj9P3cmPBM8tSJI/M6mzabpfoAQ9fIF7WK4bd5vvuFnLGgy2vi0abg94A0AcJGvMq3hDxGRyar9r4F+iLAm0yIiRk8m37tctS1WsrIhhrI30+Srmg+J87OXUf3lWGS1q89dC6ltsSanxk4Aj2QBABii96300g87P/rtlrWr8l+vyDMfdlXSyyEikqxsiOUAQJCBhfHdXRfCq1LSsSlcWG+KBAGStvvrMkgiuv8lUc2mREukPwLUfHG+uTQv8Eown7VL3XlbBxYhf1c17hbVF3MDwA9bts280TnaU1YYqPby07aeFlUlHt27wSQ4CLo+F8AvoTCvHmyKF+ZbEb/M77P2LgvAwmrTHAHflN3KZxVbMC2jMFNOpgPnrMSOhvvFkMezXdwV4ePbtvHtxnJAMQ0j4JtVnO+eLb5oiSlt5HDbv7t1O90lpYCCCKbhfzW5kAIwUAazR0BlfII8Ow0I6uoVmI9MyAMwbMs8CExmDbk4zgu931MyO4OI4KrYflkRjOoTI+uM9d1vjotwKPu9QMk/sxzuO8POiVFcdZ1M2YBVsMEAKOqLvaPIe7mACuw0z/80SMH58SMplxlfiDhVi7dw2pltRhjKBQTQdrSja2KKTfE551NHuaZ0QVPvWYQUn31/Vm2nDvgjF4grVJx6suSvrvrSJ/6cSW2Oz9mf264uNrB806xZ1k/CZ49dUKgDEtlCROX2hfHpx8pGuuo3PpqYulw8fjndOp1yhgtNKRevJ1FyR2Ola+jXAjdnwTkZ6o896GdWdxDw7IxFg+0DpmXchTKSBWQnIuJn9u4j7dt+13UfHXEkXQOcuQ4kMhVtqsgUyPiQiPQfHw1NB2sRjmXKuTg1NwwBYLhtPtQX26eqTwGXPDOqvmcC4Hnwfrrad94GrVsOYTqUTkQY+iTlNe/6O1miSP/x0VB/+wMIDwHn/vtV1iQC4Xv95uUEWVCoL9Y5Z+gdovoyMHUFJHv88jmVy0vTuw7cZNv2YaA61Bfb7ZX5F8SaUv2xwZevAAAAAElFTkSuQmCC"

        self.page = page
        self.img: cv2.Mat
        self.slider_value = 100

  
        # -------------
        self.pick_files_dialog = ft.FilePicker(
            on_result=self.pick_files_result)
        self.page.overlay.append(self.pick_files_dialog)
        # -------------
        # self.baseChart = MatplotlibChart(baseFig, expand=True)
        self.baseImage = ft.Image(
            fit=ft.ImageFit.CONTAIN)
        self.baseImage.src_base64 = imageBase64
        # ----------------
        self.processImage = ft.Image(
            fit=ft.ImageFit.CONTAIN)
        self.processImage.src_base64 = imageBase64
        # self.processChart = MatplotlibChart(processFig, expand=True)
        # ----------
        self.t = ft.Text()
        self.z = ft.Text()

        self.txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def process(self, e):
        ddepth = cv2.CV_16S
        kernel_size = 3
        img1 = self.local_histogram_equalization(
            self.clahe_process(self.img), condution=self.slider_value)
        src = self.get_blur_guassian(self.img)
        dst = cv2.Laplacian(src, ddepth, ksize=kernel_size)
        img2 = cv2.convertScaleAbs(dst)

        self.first_tap = True
        self.first_x = 0
        self.first_y = 0
        self.last_x = 0
        self.last_y = 0

        processimg = self.addImg(img1=img1, img2=img2)

        self.processImage.src_base64 = self.img2Base64(
            self.resizedImage(processimg))

        hist_original, bins_original = np.histogram(
            processimg.flatten(), 256, [0, 256])

        # self.processAX.plot(hist_original, color='b')

        self.processImage.update()
        # self.processChart.update()
        self.page.update()

    def on_pan_update1(self, e: ft.DragStartEvent):
        if self.first_tap == False:
            print(e.local_x, e.local_y)
            self.first_x = e.local_x
            self.first_y = e.local_y
            self.first_tap = True
        else:
            print(e.local_x, e.local_y)
            self.last_x = e.local_x
            self.last_y = e.local_y
            self.first_tap = False

        distance = self.get_distance((self.first_x, self.first_y),
                                     (self.last_x, self.last_y))
        self.z.value = f" Mesafesi okundu {distance} ve tekrar düzenlendi"
        self.page.update()

    def slider_changed(self, e):
        self.slider_value = e.control.value
        self.t.value = f"%{e.control.value} değerinde tekrar düzenlendi"
        self.page.update()

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        global imageBase64List
        # for file in e.files:
        # print(file.name, file.path, file.size)
        self.img = cv2.imread(e.files[0].path)

        self.baseImage.src_base64 = self.img2Base64(
            self.resizedImage(self.img))

        hist_original, bins_original = np.histogram(
            self.img.flatten(), 256, [0, 256])

        # self.baseAX.plot(hist_original, color='b')

        self.baseImage.update()
        # self.baseChart.update()

    def resizedImage(self, img) -> cv2.Mat:
        scale_percent = 45  # percent of original size
        width = int(self.page.height * scale_percent / 100)
        height = int(self.page.height * scale_percent / 100)
        dim = (width, height)
        return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
