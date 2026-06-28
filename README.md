# mlx-demo — proyecto de prueba para OpenCode

Pequeña CLI de tareas (to-do) en Python para probar OpenCode con el modelo
local Qwen2.5-Coder (servidor MLX en `http://localhost:8080/v1`).

## Estado

`tareas.py` tiene la estructura básica pero **faltan funciones por implementar**
(marcadas con `TODO`). La idea es pedirle a OpenCode que las complete.

## Ideas para pedirle a OpenCode

- "Implementa las funciones marcadas con TODO en `tareas.py`."
- "Agrega un comando `completar <id>` que marque una tarea como hecha."
- "Escribe pruebas con pytest para `tareas.py` en `test_tareas.py`."
- "Añade persistencia: guarda y carga las tareas desde `tareas.json`."

## Uso (cuando esté completo)

```bash
python tareas.py agregar "Comprar pan"
python tareas.py listar
python tareas.py completar 1
```
