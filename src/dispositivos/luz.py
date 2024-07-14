from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class LuzState(State):
    """
    Represents the state of a light device.

    Attributes:
        DESLIGADA (bool): Represents the state when the light is turned off.
        LIGADA (bool): Represents the state when the light is turned on.
    """
    DESLIGADA = False
    LIGADA = True


class Luz(ObservableDevice):
    """
    Represents a light device that can be turned on or off.

    Inherits from the ObservableDevice class.

    Attributes:
        _machine (Machine): The state machine
        that manages the transitions of the light device.
    """

    def __init__(self) -> None:
        super().__init__()
        transitions = [
            {
                'trigger': 'ligar',
                'source': LuzState.DESLIGADA,
                'dest': LuzState.LIGADA,
                'after': self.notify,
            },
            {
                'trigger': 'desligar',
                'source': LuzState.LIGADA,
                'dest': LuzState.DESLIGADA,
                'after': self.notify,
            },
        ]
        self._machine = Machine(
            model=self,
            states=LuzState,
            initial=LuzState.DESLIGADA,
            transitions=transitions,
        )

    def get_state(self) -> State:
        """
        Get the current state of the light device.

        Returns:
            State: The current state of the light device.
        """
        return self.state

    def notify(self) -> None:
        """
        Notify the observers when the state of the light device changes.

        This method is called after a transition occurs.
        It notifies each observer by calling their `notify` method with
        the current state as an argument.
        """
        if len(self.observers) > 0:
            for observer in self.observers:
                observer.notify(state=self.state)
