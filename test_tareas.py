"""Pruebas para tareas.py (pytest).

Estado inicial: FALLAN porque listar() y completar() están sin implementar.
Objetivo: deben PASAR cuando OpenCode complete los TODO de tareas.py.

Ejecutar:  python -m pytest -v        (dentro de ~/mlx-demo, con mlx-env activado)
"""
import pytest
import tareas


@pytest.fixture(autouse=True)
def limpiar_tareas():
    """Deja la lista global vacía antes y después de cada prueba."""
    tareas.TAREAS.clear()
    yield
    tareas.TAREAS.clear()


def test_agregar_anade_tarea():
    tareas.agregar("Comprar pan")
    assert len(tareas.TAREAS) == 1
    assert tareas.TAREAS[0]["texto"] == "Comprar pan"
    assert tareas.TAREAS[0]["hecha"] is False


def test_listar_muestra_el_texto_y_numeracion(capsys):
    tareas.agregar("Comprar pan")
    tareas.agregar("Leer un libro")
    capsys.readouterr()  # descartar la salida de agregar()
    tareas.listar()
    out = capsys.readouterr().out
    assert "Comprar pan" in out
    assert "Leer un libro" in out
    # numeración 1-based
    assert "1" in out and "2" in out


def test_completar_marca_como_hecha():
    tareas.agregar("Comprar pan")
    tareas.completar(1)
    assert tareas.TAREAS[0]["hecha"] is True


def test_listar_marca_las_completadas(capsys):
    tareas.agregar("Comprar pan")
    tareas.completar(1)
    capsys.readouterr()
    tareas.listar()
    out = capsys.readouterr().out
    assert "[x]" in out  # las hechas se muestran con [x]


def test_completar_indice_invalido_no_marca_nada():
    """Un índice fuera de rango no debe marcar la tarea válida (ni romper el test)."""
    tareas.agregar("Comprar pan")
    try:
        tareas.completar(5)  # fuera de rango
    except Exception:
        pass  # aceptamos que valide lanzando o imprimiendo error
    assert tareas.TAREAS[0]["hecha"] is False
