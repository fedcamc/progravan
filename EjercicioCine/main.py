from models import *
from datetime import datetime, timedelta

def main():
    #Registrar productos
    print("\nREGISTRO DE PRODUCTOS") #Se registran los productos
    prod1 = Producto(11, "Palomitas Caramelo", 95.0, "Snacks")
    prod2 = Producto(12, "ICEE Cereza", 55.0, "Bebidas")
    prod3 = Producto(13, "Crepa de Nutella", 65.0, "Postres")
    prod4 = Producto(14, "Dedos de Queso", 85.0, "Snacks")
    prod5 = Producto(15, "Frappe Oreo", 75.0, "Bebidas")
    prod6 = Producto(16, "Pizza Pepperoni", 110.0, "Comida")
    prod7 = Producto(17, "Entrada VIP Adulto", 160.0, "Boletos")
    prod8 = Producto(18, "Entrada IMAX Estudiante", 120.0, "Boletos")
    prod9 = Producto(19, "Combo Amigos (4 Refrescos + 2 Palomitas)", 350.0, "Combos")
    prod10 = Producto(20, "Chocolate", 40.0, "Dulces")

    print(prod1.mostrar_detalle())
    print(prod2.mostrar_detalle())
    print(prod3.mostrar_detalle())
    print(prod4.mostrar_detalle())
    print(prod5.mostrar_detalle())
    print(prod6.mostrar_detalle())
    print(prod7.mostrar_detalle())
    print(prod8.mostrar_detalle())
    print(prod9.mostrar_detalle())
    print(prod10.mostrar_detalle())

    #Peliculas
    print("\nREGISTRO DE PELÍCULAS") #Se registran las peliculas
    pel1 = Pelicula("El justiciero", 120, "B15", "Acción")
    pel2 = Pelicula("Avengers", 115, "B", "Ciencia Ficción")
    pel3 = Pelicula("No respires", 130, "C", "Terror")
    pel4 = Pelicula("Shrek", 145, "C", "Infantil")
    pel5 = Pelicula("Rio", 100, "B", "Infantil")
    pel6 = Pelicula("Volver al Futuro", 116, "A", "Ciencia Ficción")
    pel7 = Pelicula("Interestelar", 169, "B", "Ciencia Ficción")
    pel8 = Pelicula("Tenet", 150, "B15", "Acción")
    pel9 = Pelicula("Pollitos en Fuga", 136, "B15", "Infantil")
    pel10 = Pelicula("El infierno", 166, "B15", "Crimen")

    peliculas = [pel1, pel2, pel3, pel4, pel5, pel6, pel7, pel8, pel9, pel10]
    for i, p in enumerate(peliculas, 1):
        print(f"Pelicula {i}: {p.titulo} | {p.duracion} min | Clasificación: {p.clasificacion}")

    #Usuarios
    print("\nREGISTRO DE USUARIOS") #Se registran los usuarios
    usuario1 = Usuario(1, "Federico_C", "fedecamc@gmail.com", "2291234567", 500)
    usuario2 = Usuario(2, "AnaOG", "anawtf@gmail.com", "2229876543", 300)
    usuario3 = Usuario(3, "Luis2442", "luis24@gmail.com", "2291112233", 150)
    usuario4 = Usuario(4, "MartaVrl", "martavrl@gmail.com", "2224445566", 0)
    usuario5 = Usuario(5, "JosePz", "josegiga@gmail.com", "2297778899", 50)
    usuario6 = Usuario(6, "Mango99", "mangogg@gmail.com", "2222223344", 120)
    usuario7 = Usuario(7, "Jorgemp", "mpjorg@gmail.com", "2296667788", 80)
    usuario8 = Usuario(8, "SofiaL", "nosoysofia@gmail.com", "2229990011", 210)
    usuario9 = Usuario(9, "Hugohz", "hugohz@gmail.com", "2293334455", 15)
    usuario10 = Usuario(10, "dumbval", "valdum44@gmail.com", "2228889900", 400)

    usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10]
    for u in usuarios:
        print(f"ID: {u.idPersona} | Usuario: {u.nombre} | Puntos: {u.puntosFidelidad}")

    #Empleados
    print("\nREGISTRO DE EMPLEADOS") #Se registran los empleados
    emple1 = Empleado(11, "Carlos", "admin1@cine.com", "2291407476", "E1", RolEmpleado.ADMIN, "Matutino")
    emple2 = Empleado(12, "Laura", "taq1@cine.com", "2212251452", "E2", RolEmpleado.TAQUILLERO, "Matutino")
    emple3 = Empleado(13, "Pedro", "limp1@cine.com", "2254531259", "E3", RolEmpleado.LIMPIEZA, "Matutino")
    emple4 = Empleado(14, "Sofia", "admin2@cine.com", "787452134", "E4", RolEmpleado.ADMIN, "Vespertino")
    emple5 = Empleado(15, "Miguel", "taq2@cine.com", "229555000", "E5", RolEmpleado.TAQUILLERO, "Vespertino")
    emple6 = Empleado(16, "Juan", "limp2@cine.com", "2485462138", "E6", RolEmpleado.LIMPIEZA, "Vespertino")
    emple7 = Empleado(17, "Diana", "taq3@cine.com", "7851112456", "E7", RolEmpleado.TAQUILLERO, "Fines de Semana")
    emple8 = Empleado(18, "Luis", "limp3@cine.com", "135468259", "E8", RolEmpleado.LIMPIEZA, "Fines de Semana")
    emple9 = Empleado(19, "Roberto", "admin3@cine.com", "4781269543", "E9", RolEmpleado.ADMIN, "Nocturno")
    emple10 = Empleado(20, "Carmen", "taq4@cine.com", "1348795624", "E10", RolEmpleado.TAQUILLERO, "Nocturno")

    empleados = [emple1, emple2, emple3, emple4, emple5, emple6, emple7, emple8, emple9, emple10]
    for e in empleados:
        print(f"ID: {e.idEmpleado} | Nombre: {e.nombre} | Rol: {e.rol.name}")

    #Salas
    print("\nREGISTRO DE SALAS") #Se registran las salas
    sala1 = Sala(1, "Sala 01", "Planta Baja", TipoSala.D2, 100, False)
    sala2 = Sala(2, "Sala 02", "Planta Baja", TipoSala.D3, 80, False)
    sala3 = Sala(3, "Sala 03", "Planta Alta", TipoSala.IMAX, 150, False)
    sala4 = Sala(4, "Sala 04 VIP", "Planta Alta", TipoSala.D2, 50, True)
    sala5 = Sala(5, "Sala 05", "Planta Baja", TipoSala.D2, 120, False)
    sala6 = Sala(6, "Sala 06", "Planta Baja", TipoSala.D3, 90, False)
    sala7 = Sala(7, "Sala 07 IMAX", "Planta Alta", TipoSala.IMAX, 200, False)
    sala8 = Sala(8, "Sala 08 VIP", "Planta Alta", TipoSala.D3, 40, True)
    sala9 = Sala(9, "Sala 09", "Planta Baja", TipoSala.D2, 100, False)
    sala10 = Sala(10, "Sala 10", "Planta Baja", TipoSala.D2, 100, False)

    salas = [sala1, sala2, sala3, sala4, sala5, sala6, sala7, sala8, sala9, sala10]
    for s in salas:
        print(f"Sala: {s.nombre} | Tipo: {s.tipo.value} | Capacidad: {s.capacidadTotal}")

    #Promociones
    print("\nREGISTRO DE PROMOCIONES") #Se registran las promociones
    hoy = datetime.now()
    promo1 = Promocion("PROMO_BUAP", "Descuento universitario", 20.0, hoy + timedelta(days=30))
    promo2 = Promocion("MARTES_2X1", "Mitad de precio en boletos", 50.0, hoy + timedelta(days=5))
    promo3 = Promocion("MATUTINO", "Descuento antes de las 12pm", 15.0, hoy + timedelta(days=10))
    promo4 = Promocion("VIP_PASS", "Descuento en salas VIP", 25.0, hoy + timedelta(days=20))
    promo5 = Promocion("ESTRENO_IMAX", "Descuento en IMAX", 10.0, hoy + timedelta(days=7))
    promo6 = Promocion("CUMPLEAÑOS", "Descuento cumpleañero", 30.0, hoy + timedelta(days=1))
    promo7 = Promocion("VERACRUZ_CINE", "Promo local", 10.0, hoy + timedelta(days=15))
    promo8 = Promocion("GAMER_FEST", "Descuento en peliculas de juegos", 20.0, hoy + timedelta(days=12))
    promo9 = Promocion("FAMILIA", "Descuento grupos grandes", 15.0, hoy + timedelta(days=25))
    promo10 = Promocion("NOCTURNO", "Descuento después de las 10pm", 10.0, hoy + timedelta(days=8))

    promociones = [promo1, promo2, promo3, promo4, promo5, promo6, promo7, promo8, promo9, promo10]
    for pr in promociones:
        print(f"Código: {pr.codigo} | {pr.porcentajeDescuento}% de descuento")

    #Funciones
    print("\nREGISTRO DE FUNCIONES")# Se registran las funciones
    f1 = Funcion(101, pel1, sala1, "14:00 hrs", 80.0)
    f2 = Funcion(102, pel2, sala2, "16:00 hrs", 90.0)
    f3 = Funcion(103, pel3, sala3, "18:00 hrs", 120.0)
    f4 = Funcion(104, pel4, sala4, "20:00 hrs", 150.0)
    f5 = Funcion(105, pel5, sala5, "15:00 hrs", 80.0)
    f6 = Funcion(106, pel6, sala6, "17:30 hrs", 90.0)
    f7 = Funcion(107, pel7, sala7, "19:00 hrs", 120.0)
    f8 = Funcion(108, pel8, sala8, "21:30 hrs", 150.0)
    f9 = Funcion(109, pel9, sala9, "13:00 hrs", 80.0)
    f10 = Funcion(110, pel10, sala10, "22:00 hrs", 80.0)

    print(f1.detallesFun())
    print(f2.detallesFun())
    print(f3.detallesFun())
    print(f4.detallesFun())
    print(f5.detallesFun())
    print(f6.detallesFun())
    print(f7.detallesFun())
    print(f8.detallesFun())
    print(f9.detallesFun())
    print(f10.detallesFun())

    #Reservas
    print("\nREGISTRO DE RESERVAS")# Se registran las reservas
    reserva1 = Reserva(801, usuario1, f1, ["A1", "A2"]) #Se crean las reservas
    reserva2 = Reserva(802, usuario2, f2, ["B1", "B2", "B3"])
    reserva3 = Reserva(803, usuario3, f3, ["C5"])
    reserva4 = Reserva(804, usuario4, f4, ["D1", "D2"])
    reserva5 = Reserva(805, usuario5, f5, ["E10", "E11", "E12"])
    reserva6 = Reserva(806, usuario6, f6, ["F1"])
    reserva7 = Reserva(807, usuario7, f7, ["G4", "G5"])
    reserva8 = Reserva(808, usuario8, f8, ["H1", "H2", "H3", "H4"])
    reserva9 = Reserva(809, usuario9, f9, ["J8"])
    reserva10 = Reserva(810, usuario10, f10, ["K1", "K2"])

    reservas = [reserva1, reserva2, reserva3, reserva4, reserva5, reserva6, reserva7, reserva8, reserva9, reserva10]
    for r in reservas:
      #Se seleccionan asientos para reservar 
        r.seleccasientos()
        r.confirmarPago()
        print(f"Reserva #{r.idReserva} | Usuario: {r.usuario.nombre} | {len(r.asientos)} asientos en {r.funcion.pelicula.titulo}")

    print("\nVALIDACIÓN DE DATOS FINALIZADA")

    # Comprobamos que el codigo funcione para las espicificaciones del ejercicio
    print("INICIANDO PROCESO DE RESERVA")
    print(f"Usuario: {usuario1.nombre} (Puntos: {usuario1.puntosFidelidad})")
    print(f"Película: '{f10.pelicula.titulo}' | Sala: {f10.sala.nombre} ({f10.sala.tipo.value})")
    
    # Simulando el asiento ocupado
    f10.asientos_ocupados.append("A2")
    
    print("Seleccione sus asientos: A1, A2, B5")
    print("Verificando disponibilidad")
    
    reserva_intento = Reserva(994, usuario1, f10, ["A1", "A2", "B5"])
    exito, asiento_error = reserva_intento.seleccasientos()
    
    if not exito:
        print(f"El asiento {asiento_error} ya esta ocupado")
        print("Seleccione los asientos que quedan disponibles")
    
    print("Seleccione sus asientos: A1, A3, B5")
    reserva_final = Reserva(995, usuario1, f10, ["A1", "A3", "B5"])
    exito_final, _ = reserva_final.seleccasientos()
    
    if exito_final:
        print(f"Asientos A1, A3, B5 seleccionados correctamente")
        print(f"Monto base: ${reserva_final.montoTotal:.2f}")

    print("\n>>> APLICANDO GESTIÓN COMERCIAL")
    print(f"¿Cuenta con codigo de promocion?: SI")
    print(f"Codigo: {promo1.codigo}")
    
    if reserva_final.aplicarPromocion(promo1):
        print(f"[SISTEMA]: Validando codigo... ¡ÉXITO! (Descuento del {int(promo1.porcentajeDescuento)}% aplicado).")
    
    reserva_final.confirmarPago()
    
    print(f"\nResumen de Reserva #{reserva_final.idReserva}:")
    print(f"Usuario: {reserva_final.usuario.nombre}")
    print(f"Función: {reserva_final.funcion.pelicula.titulo.split(':')[0]} ({reserva_final.funcion.horarioInicio})")
    print(f"Asientos: [{', '.join(reserva_final.asientos)}]")
    ahorro = (reserva_final.funcion.precioBase * len(reserva_final.asientos)) - reserva_final.montoTotal
    print(f"Total: ${reserva_final.montoTotal:.2f} (Ahorraste ${ahorro:.2f})")
    print(f"Estado: {reserva_final.estado.name}. {reserva_final.generarTicket()}")

main()