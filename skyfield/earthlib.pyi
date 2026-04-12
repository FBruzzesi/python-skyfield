from __future__ import annotations

from numpy import float64
from numpy.typing import NDArray

from .timelib import Time

earth_radius_au: float
one_minus_flattening: float
one_minus_flattening_squared: float

def terra(
    latitude: NDArray[float64],
    longitude: NDArray[float64],
    elevation: NDArray[float64],
    gast: NDArray[float64],
) -> tuple[NDArray[float64], NDArray[float64]]: ...

def reverse_terra(
    xyz_au: NDArray[float64],
    gast: NDArray[float64],
    iterations: int = ...,
) -> tuple[NDArray[float64], NDArray[float64], NDArray[float64]]: ...

def compute_limb_angle(
    position_au: NDArray[float64],
    observer_au: NDArray[float64],
) -> tuple[NDArray[float64], NDArray[float64]]: ...

def sidereal_time(t: Time) -> NDArray[float64]: ...

def earth_rotation_angle(
    jd_ut1: NDArray[float64],
    fraction_ut1: NDArray[float64] = ...,
) -> NDArray[float64]: ...

def refraction(
    alt_degrees: NDArray[float64],
    temperature_C: NDArray[float64],
    pressure_mbar: NDArray[float64],
) -> NDArray[float64]: ...

def refract(
    alt_degrees: NDArray[float64],
    temperature_C: NDArray[float64],
    pressure_mbar: NDArray[float64],
) -> NDArray[float64]: ...
