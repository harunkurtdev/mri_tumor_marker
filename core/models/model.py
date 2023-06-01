import numpy as np

import base64


from glob import glob
from tqdm import tqdm

import cv2


class Distance:

    def get_distance(self, p1: int, p2: int) -> float:
        return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def get_mid_point(self, p1: int, p2: int) -> tuple:
        midpoint = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
        return midpoint

    def get_points(self, index, approx) -> list:
        p1 = tuple(approx[index][0])
        p2 = tuple(approx[(index + 1) % len(approx)][0])
        return [p1, p2]


class Shape:

    @staticmethod
    def get_widt_height(img):
        return img.shape

    def get_center_radius(self, approx) -> cv2.minEnclosingCircle:
        return cv2.minEnclosingCircle(approx)

    def get_center(self, center) -> tuple:
        return tuple(map(int, center))


class Kernel2Img:

    # def __init__(self) :
    #     self.img

    def get_blur_guassian(self, gray_image, matrix: int = 3) -> cv2.GaussianBlur:
        return cv2.GaussianBlur(gray_image, (matrix, matrix), 0)

    def get_kernel_5x5(self) -> np.ones:
        return np.ones((5, 5), np.uint8)

    def get_kernel_3x3(self) -> np.ones:
        return np.ones((3, 3), np.uint8)

    def get_img2dilation(self, blur_image: cv2.Mat) -> cv2.dilate:
        return cv2.dilate(blur_image, self.get_kernel_5x5(), iterations=3)

    def get_img2erosion(self, img: cv2.Mat) -> cv2.erode:
        return cv2.erode(img, self.get_kernel_5x5(), iterations=3)

    def get_gray_image(self, img: cv2.Mat) -> cv2.cvtColor:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def get_image_read(self, img_path: str):
        return cv2.imread(img_path)

    def get_edges(self, img) -> cv2.Canny:
        return cv2.Canny(img, 30, 60)

    def get_find4contorus(self, edges):
        contours, _ = cv2.findContours(
            edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def clahe_process(self, img: cv2.Mat, clip_limit=2.0, tile_grid_size=(8, 8)) -> cv2.Mat:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=clip_limit,
                                tileGridSize=tile_grid_size)
        return clahe.apply(gray)

    def local_histogram_equalization(self, img: cv2.Mat,condution:float=100) -> cv2.Mat:

        # Filtering
        blurred = cv2.bilateralFilter(img, 5, 8, 8)
        # blurred = cv2.GaussianBlur(equalized, (3, 3), 0)
        kernel = np.array(
            [[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
        sharpened = cv2.filter2D(blurred, -1, kernel)
        result = np.where(sharpened > np.mean(sharpened)*condution/100, sharpened, 0)
        return result

    def addImg(self, img1: cv2.Mat, img2: cv2.Mat, alpha=1, beta=1) -> cv2.Mat:
        return cv2.addWeighted(img1, alpha, self.add_resize_imgs(img1, img2), beta, 0.0)

    def img2Base64(self, img) -> str:
        retval, buffer = cv2.imencode('.jpg', img)
        base64Image = base64.b64encode(buffer)
        return base64Image.decode("utf-8")

    def get_epsilon(self, contour):
        return (0.01 * cv2.arcLength(contour, True))

    def add_resize_imgs(self, img1: cv2.Mat, img2: cv2.Mat) -> cv2.Mat:
        return cv2.resize(img1, (img2.shape[1], img2.shape[0]))

    def get_resize_img(self, img, new_height=500) -> cv2.Mat:
        height, width, channels = img.shape
        new_width = int(new_height * (width / height))
        img = cv2.resize(img, (new_width, new_height))
        return img

    def get_approx(self, contour) -> cv2.approxPolyDP:
        return cv2.approxPolyDP(contour, self.get_epsilon(contour), True)

    def get_zero_image(self, img_zero_shape: Shape.get_widt_height) -> np.zeros:
        print(type(img_zero_shape))
        return np.zeros(img_zero_shape, np.uint8)


class GetImages:
    color_radius = (100, 100, 100)
    color_distance = (50, 50, 50)

    def __init__(self, fileType="*.jpeg", filesPath='/HW1/images/'):
        self.fileType = fileType
        self.filesPath = filesPath

    def get_point_distance(self, img, midpoint: int, p1: int, p2: int, distance: float) -> cv2.Mat:

        if (distance > 30):
            cv2.putText(img, f" D: {distance:.1f}",
                        midpoint, cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.color_distance, 1)
        return img

    def get_line_img(self, img: cv2.Mat, pt1: tuple = (0, 0), pt2: tuple = (0, 0)) -> cv2.Mat:
        cv2.line(img, pt1=pt1, pt2=pt2, color=(0, 0, 255), thickness=1)
        return img

    def get_text_radius_img(self, radius: int, center: int, img) -> cv2.Mat:
        cv2.putText(
            img, f"R: {radius}", center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.color_radius, 1)
        return img

    def getImages4Glob(self) -> list:
        return glob(self.filesPath+self.fileType)

    def getImages4tqdm(self) -> list:
        return tqdm(self.getImages4Glob())


class Proccess4Draw(Distance, Shape, GetImages, Kernel2Img):
    # static color
    color = (50, 50, 50)
    radiusColor = (100, 100, 100)
    p1 = 0
    p2 = 1

    def __init__(self, fileType: str="", filesPath: str=""):
        GetImages.__init__(self, fileType=fileType, filesPath=filesPath)
        Distance.__init__(self)
        Shape.__init__(self,)
        Kernel2Img.__init__(self,)

    def draw_countur(self, contours, img) -> cv2.Mat:
        for contour in contours:
            approx = self.get_approx(contour)
            for i in range(len(approx)):
                get_points = self.get_points(index=i, approx=approx)
                p1 = get_points[self.p1]
                p2 = get_points[self.p2]
                cv2.line(img, p1,
                         p2, self.color, 2)
                img = self.get_point_distance(img=img, p1=p1, p2=p2, midpoint=self.get_mid_point(p1, p2), distance=self.get_distance(
                    p1, p2))

            if len(approx) > 10:
                center = self.get_center(self.get_center_radius(approx)[0])
                radius = int(self.get_center_radius(approx)[1])
                img = self.get_text_radius_img(
                    radius=radius, center=center, img=img)

        return img


class Image2Drawer(Proccess4Draw):
    def __init__(self, fileType: str, filesPath: str):
        Proccess4Draw.__init__(self, fileType=fileType, filesPath=filesPath)

    def drawed_img(self, image) -> cv2.Mat:
        # print(image_path, " gelen image türü",
        #           Shape.get_widt_height(image))
        backend_image = self.get_zero_image(Shape.get_widt_height(image))
        gray_image = self.get_gray_image(image)
        blur = self.get_blur_guassian(gray_image)
        dilation = self.get_img2dilation(blur)
        erosion = self.get_img2erosion(dilation)
        get_edges = self.get_edges(erosion)
        contours = self.get_find4contorus(get_edges)
        drawed_img = self.draw_countur(contours, backend_image)
        return drawed_img

    def draw_paper_show(self):
        for image_path in self.getImages4tqdm():

            image = self.get_image_read(image_path)
            drawed_img = self.drawed_img(image)
            cv2.imshow("drawed_img", drawed_img)
            # cv2.imshow("backend_image", backend_image)
            # time.sleep(2)
            cv2.waitKey(5000)


if __name__ == '__main__':
    import os
    import time
    fileType = "*.jpeg"
    filesPath = os.getcwd()+'/HW1/images/'
    # Image2Drawer(filesPath=filesPath, fileType=fileType).draw_paper_show()
