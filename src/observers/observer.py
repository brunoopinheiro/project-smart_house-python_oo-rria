from abc import ABC, abstractmethod


class Observer(ABC):
    """
    The base class for all observers in the system.

    Attributes:
        observer_id (int): The unique identifier for the observer.

    Methods:
        notify(*args, **kwargs): Notifies the observer
            with the given arguments.
        register(observer_id: int): Registers the observer
            with the given observer ID.
    """

    @property
    def observer_id(self) -> int:
        """
        Returns the ID of the observer.

        Returns:
            int: The ID of the observer.
        """
        return self.__observerid

    @observer_id.setter
    def observer_id(self, value) -> None:
        """
        Sets the observer ID.

        Args:
            value: The ID of the observer.

        Returns:
            None
        """
        if self.__observerid is None:
            self.__observerid = value

    def __init__(self) -> None:
        self.__observerid = None

    @abstractmethod
    def notify(self, *args, **kwargs) -> None:
        """
        Notify the observer about an event.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            NotImplementedError: This method should
                be implemented by subclasses.
        """
        raise NotImplementedError

    def register(self, observer_id: int) -> None:
        """
        Register the observer with the given observer_id.

        Args:
            observer_id (int): The ID of the observer.

        Returns:
            None
        """
        self.observer_id = observer_id
