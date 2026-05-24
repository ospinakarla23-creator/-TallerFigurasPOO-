# ============================================================
#  POO en Python - Figuras Geométricas
#  Clase derivada: Cuadrado (hereda de FiguraGeometrica)
# ============================================================

from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    """Clase que representa un cuadrado. Recibe un solo valor: lado."""

    def __init__(self, lado: float):
        # lado se asigna a ancho y alto (ambos iguales)
        super().__init__(ancho=lado, alto=lado)

    # ── Métodos sobreescritos ────────────────────────────────
    def area(self) -> float:
        """Área del cuadrado: lado²"""
        return self._ancho ** 2

    def perimetro(self) -> float:
        """Perímetro del cuadrado: 4 * lado"""
        return 4 * self._ancho

    def __str__(self) -> str:
        return (
            f"Cuadrado       | Lado: {self._ancho} | "
            f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"
        )
