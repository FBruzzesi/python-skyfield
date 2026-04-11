from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal, TypeAlias

    PlanetName: TypeAlias = Literal[
        'Sun',
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
        '134340 Pluto',
    ]

radii_km: list[tuple["PlanetName", float]]

def festoon_ephemeris(ephemeris: object) -> None: ...
