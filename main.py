import os

import flet as ft
from dotenv import load_dotenv

import ui.homeView.home_view as homeView


def main(page: ft.Page):
    load_dotenv()
    page.title = "MKT4830 | Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    homeView.HomeView(page).baseView()


ft.app(target=main, port=os.getenv("PORT"), assets_dir="assets")
