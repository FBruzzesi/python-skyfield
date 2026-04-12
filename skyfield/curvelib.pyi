from numpy import float64
from numpy.typing import NDArray

from .descriptorlib import reify

class Splines:
    table: NDArray[float64]
    lower: NDArray[float64]
    upper: NDArray[float64]
    coefficients: NDArray[float64]
    _width: NDArray[float64]
    _n: NDArray[float64]
    def __init__(self, table: NDArray[float64]) -> None: ...
    def __call__(self, x: NDArray[float64]) -> NDArray[float64]: ...
    @reify
    def derivative(self) -> Splines: ...

def build_spline_given_ends(
    x0: NDArray[float64],
    y0: NDArray[float64],
    slope0: NDArray[float64],
    x1: NDArray[float64],
    y1: NDArray[float64],
    slope1: NDArray[float64],
) -> tuple[NDArray[float64], NDArray[float64], NDArray[float64], NDArray[float64], NDArray[float64], NDArray[float64]]: ...
