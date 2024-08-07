import flet as ft
from ..database import get_user



def login_page(page: ft.Page):
    login_email = ft.TextField(label="Email", width=300)
    login_password = ft.TextField(label="Password", password=True, width=300)
    
    def login(e):
        email = login_email.value
        password = login_password.value
        user = get_user(email, password)
        
        if user:
            page.snack_bar = ft.SnackBar(ft.Text("Login Successful"), open=True)
            page.go("/home")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Invalid Credentials"), open=True)

    page.add(
        ft.Column([
            ft.Text("Login", size=24),
            login_email,
            login_password,
            ft.ElevatedButton("Login", on_click=login),
            ft.ElevatedButton("Back", on_click=lambda e: page.go("/"))
        ], alignment=ft.alignment.center)
    )
