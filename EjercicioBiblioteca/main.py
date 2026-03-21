from models import *

def main():
    print("SISTEMA DE BIBLIOTECA DIGITAL\n")

    print("Registro de libros:")
    lib1 = Libro(354, "El principio del placer", 1972, "Jose Emilio Pacheco", "978-968", "Ficcion")
    lib2 = Libro(895, "Algebra Lineal", 2012, "Stanley Grossman", "978-970", "Matematicas")
    lib3 = Libro(442, "Calculo Integral y Diferencial", 2014, "James Stewart", "978-607", "Matematicas")
    lib4 = Libro(256, "Python Object-Oriented Programming", 2021, "Steven F. Lott", "978-180", "Programacion")
    lib5 = Libro(189, "Data Science for Business", 2013, "Foster Provost", "978-144", "Ciencia de Datos")
    lib6 = Libro(996, "La maquina del tiempo", 1895, "H.G. Wells", "978-842", "Ciencia Ficcion")
    lib7 = Libro(475, "Estructuras de Datos", 2013, "Luis Joyanes", "978-844", "Programacion")
    lib8 = Libro(331, "Estadistica Practica", 2020, "Peter Bruce", "978-149", "Ciencia de Datos")
    lib9 = Libro(551, "El fin de la eternidad", 1955, "Isaac Asimov", "978-849", "Ciencia Ficcion")
    lib10 = Libro(547, "Patrones de Diseño", 1994, "Erich Gamma", "978-020", "Programacion")

    libros = [lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10]
    for x in libros: print(x.mostrar_detalle())

    print("\nRegistro de revistas:")
    rev1 = Revista(564, "Bass Player Magazine", 2023, 450, "Mensual")
    rev2 = Revista(606, "PC Gamer", 2024, 380, "Mensual")
    rev3 = Revista(787, "Science", 2023, 6650, "Semanal")
    rev4 = Revista(594, "Nature", 2023, 7900, "Semanal")
    rev5 = Revista(5430, "Metal Hammer", 2024, 350, "Mensual")
    rev6 = Revista(114, "National Geographic", 2023, 900, "Mensual")
    rev7 = Revista(404, "Wired", 2024, 320, "Mensual")
    rev8 = Revista(516, "Linux Format", 2024, 280, "Quincenal")
    rev9 = Revista(999, "Guitar World", 2023, 410, "Mensual")
    rev10 = Revista(145, "Edge", 2024, 390, "Mensual")
    
    revistas = [rev1, rev2, rev3, rev4, rev5, rev6, rev7, rev8, rev9, rev10]
    for i in revistas: print(i.mostrar_detalle())

    print("\nregitro de material digital:")
    md1 = MaterialDigital(12, "Assassin's Creed Unity Artbook", 2014, "PDF", "url.com/acu", 150.5)
    md2 = MaterialDigital(78, "GTA V Manual Oficial", 2013, "PDF", "url.com/gtav", 45.0)
    md3 = MaterialDigital(35, "Titanfall 2 Lore Guide", 2016, "EPUB", "url.com/tf2", 12.0)
    md4 = MaterialDigital(66, "Resident Evil Requiem Walkthrough", 2025, "PDF", "url.com/rer", 25.4)
    md5 = MaterialDigital(78, "Matplotlib & Tkinter Cheat Sheet", 2023, "PDF", "url.com/py", 5.2)
    md6 = MaterialDigital(11, "Davies-Bouldin Index Explained", 2022, "PDF", "url.com/db", 2.1)
    md7 = MaterialDigital(93, "Rock & Metal Bass Tabs Collection", 2021, "ZIP", "url.com/tabs", 80.0)
    md8 = MaterialDigital(34, "P-value and P-hacking Guide", 2020, "PDF", "url.com/phack", 3.5)
    md9 = MaterialDigital(47, "Windows User Manual", 2023, "PDF", "url.com/wi", 15.0)
    md10 = MaterialDigital(75, "Clean Code Digital Edition", 2008, "EPUB", "url.com/cc", 8.8)
    
    digitales = [md1, md2, md3, md4, md5, md6, md7, md8, md9, md10]
    for md in digitales: print(md.mostrar_detalle())

    print("\nRegistro de usuarios:")
    usu1 = Usuario(187, "Federico", 5)
    usu2 = Usuario(452, "Carlos", 3)
    usu3 = Usuario(320, "Lupita", 4)
    usu4 = Usuario(884, "Gio", 5)
    usu5 = Usuario(666, "Oscar", 2)
    usu6 = Usuario(721, "Lans", 3)
    usu7 = Usuario(953, "Dana", 5)
    usu8 = Usuario(324, "Sela", 4)
    usu9 = Usuario(807, "Renata", 3)
    usu10 = Usuario(656, "Edgar", 5)
    
    usuarios = [usu1, usu2, usu3, usu4, usu5, usu6, usu7, usu8, usu9, usu10]
    for u in usuarios: print(u.mostrar_detalle())

    biblio1 = Bibliotecario(434, "Admin_eduardo")
    biblio2 = Bibliotecario(222, "Admin_marco")
    biblio3 = Bibliotecario(108, "Admin_Pedro")
    biblio4 = Bibliotecario(777, "Admin_Carmen")
    biblio5 = Bibliotecario(612, "Admin_Raul")
    biblio6 = Bibliotecario(230, "Admin_lans")
    biblio7 = Bibliotecario(758, "Admin_Sela")
    biblio8 = Bibliotecario(119, "Admin_Marta")
    biblio9 = Bibliotecario(791, "Admin_Oscar")
    biblio10 = Bibliotecario(241, "Admin_Diana")

    bibliotecarios = [biblio1, biblio2, biblio3, biblio4, biblio5, biblio6, biblio7, biblio8, biblio9, biblio10]
    for b in bibliotecarios: print(F"Bibliotecario: {b.nombre} (ID: {b.idPersona})")

    suc1 = Sucursal(112, "Biblioteca Central BUAP")
    suc2 = Sucursal(531, "Sede Veracruz Centro")
    suc3 = Sucursal(885, "Sede Xalapa")
    suc4 = Sucursal(939, "Sede Boca del Rio")
    suc5 = Sucursal(616, "Biblioteca de Ciencias")
    suc6 = Sucursal(200, "Sede Ingenieria")
    suc7 = Sucursal(713, "Sede Humanidades")
    suc8 = Sucursal(949, "Biblioteca de Artes")
    suc9 = Sucursal(323, "Sede Medicina")
    suc10 = Sucursal(686, "Sede Virtual")

    sucursales = [suc1, suc2, suc3, suc4, suc5, suc6, suc7, suc8, suc9, suc10]
    for s in sucursales: print(f"Sucursal: {s.nombre}")

    #agregar libros a sucursales
    suc1.agregar_material(lib1)
    suc1.agregar_material(lib2)
    suc2.agregar_material(lib3)
    suc2.agregar_material(lib4)

    #metodo buscar por autor
    catalogo = Catalogo()
    print("\nBuscar libros de 'Jose Emilio Pacheco':")
    resultados_autor = catalogo.buscarPorAutor("Jose Emilio Pacheco", libros)
    for j in resultados_autor: print(f"Encontrado: {j.titulo}")

    #buscar em sucursal
    todas_sucursales = [suc1, suc2, suc3, suc4, suc5, suc6, suc7, suc8, suc9, suc10]
    print("\nBuscar 'Algebra' en todas las sucursales:")
    resultados_globales = catalogo.buscarEnTodasSucursales("Algebra", todas_sucursales)
    for c, mat in resultados_globales:
        print(f"Encontrado en {c}: {mat.titulo}")

    #gestion de prestamo
    print(f"\nBibliotecario {biblio1.nombre} prestando '{lib1.titulo}' a {usu1.nombre}")
    prestamo_exitoso = biblio1.gestionarPrestamo(usu1, lib1)
    if prestamo_exitoso:
        print(f"Prestamo registrado. {lib1.mostrar_detalle()}")
        print(f"{usu1.mostrar_detalle()}")
    
    #transferencia de material
    print(f"\nTransfiriendo '{lib2.titulo}' de {suc1.nombre} a {suc2.nombre}")
    transferencia = biblio1.transferirMaterial(lib2, suc1, suc2)
    if transferencia:
        print(f"Transferencia exitosa. Ahora {suc2.nombre} tiene {len(suc2.catalogoLocal)} materiales")

    #penalizacion
    print("\nAplicando penalizacion")
    penalizacion = Penalizacion(0.0, "Retraso en entrega de 'Algebra Lineal'")
    multa = penalizacion.calcularMulta(4) # 4 días de retraso
    print(f"Calculando multa por 4 dias de retraso. \nTotal: ${multa}")
    
    print(f"Procediendo a bloquear usuario {usu6.nombre}")
    mensaje_bloqueo = penalizacion.bloquearUsuario(usu6)
    print(f"{mensaje_bloqueo} (Nuevo límite de prestamos: {usu6.limitePrestamos})")

main()