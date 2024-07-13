from observers.observer import Observer
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


class ObservableDevice(Dispositivo):

    @property
    def observers(self) -> list[Observer]:
        return [obs for obs in self.__observers.values()
                if obs['registered'] is True]

    def __init__(self) -> None:
        super().__init__()
        self.__observers: dict[int, dict] = {}
        self.__lastid = 0

    def register(self, observer: Observer) -> None:
        if not isinstance(observer, Observer):
            raise TypeError('This is not a valid observer.')
        if observer.observer_id is None:
            nextid = self.__lastid + 1
            self.__observers[nextid] = {
                'observer': observer,
                'registered': True,
            }
            observer.register(nextid)
            self.__lastid = nextid
        else:
            self.__observers[observer.observer_id]['registered'] = True

    def unregister(self, observerid: int) -> None:
        if observerid in self.__observers:
            self.__observers[observerid]['registered'] = False

    def _get_observer_by_id(self, observerid) -> Observer | None:
        obs = self.__observers.get(observerid)
        if obs is not None:
            if obs['registered'] is True:
                return obs['observer']
            else:
                return None

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError
