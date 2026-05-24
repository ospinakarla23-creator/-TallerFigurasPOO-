# ============================================================
#  POO en Python - Figuras Geométricas
#  Clase derivada: Circunferencia (hereda de FiguraGeometrica)
# ============================================================

import math
from figura_geometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica):
    """Clase que representa una circunferencia. Recibe solo el radio,
    que es asignado al ancho."""

    def __init__(self, radio: float):
        # radio se asigna a ancho (y alto queda igual por requisito del taller)
        super().__init__(ancho=radio, alto=radio)

    # ── Métodos sobreescritos ────────────────────────────────
    def area(self) -> float:
        """Área de la circunferencia: π * radio²"""
        return math.pi * (self._ancho ** 2)

    def perimetro(self) -> float:
        """Perímetro (circunferencia): 2 * π * radio"""
        return 2 * math.pi * self._ancho

    def __str__(self) -> str:
        return (
            f"Circunferencia | Radio: {self._ancho} | "
            f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"
        )
