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
    # TODO: imprimir cada tarea con su número (empezando en 1) y [x] si está hecha
    raise NotImplementedError


def completar(indice):
    """Marca como hecha la tarea con el número dado (empezando en 1)."""
    # TODO: validar el índice y marcar la tarea como hecha
    raise NotImplementedError


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
