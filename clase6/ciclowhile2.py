menu = """
Restaurante el Buen Sabor
    1. Hamburguesa - $20.000
    2. Pizza - $15.000
    3. Ensalada - $4.500
    4. Salchipapa - $8.000
    5. Perro Caliente - $12.000
    6. Salir
"""

opcion = 0
total = 0
totalHamburguesa = 0
cuentaHamburguesa = 0
totalPizza = 0
cuentaPizza = 0
totalEnsalada = 0
cuentaEnsalada = 0
totalSalchipapa = 0
cuentaSalchipapa = 0
totalPerro = 0
cuentaPerro = 0
while opcion !=6:
    print(menu)
    opcion = int(input("Ingrese una opción del menú: "))
    if opcion == 1:
        print("Has elegido Hamburguesa - $20.000")
        total += 20000
        totalHamburguesa += 20000
        cuentaHamburguesa += 1
    elif opcion == 2:
        print("Has elegido Pizza - $15.000")
        total += 15000
        totalPizza += 15000
        cuentaPizza += 1
    elif opcion == 3:
        print("Has elegido Ensalada - $4.500")
        total += 4500
        totalEnsalada += 4500
        cuentaEnsalada += 1
    elif opcion == 4:
        print("Has elegido Salchipapa - $8.000")
        total += 8000
        totalSalchipapa += 8000
        cuentaSalchipapa += 1
    elif opcion == 5:
        print("Has elegido Perro Caliente - $12.000")
        total += 12000
        totalPerro += 12000
        cuentaPerro += 1
    elif opcion == 6:
        print("El Total del pedido es: ",total)
        print("Detallado de la siguiente manera:")
        print("     Fueron ", cuentaHamburguesa ," Hamburguesas para un Total de: ",totalHamburguesa)
        print("     Fueron ", cuentaPizza ," Pizzas para un Total de: ",totalPizza)
        print("     Fueron ", cuentaEnsalada ," Ensaladas para un Total de: ",totalEnsalada)
        print("     Fueron ", cuentaSalchipapa ," Salchipapas para un Total de: ",totalSalchipapa)
        print("     Fueron ", cuentaPerro ," Perros Calientes para un Total de: ",totalPerro)
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")

