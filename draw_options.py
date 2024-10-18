from dataclasses import dataclass
from typing import Tuple

from RGBA_color import RGBAColor


@dataclass
class DrawOptions:
    color: RGBAColor
    thickness: int
