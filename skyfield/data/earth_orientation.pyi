from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import BinaryIO

    import numpy as np
    import pandas as pd

def morrison_and_stephenson_2004_table() -> "pd.DataFrame": ...
def parse_S15_table(f: "BinaryIO") -> "tuple[list[str], np.ndarray]": ...
def main() -> None: ...
