import flet as ft
class Interfaz:
    def __init__(self):
        def create_cupertino_button(a ,b , c = ''):
            """Crear el botón de segmento tipo Cupertino"""
            return ft.CupertinoSegmentedButton(
                selected_index=1,
                selected_color=ft.Colors.RED_400,
                on_change=lambda e: print(f"selected_index: {e.data}"),
                controls=[
                    ft.Text(a),
                    ft.Container(
                        padding=ft.padding.symmetric(0, 30),
                        content=ft.Text(b),
                    ),
                    ft.Container(
                        padding=ft.padding.symmetric(0, 10),
                        content=ft.Text(c),
                    ),
                ]
            )

        def create_navigation_button(text):
            """Crear botón de navegación reutilizable"""
            return ft.Container(
                content=ft.Text(text),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=150,
                height=300,
                border_radius=10,
                ink=True,
                on_click=lambda e: print(f"{text} clicked!"),
            )

        def create_product_image(imagen = ''):
            """Crear imagen del producto"""
            return ft.Image(
                src=imagen,
                width=300,
                height=300,
                fit=ft.ImageFit.CONTAIN,
                border_radius=10
            )
        
    
        

  