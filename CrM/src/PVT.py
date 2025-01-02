from Productos import Productos

class PVT:
    def __init__ (self):
        self.productos = Productos()

    def inicializar_Productos(self):
        #agregar galletas
        self.productos.agregar_Galletas('Conquistador', 20)
        #agregar Sabritas
        self.productos.agregar_Sabritas('Fritos', 20)
        #agregar Refresco
        self.productos.agregar_Refrescos('Monster', 45)