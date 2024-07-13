from dispositivos.dispositivo import Dispositivo, State
from transitions import Machine


class SisSegState(State):

    DESARMADO = 'desarmado'
    ARMADO_COM_GENTE = 'armado_com_gente'
    ARMADO_SEM_NINGUEM = 'armado_sem_ninguem'


class SistemaSeguranca(Dispositivo):
    def __init__(self) -> None:
        transitions = [
            {
                'trigger': 'armar_com_gente',
                'source': SisSegState.DESARMADO,
                'dest': SisSegState.ARMADO_COM_GENTE,
            },
            {
                'trigger': 'armar_sem_ninguem',
                'source': SisSegState.DESARMADO,
                'dest': SisSegState.ARMADO_SEM_NINGUEM,
            },
            {
                'trigger': 'desarmar',
                'source': '*',
                'dest': SisSegState.DESARMADO,
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
