# ============================================================
#  POO en Python - Figuras Geométricas
#  Clase derivada: Rectangulo (hereda de FiguraGeometrica)
# ============================================================

from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo. Recibe ancho y alto."""

    def __init__(self, ancho: float, alto: float):
        super().__init__(ancho=ancho, alto=alto)

    # ── Métodos sobreescritos ────────────────────────────────
    def area(self) -> float:
        """Área del rectángulo: ancho * alto"""
        return self._ancho * self._alto

    def perimetro(self) -> float:
        """Perímetro del rectángulo: 2 * (ancho + alto)"""
        return 2 * (self._ancho + self._alto)

    def __str__(self) -> str:
        return (
            f"Rectángulo     | Ancho: {self._ancho} | Alto: {self._alto} | "
            f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"
        )
