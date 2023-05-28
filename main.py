import flet as ft

import ui.homeView.home_view as homeView


def main(page: ft.Page):
    page.title = "MKT4830 | Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    homeView.HomeView(page).baseView()


ft.app(target=main, assets_dir="assets")
