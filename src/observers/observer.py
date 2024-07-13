from abc import ABC, abstractmethod


class Observer(ABC):

    @property
    def observer_id(self) -> int:
        return self.__observerid

    @observer_id.setter
    def observer_id(self, value) -> None:
        if self.__observerid is None:
            self.__observerid = value

    def __init__(self) -> None:
        self.__observerid = None

    @abstractmethod
    def notify(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def register(self, observer_id: int) -> None:
        self.observer_id = observer_id
