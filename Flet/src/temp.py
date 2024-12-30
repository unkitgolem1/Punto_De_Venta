import flet as ft

def main_container_encapsulado():
    # Creamos los contenidos de cada tab
    tab1_content = ft.Container(
        content=ft.Text("Contenido del Tab 1"),
        padding=20,
        alignment=ft.alignment.center,
    )

    tab2_content = ft.Container(
        content=ft.Column([
            ft.Text("Contenido del Tab 2"),
            ft.ElevatedButton("Botón en Tab 2")
        ]),
        padding=20,
        alignment=ft.alignment.center,
    )

    tab3_content = ft.Container(
        content=ft.Image(
            src="https://picsum.photos/200",
            width=200,
            height=200,
        ),
        padding=20,
        alignment=ft.alignment.center,
    )

    # Creamos los tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                icon=ft.icons.HOME,
                content=tab1_content
            ),
            ft.Tab(
                text="Tab 2",
                icon=ft.icons.SETTINGS,
                content=tab2_content
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.IMAGE,
                content=tab3_content
            ),
        ],
        expand=1
    )

    # Contenedor principal que contiene los tabs
    return ft.Container(
        content=tabs,
        expand=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        border_radius=10,
        padding=10,
    )
