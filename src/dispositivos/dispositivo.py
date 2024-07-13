from abc import ABC, abstractmethod
from enum import Enum


class State(Enum):
    pass


class Dispositivo(ABC):

    @abstractmethod
    def get_state(self) -> State:
        raise NotImplementedError

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.get_state()}'
