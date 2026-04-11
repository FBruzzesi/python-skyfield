from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import BinaryIO

    import pandas as pd

URL: str
PANDAS_MESSAGE: str
_COLUMN_NAMES: tuple[str, ...]

def load_dataframe(fobj: "BinaryIO") -> "pd.DataFrame": ...
