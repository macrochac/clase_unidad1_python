"""
dia = int(input("Ingrese un numero del 1 al 7: "))


if dia==1:
    print("Lunes")
elif dia==2:
    print("Martes")
elif dia==3:
    print("Miercoles")
elif dia==4:
    print("Jueves")
elif dia==5:
    print("Viernes")
elif dia==6:
    print("Sabado")
elif dia==7:
    print("Domingo")
else:
    print("Numero no valido")



match dia:
    case 1:
        print("lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero no valido")


animal = input("ingrese un animal (perro - gato - pez): ")
match animal:
    case "perro":
        print("guau")
    case "gato":
        print("miau")
    case "pez":
        print("blub")
    case _:
        print("Animal no reconocido")
"""
tabla = int(input("Que tabla de multiplicar quiere, Escriba el numero deseado: "))
i = 1
while i <= 10:
    print(f"{tabla} x {i} = {i * tabla}")
    i += 1
