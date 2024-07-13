from observers.observer import Observer


class Celular(Observer):
    """Not a real implementation.
    This class servers just to ilustrate
    the Observer pattern."""

    @property
    def number(self) -> str:
        return self.__number

    def __init__(
        self,
        number: str,
    ) -> None:
        super().__init__()
        self.__number = number

    def notify(self, *args, **kwargs) -> None:
        print(f'CELULAR {self.number}: Notificado {args} {kwargs}')
