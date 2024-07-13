from dispositivos.dispositivo import Dispositivo, State
from transitions import Machine


class LuzState(State):

    DESLIGADA = False
    LIGADA = True


class Luz(Dispositivo):

    def __init__(self) -> None:
        transitions = [
            {
                'trigger': 'ligar',
                'source': LuzState.DESLIGADA,
                'dest': LuzState.LIGADA,
            },
            {
                'trigger': 'desligar',
                'source': LuzState.LIGADA,
                'dest': LuzState.DESLIGADA,
            },
        ]
        self._machine = Machine(
            model=self,
            states=LuzState,
            initial=LuzState.DESLIGADA,
            transitions=transitions,
        )

    def get_state(self) -> State:
        return self.state
