import flet as ft

def home_page(page: ft.Page):
    page.add(
        ft.Column([
            ft.Text("Bem Vindo ao Home Food!", size=24),
            ft.Text("Estamos felizes por você escolher nosso serviço. Aproveite a deliciosa comida caseira e a comodidade de receber em sua casa.")
        ], alignment=ft.alignment.center)
    )
