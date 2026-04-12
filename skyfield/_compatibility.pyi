from numpy import float64
from numpy.typing import NDArray
from numpy._typing import _ArrayLikeFloat_co, _FloatLike_co  # pyright: ignore[reportPrivateUsage]

__all__ = ("interp", )

def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: None | _FloatLike_co = ...,
    right: None | _FloatLike_co = ...,
    period: None | _FloatLike_co = ...,
) -> NDArray[float64]: ...
