from enum import Enum

class Rol(Enum):
    BARISTA = 1
    MESERO = 2
    GERENTE = 3

class Temperatura(Enum):
    FRIA = 1
    CALIENTE = 2

class EstadoPedido(Enum):
    PENDIENTE = 1
    PREPARANDO = 2
    ENTREGADO = 3

#Personas
class Persona():
    def __init__(self, id_persona: int, nombre: str, email: str):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def login(self):
        return f"Login: {self.nombre} ha iniciado sesión en el sistema"

    def actualizar_perfil(self, nuevo_email: str):
        self.email = nuevo_email
        return f"Email actualizado a: {self.email}"

class Cliente(Persona):
    def __init__(self, id_persona: int, nombre: str, email: str, puntos_fidelidad: int = 0):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad = puntos_fidelidad
        self.historial_pedidos = []

    def realizar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)
        self.puntos_fidelidad += 15  # 
        return f"{self.nombre} realizó el pedido #{pedido.id_pedido}."

    def consultar_historial(self):
        pedidos_ids = [p.id_pedido for p in self.historial_pedidos]
        return f"Historial de {self.nombre}: Pedidos {pedidos_ids}"

    def canjear_puntos(self, puntos_a_canjear: int):
        if self.puntos_fidelidad >= puntos_a_canjear:
            self.puntos_fidelidad -= puntos_a_canjear
            return f"Canje exitoso, puntos restantes: {self.puntos_fidelidad}"
        return "Saldo insuficiente para canjear"

    def mostrar_detalle(self):
        return f"Cliente: {self.nombre} | Email: {self.email} | Puntos: {self.puntos_fidelidad}"


class Empleado(Persona):
    def __init__(self, id_persona: int, nombre: str, email: str, id_empleado: str, rol: Rol):
        super().__init__(id_persona, nombre, email)
        self.id_empleado = id_empleado
        self.rol = rol

    def actualizar_inventario(self, inventario, ingrediente: str, cantidad: int):
        inventario.ingredientes[ingrediente] = inventario.ingredientes.get(ingrediente, 0) + cantidad
        return f"{self.nombre} agregó {cantidad} de {ingrediente}"

    def cambiar_estado_pedido(self, pedido, nuevo_estado: EstadoPedido):
        pedido.estado = nuevo_estado
        return f"Pedido #{pedido.id_pedido} cambiado a {nuevo_estado.name} por {self.nombre}"
    
    def mostrar_detalle(self):
        return f"Empleado: {self.nombre} | ID Emp: {self.id_empleado} | Rol: {self.rol.name}"


#Productos
class ProductoBase:
    def __init__(self, id_producto: int, nombre: str, precio_base: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_base = precio_base

class Bebida(ProductoBase):
    def __init__(self, id_producto: int, nombre: str, precio_base: float, tamaño: str, temperatura: Temperatura):
        super().__init__(id_producto, nombre, precio_base)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = []

    def agregar_extra(self, extra: str):
        self.modificadores.append(extra)
        return f"Se agrego '{extra}' a la bebida {self.nombre}"

    def calcular_precio_final(self):
        # Cada modificador extra suma $10 al precio base
        return self.precio_base + (len(self.modificadores) * 10)
    
    def mostrar_detalle(self):
        return f"Bebida: {self.nombre} | Tamaño: {self.tamaño} | Temp: {self.temperatura.name} | Base: ${self.precio_base}"

class Postre(ProductoBase):
    def __init__(self, id_producto: int, nombre: str, precio_base: float, es_vegano: bool, sin_gluten: bool):
        super().__init__(id_producto, nombre, precio_base)
        self.es_vegano = es_vegano
        self.sin_gluten = sin_gluten
    
    def mostrar_detalle(self):
        vegano = "Si" if self.es_vegano else "No"
        gluten = "Si" if self.sin_gluten else "No"
        return f"Postre: {self.nombre} | Vegano: {vegano} | Sin Gluten: {gluten} | Precio: ${self.precio_base}"


#Ventas
class Pedido:
    def __init__(self, id_pedido: int, productos: list):
        self.id_pedido = id_pedido
        self.productos = productos
        self.estado = EstadoPedido.PENDIENTE
        self.total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for prod in self.productos:
            if isinstance(prod, Bebida):
                total += prod.calcular_precio_final()
            else:
                total += prod.precio_base
        self.total = total
        return total

    def validar_stock(self, inventario):
        if not inventario.ingredientes:
            return "No hay ingredientes registrados en el inventario"
        return f"Stock validado para el pedido #{self.id_pedido}"
    
    def mostrar_detalle(self):
        nombres_prod = [p.nombre for p in self.productos]
        return f"Pedido #{self.id_pedido} | Total: ${self.total} | Estado: {self.estado.name} | Items: {nombres_prod}"

class Inventario:
    def __init__(self, id_sucursal: int):
        self.id_sucursal = id_sucursal
        self.ingredientes = {}

    def reducir_stock(self, ingrediente: str, cantidad: int):
        if self.ingredientes.get(ingrediente, 0) >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            return f"Se redujeron {cantidad} unidades de {ingrediente}"
        else:
            return self.notificar_faltante(ingrediente)

    def notificar_faltante(self, ingrediente: str):
        return f"Faltante de '{ingrediente}' en sucursal {self.id_sucursal}. Reabastecer"
    
    def mostrar_detalle(self):
        return f"Inventario sucursal {self.id_sucursal} | Items actuales: {len(self.ingredientes)}"