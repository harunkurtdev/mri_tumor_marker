
from . import home_view_model as homemodel

import flet as ft
import core.components.button as button


class HomeView(homemodel.HomeViewModel):
    def __init__(self, page):
        # super(ClassName, self).__init__(*args))
        homemodel.HomeViewModel.__init__(self, page)

    def baseView(self):
        self.page.add(ft.Container(
            ft.Column(
                [
                    ft.Row(

                        [
                            self.baseImage,
                            ft.Container(
                                self.baseChart,
                                width=self.page.width*25/100
                            ),
                            button.ProjectButton(
                                text="Update Image", color=ft.colors.RED, on_click=lambda _: self.pick_files_dialog.pick_files(
                                    allow_multiple=True
                                ),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                    ft.Container(
                        content=ft.Slider(
                            min=0, max=100, divisions=20, label="{value}%", on_change=self.slider_changed),
                        height=20,
                        width=int(self.page.width-100),
                        padding=ft.Padding(
                            right=100, left=100, top=0, bottom=0)
                    ),
                    self.t,
                    self.z,
                    ft.Row(
                        [
                            ft.GestureDetector(
                                mouse_cursor=ft.MouseCursor.MOVE,
                                drag_interval=10,
                                on_vertical_drag_start=self.on_pan_update1,
                                content=self.processImage),
                            ft.Container(
                                self.processChart,
                                width=self.page.width*25/100
                            ),
                            button.ProjectButton(
                                text="Proccesing Image", color=ft.colors.RED, on_click=self.process),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.Padding(left=100, right=100, top=0, bottom=0)
        ))
