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
 #.................................

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
            
        
#         


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
    
# ==============================
 # MENÚ PRINCIPAL
 # =============================

def menu():
    while True:
        print("\n***MENÚ PRINCIPAL***")
        print("1. Stock Marca.")
        print("2. Busqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
                    Busqueda_por_RAM()
        elif opcion == "3":
                    eliminar_producto()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")
 #
menu()