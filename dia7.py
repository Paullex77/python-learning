import json
tareas = []

def agregar_tarea(titulo, prioridad, completada):
    for tarea in tareas:
        if tarea["titulo"].lower() == titulo.lower():
            print("La tarea ya existe")
            return
    nueva_tarea = {
        "titulo": titulo,
        "prioridad": prioridad,
        "estado": completada
    }
    tareas.append(nueva_tarea)
    print(f"Tarea '{titulo}' agregada")

def completar_tarea(titulo):
    for tarea in tareas:
        if tarea["titulo"].lower() == titulo.lower():
           tarea["estado"] = True
           print(f"Tarea '{titulo}' marcada como completada")
           return
    print("Tarea no encontrada")

def mostrar_tareas():
    for tarea in tareas:
        estado = "✅" if tarea["estado"] else "⏳"
        print(f"{estado} {tarea['titulo']} (Prioridad: {tarea['prioridad']})")

def contar_pendientes():
    pendientes = 0
    for tarea in tareas:
        if not tarea["estado"]: 
            pendientes += 1
    print(f"Total de tareas pendientes: {pendientes}")

def guardar_tareas():
    with open("tareas.json", "w")as archivo:
        json.dump(tareas, archivo, indent=4)
    print("Tareas guardadas")

def cargar_tareas():
    try:
        with open("tareas.json", "r")as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
tareas = cargar_tareas() 
if not tareas:
    agregar_tarea("Mate", "Urgente", False)
    agregar_tarea("Fisica", "Importante", False)
else:
    print(f"Cargadas tareas existentes")
print("ESTADO INICIAL:")
print(tareas)
mostrar_tareas()
contar_pendientes()
print("DESPUÉS DE COMPLETAR 'MATE':")
completar_tarea("Mate")
mostrar_tareas()
contar_pendientes()
print("DATOS FINALES:")
guardar_tareas()
print(tareas)

