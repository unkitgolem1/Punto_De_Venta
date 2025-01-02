import flet as ft



#####################################

def create_cupertino_button(a = 'Galletas',b = 'Sabritas',c = 'Refrescos'):
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
#modificar para funcion de cambiar imagen
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
        #aqui modificar
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


def contenedor_tab1():
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[create_cupertino_button()],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        create_navigation_button('<'),
                        create_product_image('png-clipart-coca-cola-coca-cola.png'),
                        create_navigation_button('>')
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[ft.Text('NOMBRE DEL PRODUCTO EN PANTALLA')],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        ft.FilledTonalButton(
                            text="Filled tonal button",
                            on_click=lambda e: print("clicked!")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

def contenedor_tab2():
    pass
def contenedor_tab3():
    pass


def main_container_encapsulado():
    # Creamos los contenidos de cada tab
    tab1_content = ft.Container(
        content=contenedor_tab1(),
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
                text="Ventas",
                icon=ft.icons.HOME,
                content=tab1_content
            ),
            ft.Tab(
                text="Update Procucto",
                icon=ft.icons.SETTINGS,
                content=tab2_content
            ),
            ft.Tab(
                text="Crear Producto",
                icon=ft.icons.IMAGE,
                content=tab3_content
            ),
        ],
        tab_alignment=ft.TabAlignment.CENTER,
        expand=1
    )

    # Contenedor principal que contiene los tabs
    return ft.Container(
        theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
        theme_mode=ft.ThemeMode.DARK,
        content=tabs,
        expand=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        border_radius=10,
        padding=10,
    )
