"""
sum = 0
for x in range(3):
 sum += x
print(sum)

for x in range(1,11):
    print(x)

for x in range(1, 11, 2):
   print(x)


texto="Python"
for letra in texto:
   print(letra)
"""

Num = int(input("Cual Tabla de Multiplicar Quiere: "))
for x in range(1,11):
    Mul = Num * x
    print(Num ," x ",x," = ",Mul)