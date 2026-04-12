from numpy import float64
from numpy.typing import NDArray

from .timelib import Time

ke0_t: NDArray[float64]
ke1: NDArray[float64]
lunisolar_longitude_coefficients: NDArray[float64]
lunisolar_obliquity_coefficients: NDArray[float64]
nals_t: NDArray[float64]
napl_t: NDArray[float64]
nutation_coefficients_longitude: NDArray[float64]
nutation_coefficients_obliquity: NDArray[float64]
se0_t_0: NDArray[float64]
se0_t_1: NDArray[float64]

anomaly_constant: NDArray[float64]
anomaly_coefficient: NDArray[float64]

fa0: NDArray[float64]
fa1: NDArray[float64]
fa2: NDArray[float64]
fa3: NDArray[float64]
fa4: NDArray[float64]

se1_0: float
se1_1: float

def iau2000a_radians(
    t: Time,
    fundamental_argument_terms: int = ...,
    lunisolar_terms: int = ...,
    planetary_terms: int = ...,
) -> tuple[NDArray[float64], NDArray[float64]]: ...

def iau2000b_radians(t: Time) -> tuple[NDArray[float64], NDArray[float64]]: ...

def build_nutation_matrix(
    mean_obliquity_radians: NDArray[float64],
    true_obliquity_radians: NDArray[float64],
    psi_radians: NDArray[float64],
) -> NDArray[float64]: ...

def mean_obliquity(jd_tdb: NDArray[float64]) -> NDArray[float64]: ...

def equation_of_the_equinoxes_complimentary_terms(
    jd_tt: NDArray[float64],
) -> NDArray[float64]: ...

def iau2000a(
    jd_tt: NDArray[float64],
    fundamental_argument_terms: int = ...,
    lunisolar_terms: int = ...,
    planetary_terms: int = ...,
) -> tuple[NDArray[float64], NDArray[float64]]: ...

def iau2000b(jd_tt: NDArray[float64]) -> tuple[NDArray[float64], NDArray[float64]]: ...

def fundamental_arguments(
    t: NDArray[float64],
    terms: int = ...,
) -> NDArray[float64]: ...

def compute_nutation(t: Time) -> NDArray[float64]: ...

def earth_tilt(
    t: Time,
) -> tuple[NDArray[float64], NDArray[float64], NDArray[float64], NDArray[float64], NDArray[float64]]: ...
