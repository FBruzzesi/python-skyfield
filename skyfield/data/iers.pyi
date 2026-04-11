from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import BinaryIO

    import numpy as np

    from skyfield.timelib import Timescale

inf: float
_R: bytes

def parse_x_y_dut1_from_finals_all(f: "BinaryIO") -> "np.ndarray": ...
def install_polar_motion_table(ts: "Timescale", finals_data: "np.ndarray") -> None: ...
def build_timescale_arrays(utc_mjd: "np.ndarray", dut1: "np.ndarray") -> "tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]": ...
def parse_dut1_from_finals_all(f: "BinaryIO") -> "tuple[np.ndarray, np.ndarray]": ...
