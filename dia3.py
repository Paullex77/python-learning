
contactos = []

def agregar_contacto(nombre, telefono, email):
    contacto = {
        "nombre": nombre,
        "telefono" : telefono,
        "email" : email 
    }
    contactos.append(contacto)
    print(f"contacto {nombre} agregado")

agregar_contacto("Ana", "0981097056","ana@gmail.com")
agregar_contacto("Luis", "0981097057","luis@gmail.com")

print(contactos)



def buscar_contacto (nombre):
    for contacto in contactos:
        if contacto ["nombre"].lower()== nombre.lower():
            return contacto
    return None

resultado = buscar_contacto("ana")
if resultado:
    print(f"Encontrado: {resultado['telefono']}")
else:
    print("No se encontro el contacto")


import json
def guardar_contactos():
    with open("agenda.json", "w")as archivo:
        json.dump(contactos, archivo, indent=4)
    print("Agenda guardada")

def cargar_contactos():
    try:
        with open("agenda.json", "r")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
guardar_contactos()

contactos = cargar_contactos()
print (contactos)
