from datetime import date, timedelta

class Material:
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = True

    def mostrar_detalle(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.idMaterial} | {self.titulo} ({self.añoPublicacion}) - {estado}"

class Libro(Material):
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, autor: str, isbn: str, genero: str):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, edicion: int, periodicidad: str):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, tipoArchivo: str, urlDescarga: str, tamanoMB: float):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamanoMB = tamanoMB

class Persona:
    def __init__(self, idPersona: int, nombre: str):
        self.idPersona = idPersona
        self.nombre = nombre

class Usuario(Persona):
    def __init__(self, idPersona: int, nombre: str, limitePrestamos: int):
        super().__init__(idPersona, nombre)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []

    def mostrar_detalle(self):
        return f"Usuario: {self.nombre} | Limite: {self.limitePrestamos} | Prestamos activos: {len(self.listaActiva)}"

class Sucursal:
    def __init__(self, idSucursal: int, nombre: str):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

    def agregar_material(self, material: Material):
        self.catalogoLocal.append(material)

class Bibliotecario(Persona):
    def __init__(self, idPersona: int, nombre: str):
        super().__init__(idPersona, nombre)

    def gestionarPrestamo(self, usuario: Usuario, material: Material):
        if material.disponible and len(usuario.listaActiva) < usuario.limitePrestamos:
            material.disponible = False
            prestamo = Prestamo(len(usuario.listaActiva) + 1, date.today(), date.today() + timedelta(days=7), usuario, material)
            usuario.listaActiva.append(prestamo)
            return prestamo
        return None

    def transferirMaterial(self, material: Material, sucursalOrigen: Sucursal, sucursalDestino: Sucursal):
        if material in sucursalOrigen.catalogoLocal:
            sucursalOrigen.catalogoLocal.remove(material)
            sucursalDestino.agregar_material(material)
            return True
        return False

class Prestamo:
    def __init__(self, idPrestamo: int, fechaInicio: date, fechaDevolucion: date, usuario: Usuario, material: Material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto: float, motivo: str):
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def calcularMulta(self, dias_retraso: int):
        self.monto = dias_retraso * 25.50  # $25.50 por día de retraso
        return self.monto

    def bloquearUsuario(self, usuario: Usuario):
        usuario.limitePrestamos = 0
        return f"Usuario {usuario.nombre} bloqueado por multas pendientes."

class Catalogo:
    def buscarPorAutor(self, autor: str, lista_materiales: list):
        return [m for m in lista_materiales if isinstance(m, Libro) and m.autor.lower() == autor.lower()]

    def buscarEnTodasSucursales(self, titulo: str, sucursales: list):
        resultados = []
        for sucursal in sucursales:
            for material in sucursal.catalogoLocal:
                if titulo.lower() in material.titulo.lower():
                    resultados.append((sucursal.nombre, material))
        return resultados