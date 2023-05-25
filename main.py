import flet as ft
import core.components.button as button

import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

import ui.homeView.home_view as homeView


def main(page: ft.Page):
    page.title = "MKT4830 | Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    homeView.HomeView(page).baseView()


ft.app(target=main, assets_dir="assets")
