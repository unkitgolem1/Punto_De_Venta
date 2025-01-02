class Productos:
    def __init__ (self):
        self.galletas = []
        self.sabritas = []
        
        self.refrescos =[]
    
    #metodos de la clase productos
    #agregar productos
    def agregar_Galletas (self, nombre, precio):
        galleta = Galletas(nombre, precio)
        self.galletas.append(galleta)    
        return galleta
    
    def agregar_Sabritas (self, nombre, precio):
        sabrita = Sabritas(nombre, precio)
        self.sabritas.append(sabrita)
        return sabrita
    
    def agregar_Refrescos(self, nombre, precio):
        refresco = Refrescos(nombre, precio)
        self.refrescos.append(refresco)
        return refresco
    
    #Eliminar Productos
    def eliminar_Item(self, nombre, tipo):
 
        if tipo == 'Galletas':
            items = self.galletas
        elif tipo == 'Sabritas':
            items == self.sabritas
        elif tipo == 'Refresco':
            items == self.refrescos 
        else:
            return False
        
        for item in items[:]:
            if item.nombre == nombre:
                items.remove(item)
                return True
        return False
    
    
    def eliminar_Galletas(self, nombre):
        return self.eliminar_Item(nombre, tipo='Galletas')
    
    def eliminar_Sabritas(self, nombre):
        return self.eliminar_Item(nombre, tipo='Sabritas')
 
    def eliminar_Refresco(self, nombre):
        return self.eliminar_Item(nombre, tipo='Refresco')
    
    def obtener_Item(self, nombre, tipo):

        if tipo == 'Galletas':
            items = self.galletas
        elif tipo == 'Sabritas':
            items == self.sabritas
        elif tipo == 'Refresco':
            items == self.refrescos 
        else:
            return None
        

        for item in items[:]:
            if item.nombre == nombre:
                return item
        return None
    

class Item_Productos:
    def __init__ (self, nombre, precio, cantidad=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_Subtotal(self):
        return self.precio * self.cantidad
    
class Galletas (Item_Productos):
    def __init__ (self, nombre, precio, cantidad=0):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = 'Galleta'

class Sabritas (Item_Productos):
    def __init__ (self, nombre, precio, cantidad=0):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = 'Sabritas'

class Refrescos (Item_Productos):
    def __init__ (self, nombre, precio, cantidad=0):
        super().__init__(self, nombre, precio, cantidad)
        self.tipo = 'Refrescos'



