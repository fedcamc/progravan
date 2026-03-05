from enum import Enum
from datetime import datetime

class RolEmpleado(Enum):
    TAQUILLERO = 1
    ADMIN = 2
    LIMPIEZA = 3

class TipoSala(Enum):
    D2 = "2D"
    D3 = "3D"
    IMAX = "IMAX"

class EstadoReserva(Enum):
    PENDIENTE = 1
    PAGADA = 2
    CANCELADA = 3

#Creamos la clase persona
class Persona:
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        return f"{self.nombre} ha iniciado sesion"

    def logout(self):
        return f"{self.nombre} ha cerrado sesion"

    def actualizarDatos(self, nuevo_email):
        self.email = nuevo_email
        return "Datos actualizados"

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono, puntosFidelidad=0):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad = puntosFidelidad
        self.historialReservas = []

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)
        return "Reserva añadida al historial"

    def consultarPromociones(self, promociones_activas):
        return [p.descripcion for p in promociones_activas if p.esValida(self)]

    def cancelarReserva(self, idReserva):
        for reserva in self.historialReservas:
            if reserva.idReserva == idReserva:
                reserva.estado = EstadoReserva.CANCELADA

                #se liberan asientos de la funcion
                for asiento in reserva.asientos:
                    if asiento in reserva.funcion.asientos_ocupados:
                        reserva.funcion.asientos_ocupados.remove(asiento)
                return f"Reserva {idReserva} cancelada"
        return "Reserva no encontrada"

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        return f"Empleado {self.nombre} marcó entrada a las {datetime.now().strftime('%H:%M')}."

    def gestionarFunciones(self, funcion):
        if self.rol == RolEmpleado.ADMIN:
            return f"Función de '{funcion.pelicula.titulo}' gestionada correctamente"
        return "Se requiere rol de administrador"

class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.en_mantenimiento = False

    def verificarDisponibilidad(self):
        return "No disponible" if self.en_mantenimiento else "Disponible"

    def limpiarEspacio(self):
        self.en_mantenimiento = False
        return f"El espacio '{self.nombre}' ha sido limpiado y está listo."

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip

    def ajustarAforo(self, nuevos_asientos):
        self.capacidadTotal = nuevos_asientos
        return f"Aforo ajustado a {self.capacidadTotal} asientos."

    def obtenerTipoSala(self):
        return self.tipo.value

class Producto:
    def __init__(self, id_prod, nombre, precio, categoria):
        self.id_prod = id_prod
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def mostrar_detalle(self):
        return f"ID: {self.id_prod} | {self.nombre} (${self.precio:.1f}) | Cat: {self.categoria}"

class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def actualizarInventario(self, producto, cantidad):
        if producto not in self.listaProductos:
            self.listaProductos.append(producto)
        self.stockActual[producto.nombre] = self.stockActual.get(producto.nombre, 0) + cantidad
        return f"Inventario de {producto.nombre} actualizado a {self.stockActual[producto.nombre]}"

    def venderProducto(self, nombre_producto, cantidad):
        if self.stockActual.get(nombre_producto, 0) >= cantidad:
            self.stockActual[nombre_producto] -= cantidad
            return f"Venta exitosa, quedan {self.stockActual[nombre_producto]} unidades de {nombre_producto}"
        return f"Stock insuficiente para {nombre_producto}"

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        return f"{self.titulo}: Una increíble aventura de {self.genero}"

    def esAptaParaTodoPublico(self):
        return self.clasificacion in ["A", "AA"]

class Funcion:
    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.asientos_ocupados = []

    def calcAsientos(self):
        return self.sala.capacidadTotal - len(self.asientos_ocupados)

    def detallesFun(self):
        return f"{self.pelicula.titulo} | Sala {self.sala.nombre} ({self.sala.tipo.value}) | Inicio: {self.horarioInicio}"

class Promocion:
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion

    def esValida(self, usuario):
        return datetime.now() <= self.fechaExpiracion

    def aplicarDescuento(self, monto):
        return monto - (monto * (self.porcentajeDescuento / 100))

class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos 
        self.estado = EstadoReserva.PENDIENTE
        self.montoTotal = self.funcion.precioBase * len(self.asientos)

    def seleccasientos(self):
        for asiento in self.asientos:
            if asiento in self.funcion.asientos_ocupados:
                return False, asiento
        
        for asiento in self.asientos:
            self.funcion.asientos_ocupados.append(asiento)
        return True, None

    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)
            return True
        return False

    def confirmarPago(self):
        self.estado = EstadoReserva.PAGADA
        self.usuario.crearReserva(self)
        return "Pago confirmado"

    def generarTicket(self):
        return f"Ticket generado en PDF para reserva #{self.idReserva}"