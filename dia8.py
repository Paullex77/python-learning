
import sqlite3

conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    prioridad TEXT,
    completada INTEGER DEFAULT 0
)
""")
def agregar_tarea(titulo, prioridad):
    try:
        cursor.execute("INSERT INTO tareas (titulo, prioridad, completada) VALUES (?, ?, ?)",
                       (titulo, prioridad, 0))
        conexion.commit()
        print(f"Tarea '{titulo}' agregada")
    except sqlite3.IntegrityError:
        print(f"La tarea '{titulo}' ya existe")

def completar_tarea(titulo):
    cursor.execute("UPDATE tareas SET completada = 1 WHERE titulo = ?", (titulo,))
    conexion.commit()
    if cursor.rowcount > 0:
        print(f"Tarea '{titulo}' marcada como completada")
    else:
        print(f"No se encontró la tarea '{titulo}'")

def eliminar_tarea(titulo):
    cursor.execute("DELETE FROM tareas WHERE titulo = ?", (titulo,))
    conexion.commit()
    if cursor.rowcount > 0:
        print(f"Tarea '{titulo}' eliminada")
    else:
        print(f"No se encontró la tarea '{titulo}'")


agregar_tarea("Mate", "Urgente")
agregar_tarea("Quimica", "Media")
completar_tarea("Mate")
eliminar_tarea("Fisica")

cursor.execute("SELECT * FROM tareas")
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conexion.close()
#cursor.execute("DELETE FROM tareas")
#conexion.commit()
#print("Tabla limpiada")
#conexion.close()
