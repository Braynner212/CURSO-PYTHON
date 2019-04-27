import math
# Comentario de linea
"""
Comentario
de párrafo
"""

# Hola mundo
print("Hola mundo")

# Variables

x = 4  # Int
y = "Texto"  # String
z = 4.5  # float
a = True  # Boolean
b = False  # Boolean
c = 4+5j  # Complejo

print(x, y, z, a, b, c)

# Conocer el tipo de datos de una variable
print(type(b))

# Conversiones de tipos de datos

# Enteros
x = int(2)
print(x)

x = int(2.8)
print(x)

x = int("2")
print(x)

# Float
x = float(2)
print(x)

x = float(2.8)
print(x)

x = float("2")
print(x)

x = float("2.5")
print(x)

# String
x = str(2)
print(x)

x = str(2.8)
print(x)

x = str("2")
print(x)

# Manejo de cadenas de texto y algunos métodos

cad = "Hello world"
print(cad[0])
print(cad[0:5])  # No toma la última posición

cad = "     Hello world    "
cad = cad.strip()  # Quita los espacios a el inicio y al final
print(cad)
print(len(cad))
print(cad.lower())
print(cad.upper())
print(cad.replace('l', 'y'))
print(cad.split(' '))

# Operaciones

# Operaciones aritméticas
a = 2
b = 3
c = a + b
c = a - b
c = a * b
c = a / b  # Cociente
c = a % b
c = a ** b
c = math.sqrt(a)
c = math.pi

# Captura por consola
print("Digite el nombre")
nombre = input()
print("Hola "+nombre+"!")


print("Ingrese primer número")
n1 = input()
print("Ingrese segundo número")
n2 = input()
print(float(n1)+float(n2))

# Condiciones
a = 1
b = 3
if a > b:
    print(a, "Es mayor que ", b)
else:
    print(a, "Es menor que ", b)

if b == a:
    print("Son iguales")
elif a > b:
    print(a, "Es mayor que ", b)
else:
    print(b, "Es mayor que ", a)

if a == b and a > 1:
    print(" ")








