import flet as ft

# flutter - mobile app

class AuthUI:

    def __init__(self, page: ft.Page):
        page.title = "Powered by Rustambek"
        page.theme_mode = ft.ThemeMode.DARK
        self.page = page
        self.main()

    def main(self):
        self.username_input = ft.TextField(label="Username", width=300)
        self.password_input = ft.TextField(label="Password", password=True, width=300)
        self.login_button = ft.ElevatedButton(text="Login", on_click=self.on_login)

        self.reg_username_input = ft.TextField(label="Username", width=300)
        self.reg_password_input = ft.TextField(label="Password", password=True, width=300)
        self.confirm_password_input = ft.TextField(label="Confirm Password", password=True, width=300)
        self.register_button = ft.ElevatedButton(text="Register", on_click=self.on_register)
        self.show_login_screen()

    def change_theme_dark(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()

    def change_theme_light(self, e):
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

    def dropdown_build(self):
        body = ft.Container(
            ft.Row(
                [
                    ft.Text("Theme: "),
                    ft.Dropdown(
                        options=[
                            ft.dropdown.Option("Light", on_click=self.change_theme_light),
                            ft.dropdown.Option("Dark", on_click=self.change_theme_dark)
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        return body

    def show_login_screen(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [
                    ft.Column(
                        [
                            ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                            self.username_input,
                            self.password_input,
                            self.login_button,
                            ft.TextButton("Register", on_click=self.show_registration_screen),
                            self.dropdown_build()
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ]
            )
        )
        self.page.update()

    def clean_all_input(self):
        self.username_input.value = ''
        self.password_input.value = ""
        self.reg_password_input.value = ""
        self.confirm_password_input.value = ""

    def show_welcome_screen(self):
        self.clean_all_input()
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/welcome",
                [
                    ft.Text("Hello Admin!", size=30, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Logout", on_click=self.on_logout)
                ]
            )
        )
        self.page.update()

    def show_registration_screen(self, e):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/register",
                [
                    ft.Column(
                        [
                            ft.Text("Register", size=30, weight=ft.FontWeight.BOLD),
                            self.reg_username_input,
                            self.reg_password_input,
                            self.confirm_password_input,
                            self.register_button,
                            ft.TextButton("Back to Login", on_click=lambda e: self.show_login_screen()),
                            self.dropdown_build()

                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ]
            )
        )
        self.page.update()

    def on_login(self, e):
        username = self.username_input.value
        password = self.password_input.value
        if username == "admin" and password == "admin":
            self.show_welcome_screen()
        else:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Invalid username or password", color=ft.colors.RED)
            )
            self.page.snack_bar.open = True
            self.page.update()

    def on_register(self, e):
        username = self.reg_username_input.value
        password = self.reg_password_input.value
        confirm_password = self.confirm_password_input.value

        if password != confirm_password:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Passwords do not match", color=ft.colors.RED)
            )
            self.page.snack_bar.open = True
            self.page.update()
            return

        self.page.snack_bar = ft.SnackBar(
            ft.Text("Registration successful!", color=ft.colors.GREEN)
        )
        self.page.snack_bar.open = True
        self.page.update()
        self.show_login_screen()

    def on_logout(self, e):
        self.show_login_screen()


ft.app(target=AuthUI)
