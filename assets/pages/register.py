import flet as ft
from ..database import insert_user

def register_page(page: ft.Page):
    reg_username = ft.TextField(label="Nome de Usuário", width=300)
    reg_email = ft.TextField(label="Email", width=300)
    reg_phone = ft.TextField(label="Telefone", width=300)
    reg_cpf = ft.TextField(label="CPF", width=300)
    reg_password = ft.TextField(label="Senha", password=True, width=300)

    def register(e):
        username = reg_username.value
        email = reg_email.value
        phone = reg_phone.value
        cpf = reg_cpf.value
        password = reg_password.value
        
        insert_user(username, email, phone, cpf, password)
        page.snack_bar = ft.SnackBar(ft.Text("Registration Successful"), open=True)
        page.go("/login")

    page.add(
        ft.Column([
            ft.Text("Cadastro", size=24),
            reg_username,
            reg_email,
            reg_phone,
            reg_cpf,
            reg_password,
            ft.ElevatedButton("Sign Up", on_click=register),
            ft.ElevatedButton("Back", on_click=lambda e: page.go("/"))
        ], alignment=ft.alignment.center)
    )
