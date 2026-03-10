
"""
nombre1 = input("Ingres su nombre: ")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

suma = num1 + num2
Resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
divEntera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"Hola {nombre1} la suma de los numeros es: {suma}")
print(f"la resta de los numeros es: {Resta}")
print(f"la multiplicacion de los numeros es: {multiplicacion}")
print(f"la division de los numeros es: {division}")
print(f"la division entera de los numeros es: {divEntera}")
print(f"el modulo de los numeros es: {modulo}")
print(f"la potencia de los numeros es: {potencia}")

# area del circulo

PI = 3.1416
radio = float(input("Ingrese el radio del circulo: "))
areaCir = PI*(radio**2)

print("el area del circulo es: ", f"{areaCir:.2f2}")

# area del triangulo

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

areaT = (base * altura)/2

print("el area del triangulo es: ", f"{areaT:.2f}")

# valor a pagar a un empleado por tarbajar la semana

horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
valorHora = int(input("Ingrese valor de hora: "))

sueldo = (horasTrabajadas * valorHora)

print("el valor a pagar por la semana de trabajo es: ", f"{sueldo:.0f}")
"""
horasTrabajadas1 = float(input("Ingrese las horas trabajadas empleado1: "))
valorHora1 = int(input("Ingrese valor de hora: "))

sueldo1 = (horasTrabajadas1 * valorHora1)

horasTrabajadas2 =float(input("Ingrese las horas trabajadas empleado2: "))
valorHora2 = int(input("Ingrese valor de hora: "))

sueldo2 = (horasTrabajadas2 * valorHora2)

horasTrabajadas3 = float(input("Ingrese las horas trabajadas empleado3: "))
valorHora3 = int(input("Ingrese valor de hora: "))

sueldo3 = (horasTrabajadas3 * valorHora3)

sueldoTotal = sueldo1 + sueldo2 + sueldo3

print("el valor a pagar por todos los empleado es: ", f"{sueldoTotal:.0f}")


