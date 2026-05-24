# ============================================================
#  POO en Python - Figuras Geométricas
#  Clase base: FiguraGeometrica
# ============================================================

class FiguraGeometrica:
    """Super clase que representa una figura geométrica."""

    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho  # usa el setter
        self.alto = alto    # usa el setter

    # ── Getters ─────────────────────────────────────────────
    @property
    def ancho(self) -> float:
        return self._ancho

    @property
    def alto(self) -> float:
        return self._alto

    # ── Setters con validación ───────────────────────────────
    @ancho.setter
    def ancho(self, valor: float):
        if valor <= 0:
            raise ValueError(f"El ancho debe ser mayor que 0. Se recibió: {valor}")
        self._ancho = valor

    @alto.setter
    def alto(self, valor: float):
        if valor <= 0:
            raise ValueError(f"El alto debe ser mayor que 0. Se recibió: {valor}")
        self._alto = valor

    # ── Métodos ──────────────────────────────────────────────
    def area(self) -> float:
        """Calcula el área: ancho * alto."""
        return self._ancho * self._alto

    def perimetro(self) -> float:
        """Método a sobreescribir en las clases hijas."""
        pass

    def __str__(self) -> str:
        return (f"Figura Geométrica | Ancho: {self._ancho} | Alto: {self._alto}")
