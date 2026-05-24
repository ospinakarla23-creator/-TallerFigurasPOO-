# ============================================================
#  POO en Python - Figuras Geométricas
#  Programa principal
# ============================================================

from figura_geometrica import FiguraGeometrica
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia


def separador():
    print("─" * 60)


if __name__ == "__main__":

    separador()
    print("  TALLER: Figuras Geométricas con POO")
    separador()

    # ── Cuadrado ─────────────────────────────────────────────
    print("\n▶ Cuadrado (lado = 5)")
    cuadrado = Cuadrado(5)
    print(cuadrado)

    # ── Rectángulo ───────────────────────────────────────────
    print("\n▶ Rectángulo (ancho = 8, alto = 4)")
    rectangulo = Rectangulo(8, 4)
    print(rectangulo)

    # ── Circunferencia ───────────────────────────────────────
    print("\n▶ Circunferencia (radio = 7)")
    circunferencia = Circunferencia(7)
    print(circunferencia)

    # ── Verificar herencia ───────────────────────────────────
    separador()
    print("\n▶ Verificación de herencia con isinstance():")
    for figura in [cuadrado, rectangulo, circunferencia]:
        print(f"   {type(figura).__name__:15} es FiguraGeometrica: "
              f"{isinstance(figura, FiguraGeometrica)}")

    # ── Validación de errores ────────────────────────────────
    separador()
    print("\n▶ Validación: valor inválido (lado = -3)")
    try:
        mal = Cuadrado(-3)
    except ValueError as e:
        print(f"   ValueError capturado → {e}")

    print("\n▶ Validación: valor inválido (ancho = 0)")
    try:
        mal = Rectangulo(0, 5)
    except ValueError as e:
        print(f"   ValueError capturado → {e}")

    separador()
