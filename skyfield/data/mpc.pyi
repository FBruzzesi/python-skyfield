import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import BinaryIO

    import pandas as pd

    from skyfield.keplerlib import _KeplerOrbit
    from skyfield.timelib import Timescale

MPCORB_URL: str
_MPCORB_COLUMNS: list[tuple[str, tuple[int, int]]]
_MPCORB_NECESSARY_COLUMNS: set[str]
_MPCORB_DTYPES: dict[str, str]
_MPCORB_CONVERTERS: dict[str, type]

COMET_URL: str

_COMET_COLUMNS: list[tuple[str, tuple[int, int]]]
_COMET_FAST_COLUMNS: tuple[str, ...]
_COMET_SEP: str
_fast_comet_re: re.Pattern[bytes] | None
_fast_comet_sub: bytes | None

def load_mpcorb_dataframe(fobj: "BinaryIO") -> "pd.DataFrame": ...
def mpcorb_orbit(row: "pd.Series", ts: "Timescale", gm_km3_s2: float) -> "_KeplerOrbit": ...
def load_comets_dataframe(fobj: "BinaryIO") -> "pd.DataFrame": ...
def load_comets_dataframe_slow(fobj: "BinaryIO") -> "pd.DataFrame": ...
def comet_orbit(row: "pd.Series", ts: "Timescale", gm_km3_s2: float) -> "_KeplerOrbit": ...
def _comet_orbits(rows: "pd.DataFrame", ts: "Timescale", gm_km3_s2: float) -> "_KeplerOrbit": ...
def unpack(designation_packed: str) -> str: ...
