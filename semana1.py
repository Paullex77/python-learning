# Mi primer programa en Python
nombre = "Paul"
edad = 24
lenguajes = ["C", "Java", "Python"]
print(f"Hola, soy {nombre}")
print(f"Tengo {edad} años")
print(f"Sé: {lenguajes}")
print(f"Favorito: {lenguajes[-1]}")

anio_actual = 2026
anio_nacimiento = anio_actual - edad
print(f"naci en el año {anio_nacimiento}")
lenguajes.append("Csharp")
print(f"Ahora se: {lenguajes}")
print(f"Ahora se : {len(lenguajes)}")


if edad >= 18:
    print("soy mayor de edad")
elif edad >= 13:
    print("soy un adolescente")
else:
    print("soy un niño")

for lenguaje in lenguajes:
    print(f"Se programar en {lenguaje}")

for i in range(5):
        print(f"Numero {i}")


def saludar(nombre, lenguaje):
     print(f"Hola {nombre}, bienvenido al mundo de {lenguaje}")

def calcular_edad(anio_nacimiento):
     return 2026 - anio_nacimiento

def lenguaje_favorito(lenguajes):
     return lenguajes [-2]
saludar("Paul", "Python")
edad_calculada = calcular_edad(2002)
print(f"tengo {edad_calculada} años")
lenguaje_fav = lenguaje_favorito(lenguajes)
print(f"Mi lenguaje favorito es {lenguaje_fav}")
