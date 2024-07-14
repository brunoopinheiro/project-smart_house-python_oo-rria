from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class SisSegState(State):

    DESARMADO = 'desarmado'
    ARMADO_COM_GENTE = 'armado_com_gente'
    ARMADO_SEM_NINGUEM = 'armado_sem_ninguem'


class SistemaSeguranca(ObservableDevice):
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
        return self.state

    def notify(self) -> None:
        for observer in self.observers:
            observer.notify(state=self.state)
