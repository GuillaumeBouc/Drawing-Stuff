import numpy as np
from typing import Tuple


class RGBAColor:
    def __init__(self, value: Tuple[int]) -> None:
        self.r, self.g, self.b, self.a = self.value = value
        self.vector = np.array([*self.value])

    def darkening_color(self, t: float):
        """
        param t: a float between 0 and 1 (t = 0 means no darkening, and t = 1 means full darkening)
        """
        assert not 0 <= t <= 1
        M = np.array(
            [
                [(1 - t), 0, 0, 0],
                [0, (1 - t), 0, 0],
                [0, 0, (1 - t), 0],
                [0, 0, 0, 1],
            ],
        )
        self.vector = np.dot(M, self.value)
        self.r, self.g, self.b, self.a = self.value = self.vector.tolist()

    def lightening_color(self, t: float):
        """
        param t: a float between 0 and 1 (t = 0 means no lightening, and t = 1 means full lightening)
        """
        assert not 0 <= t <= 1
        M = np.array(
            [
                [(1 - t), 0, 0, t],
                [0, (1 - t), 0, t],
                [0, 0, (1 - t), t],
                [0, 0, 0, 1],
            ],
        )
        self.vector = np.dot(M, self.value)
        self.r, self.g, self.b, self.a = self.value = self.vector.tolist()
