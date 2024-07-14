from observers.observer import Observer
from abc import ABC, abstractmethod
from enum import Enum


class State(Enum):
    """
    Represents the state of a device.
    """

    pass


class Dispositivo(ABC):
    """
    Abstract base class for devices in the smart house system.
    """

    @abstractmethod
    def get_state(self) -> State:
        """
        Abstract method to get the state of the device.
        Returns:
            The state of the device.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Returns a string representation of the device.
        Returns:
            A string representation of the device.
        """
        return f'{type(self).__name__}: {self.get_state()}'


class ObservableDevice(Dispositivo):
    """
    A class representing an observable device.

    This class extends the base `Dispositivo`
    class and provides functionality for registering
    and unregistering observers,
    as well as notifying them of changes.

    Attributes:
        __observers (dict[int, dict]): A dictionary
        containing information about registered observers.
        __lastid (int): The ID of the last registered observer.

    Methods:
        observers() -> list[Observer]: Returns a list of registered observers.
        register(observer: Observer) -> None: Registers a new observer.
        unregister(observerid: int) -> None: Unregisters an observer.
        _get_observer_by_id(observerid) -> Observer | None: Returns the
        observer with the specified ID.
        notify() -> None: Notifies all registered observers of a change.
    """

    @property
    def observers(self) -> list[Observer]:
        """
        Get the list of registered observers.

        Returns:
            list[Observer]: A list of registered observers.
        """
        if len(self.__observers) > 0:
            return [obs['observer'] for obs in self.__observers.values()
                    if obs['registered'] is True]
        return []

    def __init__(self) -> None:
        super().__init__()
        self.__observers: dict[int, dict] = {}
        self.__lastid = 0

    def register(self, observer: Observer) -> None:
        """
        Register a new observer.

        Args:
            observer (Observer): The observer to register.

        Raises:
            TypeError: If the provided observer is not a valid observer.
        """
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
        """
        Unregister an observer.

        Args:
            observerid (int): The ID of the observer to unregister.
        """
        if observerid in self.__observers:
            self.__observers[observerid]['registered'] = False

    def _get_observer_by_id(self, observerid) -> Observer | None:
        """
        Get the observer with the specified ID.

        Args:
            observerid: The ID of the observer.

        Returns:
            Observer | None: The observer with the specified ID,
            or None if not found or not registered.
        """
        obs = self.__observers.get(observerid)
        if obs is not None:
            if obs['registered'] is True:
                return obs['observer']
            else:
                return None

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all registered observers of a change.

        This method should be implemented by subclasses.
        """
        raise NotImplementedError
