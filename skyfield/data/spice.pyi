from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping

    import numpy as np


inertial_frames: "Mapping[str, np.ndarray]"
