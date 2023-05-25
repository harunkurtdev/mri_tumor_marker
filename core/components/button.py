import flet as ft

class ProjectButton(ft.ElevatedButton):
    def __init__(self,text,color,on_click):
        ft.ElevatedButton.__init__(self=self,text=text,bgcolor=color,color=ft.colors.WHITE,on_click=on_click)