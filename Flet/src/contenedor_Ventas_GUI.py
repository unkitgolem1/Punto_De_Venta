import flet as ft
from temp import main_container_encapsulado

def create_cupertino_button():
    """Crear el botón de segmento tipo Cupertino"""
    return ft.CupertinoSegmentedButton(
        selected_index=1,
        selected_color=ft.Colors.RED_400,
        on_change=lambda e: print(f"selected_index: {e.data}"),
        controls=[
            ft.Text("One"),
            ft.Container(
                padding=ft.padding.symmetric(0, 30),
                content=ft.Text("Two"),
            ),
            ft.Container(
                padding=ft.padding.symmetric(0, 10),
                content=ft.Text("Three"),
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

def create_product_image():
    """Crear imagen del producto"""
    return ft.Image(
        src='https://media.gettyimages.com/id/157726102/es/foto/cl%C3%A1sica-de-botella-de-coca-cola.jpg?s=612x612&w=0&k=20&c=xmX4zHkYcmouczHtqmpQ_PIuuL6eVYvzgvhGOOvO4gI=',
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN
    )

def create_sales_area():
    """Crear el área principal de ventas"""
    boton_cupertino = create_cupertino_button()
    boton_izquierdo = create_navigation_button("Navegación Izquierda")
    imagen = create_product_image()
    boton_derecho = create_navigation_button("Navegación Derecha")

    return ft.Column(
        controls=[
            ft.Row(
                controls=[boton_cupertino],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    boton_izquierdo,
                    imagen,
                    boton_derecho
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[ft.FilledTonalButton("AÑADIR PRODUCTO", icon="add")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def create_main_container(content):
    """Crear el contenedor principal"""
    return ft.Container(
        content=content,     
        height=600,
        expand=True,
        bgcolor=ft.colors.PURPLE,
        border_radius=10,
        alignment=ft.alignment.center
    )

def create_ticket_area():
    """Crear el área del ticket"""
    return ft.Container(
        content=ft.Text("Área del ticket"),
        width=300,
        border=ft.border.all(1, ft.colors.OUTLINE),
        border_radius=10,
        padding=20,
    )

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Tabs en Container"
    page.padding = 20
    page.theme_mode = "dark"

    # Crear componentes principales
    sales_area = create_sales_area()
    main_container = create_main_container(sales_area)
    ticket_area = create_ticket_area()


    contenedor = main_container_encapsulado()
    # Crear layout final
    fully_centered = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    contenedor,
                    ticket_area
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    page.add(fully_centered)

if __name__ == "__main__":
    ft.app(target=main)