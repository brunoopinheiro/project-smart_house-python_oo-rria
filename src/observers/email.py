from observer import Observer


class EMail(Observer):
    """Not a real implementation.
    This class servers just to ilustrate
    the Observer pattern."""

    @property
    def address(self) -> str:
        return self.__address

    def __init__(
        self,
        address: str,
    ) -> None:
        super().__init__()
        self.__address = address

    def notify(self, *args, **kwargs) -> None:
        print(f'E-Mail {self.address}: Notificado {args} {kwargs}')
