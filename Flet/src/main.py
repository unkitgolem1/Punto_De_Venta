import flet as ft 
from PVT import PVT
from temp import main_container_encapsulado

class PVTGUI:
    def __init__(self):
        self.pvt = PVT()

    def main(self, page: ft.Page):
        page.title = 'Punto de venta'
        page.padding = 20
        page.theme_mode = 'dark'

        # Botones verticales del lado izquierdo
        botones_izquierdos = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="Productos",
                    icon=ft.icons.SHOPPING_CART,
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Ventas",
                    icon=ft.icons.POINT_OF_SALE,
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Reportes",
                    icon=ft.icons.ASSESSMENT,
                    width=200,
                    height=50,
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )

        # Contenedor central (espacio vacío para contenido futuro)
        contenido_central = main_container_encapsulado()

        
        # Contenedor derecho (para el ticket)
        ticket_derecho = ft.Container(
            content=ft.Text("Área del ticket"),
            width=300,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=10,
            padding=20,
        )

        # Row principal que contiene las tres secciones
        layout_principal = ft.Row(
            controls=[
                contenido_central,
                ft.VerticalDivider(),
                ticket_derecho,
            ],
            spacing=20,
            expand=True,
        )

        page.add(layout_principal)

def main(): 
    app = PVTGUI()
    ft.app(target=app.main)

if __name__ == "__main__":
    main()