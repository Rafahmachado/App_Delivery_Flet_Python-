import flet as ft
from pages.home import home_page
from pages.login import login_page
from pages.register import register_page

def main(page: ft.Page):
    page.title = "Home Food"
    page.theme = ft.Theme(primary_color=ft.colors.RED)
    
    def show_registration(e):
        page.go("/register")
    
    def show_login(e):
        page.go("/login")
    
    page.add(
        ft.Column([
            ft.Row([
                ft.Container(
                    content=ft.Text("Home Food", size=40, color=ft.colors.WHITE),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.RED,
                    width=300,
                    height=150
                )
            ], alignment=ft.alignment.center),
            ft.Row([
                ft.ElevatedButton("Login", on_click=show_login),
                ft.ElevatedButton("Sign Up", on_click=show_registration)
            ], alignment=ft.alignment.center)
        ], alignment=ft.alignment.center)
    )

    page.routes = [
        ft.Route(path="/login", view=lambda: login_page(page)),
        ft.Route(path="/register", view=lambda: register_page(page)),
        ft.Route(path="/home", view=lambda: home_page(page))
    ]

    page.update()

ft.app(target=main)
