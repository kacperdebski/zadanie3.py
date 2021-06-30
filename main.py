from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def nazwa(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok1):
        self.bok1 = bok1

    def oblicz_pole(self):
        return self.bok1 ** 2

class Prostokat(Kwadrat):
    def __init__(self, bok1, bok2):
        super().__init__(bok1)
        self.bok2 = bok2

    def oblicz_pole(self):
        return self.bok1 * self.bok2
