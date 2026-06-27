# Diccionario básico
persona = {
        "nombre" : "Alex",
        "edad": 22,
        "lenguajes": ["c","java","python"],
    }

print(persona["nombre"])
print(persona["edad"])

persona["meta"]="libre"
print(persona)

persona["edad"]= 24
print(persona["edad"])

if "nombre" in persona:
    print("la clave existe")



lista_a =[1,2,3]
lista_b= lista_a
lista_b.append(4)

print ("lista_a:", lista_a)
print ("lista_b:", lista_b)

lista_c= lista_a.copy()
lista_c.append(99)
print ("lista_a:", lista_a)
print ("lista_c:", lista_c)


dict_a = {"x":1}
dict_b = dict_a
dict_b["x"]=999
print("dict_a:", dict_a)



with open("notas.txt", "w") as archivo:
    archivo.write("Aprendiendo python\n")
    archivo.write("Dia 2 completado\n")

with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print("linea:", linea.strip())

with open("notas.txt", "a") as archivo:
    archivo.write("agregando una linea mas\n")

