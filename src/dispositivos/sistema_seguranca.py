from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class SisSegState(State):
    """
    Represents the state of the Sistema de Segurança (Security System).

    Attributes:
        DESARMADO (str): Represents the state when the system is disarmed.
        ARMADO_COM_GENTE (str): Represents the state when the system
        is armed with people inside.
        ARMADO_SEM_NINGUEM (str): Represents the state when the system
        is armed without anyone inside.
    """
    DESARMADO = 'desarmado'
    ARMADO_COM_GENTE = 'armado_com_gente'
    ARMADO_SEM_NINGUEM = 'armado_sem_ninguem'


class SistemaSeguranca(ObservableDevice):
    """
    Represents a security system in a smart house.

    This class inherits from the ObservableDevice class and provides
    functionality to arm, disarm, and notify observers about the state
    of the security system.

    Attributes:
        _machine (Machine): The state machine that manages the transitions
            and states of the security system.
    """

    def __init__(self) -> None:
        super().__init__()
        transitions = [
            {
                'trigger': 'armar_com_gente',
                'source': SisSegState.DESARMADO,
                'dest': SisSegState.ARMADO_COM_GENTE,
                'after': self.notify,
            },
            {
                'trigger': 'armar_sem_ninguem',
                'source': SisSegState.DESARMADO,
                'dest': SisSegState.ARMADO_SEM_NINGUEM,
                'after': self.notify,
            },
            {
                'trigger': 'desarmar',
                'source': '*',
                'dest': SisSegState.DESARMADO,
                'after': self.notify,
            },
        ]
        self._machine = Machine(
            model=self,
            states=SisSegState,
            initial=SisSegState.DESARMADO,
            transitions=transitions,
        )

    def get_state(self) -> State:
        """
        Get the current state of the security system.

        Returns:
            State: The current state of the security system.
        """
        return self.state

    def notify(self) -> None:
        """
        Notify all observers about the current state of the security system.
        """
        for observer in self.observers:
            observer.notify(state=self.state)
