import os

import flet as ft

import ui.homeView.home_view as homeView


def main(page: ft.Page):
    page.title = "MKT4830 | Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    homeView.HomeView(page).baseView()


ft.app(target=main, port=os.getenv("PORT"), assets_dir="assets")
