from Productos import Item_Productos

class Ticket:
    def __init__(self):
        self.items = []
        self.estado = 'Efectivo'

    def agregar_Item(self, item):
        self.items.append(item)
    
    def remover_Item(self, item):
        self.items.remove(item)
    
    def calcular_Total(self):
        total = 0 
        for item in self.items[:]:
            total += item.calcular_Subtotal()
        return total 

    def cambiar_estado(self, nuevo_Estado):
        estado_Valido = ['Efectivo', 'Tarjeta']
        if nuevo_Estado in estado_Valido:
            self.estado = nuevo_Estado  
            return True
        return False


