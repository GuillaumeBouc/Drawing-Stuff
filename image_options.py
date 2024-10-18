from dataclasses import dataclass
from typing import Tuple

from RGBA_color import RGBAColor


@dataclass
class ImageOptions:
    size: Tuple[int]
    background_color: RGBAColor
