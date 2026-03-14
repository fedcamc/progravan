from models import *

def main():

    #Clientes
    print("\n Lista de clientes")
    
    clientes = [
        Cliente(110, "Federico Camacho", "fedcamc@gmail.com", 100),
        Cliente(111, "Fatima Camacho", "fatfecamc@gmail.com", 50),
        Cliente(112, "Vilma Camacho", "vilmacamacho07@gmail.com", 200),
        Cliente(113, "Edgardo Flores", "edflors@gmail.com", 10),
        Cliente(114, "Oscar Carmona", "el_rey_del_free@gmail.com", 80),
        Cliente(115, "Giovanni Chillopa", "noob_master69@gmail.com", 30),
        Cliente(116, "Dana Dominguez", "dandom07@gmail.com", 150),
        Cliente(117, "Sela Torres", "nosoy_sela@gmail.com", 90),
        Cliente(118, "Renata Hernandez", "renhmtz@gmail.com", 0),
        Cliente(119, "Carlos Cortez", "az.cortz@gmail.com", 300)
    ]
    for c in clientes:
           print(c.mostrar_detalle())

    # Empleados
    print("\n Lista de empleados")
    empleados = [
        Empleado(301, "Claudia Cagal", "claudiacag29@cafe.com", "Emp1", Rol.GERENTE),
        Empleado(302, "Eduardo Paredes", "edupad2008@cafe.com", "Emp2", Rol.BARISTA),
        Empleado(303, "Mariana Calderon ", "caldemarian@cafe.com", "Emp3", Rol.MESERO),
        Empleado(304, "Leandro Antele", "antleoxx@cafe.com", "Emp4", Rol.BARISTA),
        Empleado(305, "Vania Maya", "vanmaya07@cafe.com", "Emp5", Rol.MESERO),
        Empleado(306, "Axel Azamar", "soyaxlazam@cafe.com", "Emp6", Rol.BARISTA),
        Empleado(307, "Carolina Diaz", "CCDiaz@cafe.com", "Emp7", Rol.MESERO),
        Empleado(308, "Emir Vazquez", "sixseven@cafe.com", "Emp8", Rol.MESERO),
        Empleado(309, "Natalia Pretelin", "natipop10@cafe.com", "Emp9", Rol.BARISTA),
        Empleado(310, "Ariana Bonilla", "dumbAri_454@cafe.com", "Emp10", Rol.MESERO)
    ]
    for e in empleados:
        print(e.mostrar_detalle())

    #Bebidas
    print("\n Lista de bebidas")
    bebidas = [
        Bebida(801, "Americano", 37.0, "Mediano", Temperatura.CALIENTE),
        Bebida(802, "Latte", 40.50, "Grande", Temperatura.CALIENTE),
        Bebida(803, "Frappe de moka", 59.0, "Grande", Temperatura.FRIA),
        Bebida(804, "Espresso", 34.60, "Chico", Temperatura.CALIENTE),
        Bebida(805, "Te verde", 36.0, "Mediano", Temperatura.CALIENTE),
        Bebida(806, "Cold Brew", 52.0, "Mediano", Temperatura.FRIA),
        Bebida(807, "Capuchino", 56.50, "Mediano", Temperatura.CALIENTE),
        Bebida(808, "Limonada", 38.40, "Grande", Temperatura.FRIA),
        Bebida(809, "Macchiato", 41.0, "Chico", Temperatura.CALIENTE),
        Bebida(810, "Te helado", 43.0, "Grande", Temperatura.FRIA)
    ]
    for b in bebidas:
        print(b.mostrar_detalle())

    #Postres
    print("\n Lista de postres")
    postres = [
        Postre(511, "Cheesecake", 64.0, False, False),
        Postre(512, "Brownie", 42.0, False, False),
        Postre(513, "Galleta de Avena", 20.50, True, False),
        Postre(514, "Pastel de Zanahoria", 58.0, False, True),
        Postre(515, "Muffin de Mora", 33.0, False, False),
        Postre(516, "Pay de Fruta", 59.0, True, True),
        Postre(517, "Volcan de Chocolate", 73.0, False, False),
        Postre(518, "Croissant", 34.0, False, False),
        Postre(519, "Dona vegana", 35.0, True, False),
        Postre(520, "Flan", 40.0, False, True)
    ]
    for p in postres:
        print(p.mostrar_detalle())

    #Inventario
    print("\n Lista del Inventario")
    inventarios = [Inventario(i) for i in range(1, 11)]
    for inv in inventarios:
        print(inv.mostrar_detalle())

    #Pedidos
    print("\n Lista de pedidos")
    pedidos = [
        Pedido(930, [bebidas[0], postres[1]]),
        Pedido(931, [bebidas[2]]),
        Pedido(932, [bebidas[1], bebidas[1], postres[0]]),
        Pedido(933, [bebidas[3], postres[3]]),
        Pedido(934, [postres[4], postres[5]]),
        Pedido(935, [bebidas[5], bebidas[6], postres[2]]),
        Pedido(936, [bebidas[7]]),
        Pedido(937, [bebidas[8], postres[6]]),
        Pedido(938, [bebidas[9], postres[7], postres[8]]),
        Pedido(939, [bebidas[4], postres[9]])
    ]
    for ped in pedidos:
        print(ped.mostrar_detalle())

    #Ejem de cliente
    cliente_prueba = clientes[0] 
    print("Cliente")
    print(cliente_prueba.login())
    print(cliente_prueba.realizar_pedido(pedidos[0]))
    print(cliente_prueba.consultar_historial())
    print(cliente_prueba.canjear_puntos(50))

    #Ejem de bebida
    bebida_prueba = bebidas[2]  
    print("\nBebida ")
    print(bebida_prueba.agregar_extra("Leche de almendra"))
    print(bebida_prueba.agregar_extra("Crema batida extra"))
    print(f"Nuevo precio de {bebida_prueba.nombre}: ${bebida_prueba.calcular_precio_final()}")

    #Ejem de inventario
    empleado_prueba = empleados[0]
    inventario_prueba = inventarios[0]
    print("\nInventario")
    print(empleado_prueba.actualizar_inventario(inventario_prueba, "Cafe en grano", 50))
    print(empleado_prueba.actualizar_inventario(inventario_prueba, "Leche Entera", 20))
    
    print(inventario_prueba.reducir_stock("Cafe en grano", 10))
    print(inventario_prueba.reducir_stock("Sirope de vainilla", 5))

    #Ejem de pedido
    print("\nEstado de Pedido")
    pedido_prueba = pedidos[0]
    print(f"Estado inicial: {pedido_prueba.estado.name}")
    print(empleado_prueba.cambiar_estado_pedido(pedido_prueba, EstadoPedido.PREPARANDO))
    print(empleado_prueba.cambiar_estado_pedido(pedido_prueba, EstadoPedido.ENTREGADO))
    
main()