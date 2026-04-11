from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from collections.abc import Iterable

    Edge = tuple[int, int]

class StarName(NamedTuple):
    hip: int
    name: str

def parse_constellations(lines: "Iterable[bytes]") -> list[tuple[str, list["Edge"]]]: ...
def parse_star_names(lines: "Iterable[bytes]") -> list[StarName]: ...
