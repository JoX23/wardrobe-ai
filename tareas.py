#!/usr/bin/env python3
"""CLI mínima de tareas (to-do). Algunas funciones están sin implementar (TODO)."""
import sys

# Lista de tareas en memoria. Cada tarea: {"texto": str, "hecha": bool}
TAREAS = []


def agregar(texto):
    """Agrega una tarea nueva a la lista."""
    TAREAS.append({"texto": texto, "hecha": False})
    print(f"Agregada: {texto}")


def listar():
    """Muestra todas las tareas numeradas, marcando las completadas."""
    if not TAREAS:
        print("(sin tareas)")
        return
    for i, tarea in enumerate(TAREAS, start=1):
        marca = "[x]" if tarea["hecha"] else "[ ]"
        print(f"{i}. {marca} {tarea['texto']}")


def completar(indice):
    """Marca como hecha la tarea con el número dado (empezando en 1)."""
    if not 1 <= indice <= len(TAREAS):
        print(f"índice inválido: {indice}")
        return
    TAREAS[indice - 1]["hecha"] = True
    print(f"Completada: {TAREAS[indice - 1]['texto']}")


def main(argv):
    if not argv:
        print("uso: tareas.py [agregar <texto> | listar | completar <id>]")
        return
    comando, *resto = argv
    if comando == "agregar":
        agregar(" ".join(resto))
    elif comando == "listar":
        listar()
    elif comando == "completar":
        completar(int(resto[0]))
    else:
        print(f"comando desconocido: {comando}")


if __name__ == "__main__":
    main(sys.argv[1:])
