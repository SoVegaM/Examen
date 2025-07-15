productos = {
                '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                '2175HD': ['ACER', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                'JjfFHD': ['ASUS', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],                  
                'GF75HD': ['ASUS', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                '123FHD': ['ACER', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                '342FHD': ['ACER', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                'UWU131HD': ['DELL', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'] 
            }

stock = {
        '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
    }


#-------------------------------------------------------

def stock_marca():
    marca = input('Ingrese marca a consultar: ').upper()
    total_stock = 0
    encontrados = False

    for codigo, datos in productos.items():
        if datos[0].upper() == marca:
            encontrados = True
            if codigo in stock:
                print(f"- Modelo {codigo}, Stock: {stock[codigo][1]}")
                total_stock += stock[codigo][1]

    if encontrados:
        print(f"Stock total de productos {marca}: {total_stock}")
    else:
        print("No se encontraron productos de esa marca.")


#-------------------------------------------------------
def Busqueda_por_RAM():
    try:
        min_ram = int(input('Ingrese RAM mínima (en GB): '))
        max_ram = int(input('Ingrese RAM máxima (en GB): '))
        precio_max = int(input('Ingrese precio máximo: '))
    except ValueError:
        print("Debe ingresar valores enteros válidos.")
        return

    print("\nProductos encontrados:")
    encontrados = False
    for codigo, datos in productos.items():
        ram_str = datos[2].replace('GB', '')
        try:
            ram = int(ram_str)
        except:
            continue

        if codigo in stock and min_ram <= ram <= max_ram and stock[codigo][0] <= precio_max:
            encontrados = True
            print(f"- Modelo {codigo}, RAM: {ram}GB, Precio: ${stock[codigo][0]}, Stock: {stock[codigo][1]}")

    if not encontrados:
        print("No se encontraron productos que cumplan los criterios.")
            
        
#-------------------------------------------------------       


def eliminar_producto():
    while True:
        modelo = input('Ingrese modelo a eliminar: ').upper()
        if modelo in productos and modelo in stock:
            del productos[modelo]
            del stock[modelo]
            print(f'Producto {modelo} eliminado correctamente.')
        else:
            print('El modelo no existe.')

        continuar = input("¿Desea eliminar otro producto? (si/no): ").lower()
        if continuar != "si":
            break

#-------------------------------------------------------

def ver_todos_los_productos():
    print("\nListado de todos los productos disponibles:\n")
    for codigo, datos in productos.items():
        if codigo in stock:
            precio, unidades = stock[codigo]
            print(f"- Modelo: {codigo}")
            print(f"  Marca: {datos[0]}")
            print(f"  Pantalla: {datos[1]} pulgadas")
            print(f"  RAM: {datos[2]}")
            print(f"  Almacenamiento: {datos[3]} {datos[4]}")
            print(f"  Procesador: {datos[5]}")
            print(f"  Gráfica: {datos[6]}")
            print(f"  Precio: ${precio}")
            print(f"  Stock disponible: {unidades}")
            print("-" * 40)   

#-------------------------------------------------------
def agregar_producto():
    modelo = input("Ingrese el código del nuevo modelo: ").upper()

    if modelo in productos:
        print("Ese modelo ya existe.")
        return

    marca = input("Ingrese la marca: ").upper()
    pantalla = input("Tamaño de pantalla en pulgadas (ej: 15.6): ")
    ram = input("Cantidad de RAM (ej: 8GB): ").upper()
    tipo_alm = input("Tipo de almacenamiento (DD o SSD): ").upper()
    capacidad = input("Capacidad de almacenamiento (ej: 1T o 512GB): ").upper()
    procesador = input("Procesador (ej: Intel Core i5): ").title()
    grafica = input("Gráfica (ej: Nvidia GTX1050 o Integrada): ").title()

    try:
        precio = int(input("Precio del producto: "))
        stock_actual = int(input("Cantidad en stock: "))
    except ValueError:
        print("Precio y stock deben ser números enteros.")
        return

    productos[modelo] = [marca, float(pantalla), ram, tipo_alm, capacidad, procesador, grafica]
    stock[modelo] = [precio, stock_actual]

    print(f"Producto {modelo} agregado correctamente.")


#-------------------------------------

def modificar_stock():
    modelo = input("Ingrese el modelo del producto a modificar: ").upper()
    if modelo in stock:
        try:
            nuevo_stock = int(input(f"Ingrese nuevo stock para el modelo {modelo}: "))
            if nuevo_stock < 0:
                print("El stock no puede ser negativo.")
            else:
                stock[modelo][1] = nuevo_stock
                print(f"Stock del modelo {modelo} actualizado a {nuevo_stock} unidades.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    else:
        print("El modelo no existe en el sistema.")

# ==============================
 # MENÚ PRINCIPAL
 # =============================

def menu():
    while True:
        print("\n***MENÚ PRINCIPAL***")
        print("1. Stock Marca.")
        print("2. Busqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Ver todos los productos.")
        print("5. Agregar nuevo producto")
        print("6. producto a modificar")
        print("7. Salir.")
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
                    Busqueda_por_RAM()
        elif opcion == "3":
                    eliminar_producto()
        elif opcion == "4":
                    ver_todos_los_productos()
        elif opcion == "5":
                    agregar_producto()
        elif opcion == "5":
                    modificar_stock()            
        elif opcion == "7":
            print("Programa finalizado.")
            break
        
        else:
            print("Opción no válida.")
 #
menu()