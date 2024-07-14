from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class TermostatoState(State):
    """
    Represents the state of a thermostat.

    Attributes:
        DESLIGADO (str): Represents the 'off' state of the thermostat.
        AQUECENDO (str): Represents the 'heating' state of the thermostat.
        ESFRIANDO (str): Represents the 'cooling' state of the thermostat.
    """
    DESLIGADO = 'desligado'
    AQUECENDO = 'aquecendo'
    ESFRIANDO = 'esfriando'


class Termostato(ObservableDevice):
    """
    A class representing a thermostat device.

    This class inherits from the `ObservableDevice` class and provides
    functionality to control the temperature of a smart house.

    Attributes:
        _machine (Machine): The state machine used to manage the transitions
            between different thermostat states.

    Methods:
        get_state: Returns the current state of the thermostat.
        notify: Notifies all observers about
            the current state of the thermostat.
    """

    def __init__(self) -> None:
        super().__init__()
        transitions = [
            {
                'trigger': 'aquecer',
                'source': TermostatoState.DESLIGADO,
                'dest': TermostatoState.AQUECENDO,
                'after': self.notify,
            },
            {
                'trigger': 'esfriar',
                'source': TermostatoState.DESLIGADO,
                'dest': TermostatoState.ESFRIANDO,
                'after': self.notify,
            },
            {
                'trigger': 'desligar',
                'source': '*',
                'dest': TermostatoState.DESLIGADO,
                'after': self.notify,
            },
        ]
        self._machine = Machine(
            model=self,
            states=TermostatoState,
            initial=TermostatoState.DESLIGADO,
            transitions=transitions,
        )

    def get_state(self) -> State:
        """
        Get the current state of the thermostat.

        Returns:
            State: The current state of the thermostat.
        """
        return self.state

    def notify(self) -> None:
        """
        Notify all observers about the current state of the thermostat.
        """
        for observer in self.observers:
            observer.notify(state=self.state)
