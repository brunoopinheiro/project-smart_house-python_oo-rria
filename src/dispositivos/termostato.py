from dispositivos.dispositivo import Dispositivo, State
from transitions import Machine


class TermostatoState(State):

    DESLIGADO = 'desligado'
    AQUECENDO = 'aquecendo'
    ESFRIANDO = 'esfriando'


class Termostato(Dispositivo):
    def __init__(self) -> None:
        transitions = [
            {
                'trigger': 'aquecer',
                'source': TermostatoState.DESLIGADO,
                'dest': TermostatoState.AQUECENDO,
            },
            {
                'trigger': 'esfriar',
                'source': TermostatoState.DESLIGADO,
                'dest': TermostatoState.ESFRIANDO,
            },
            {
                'trigger': 'desligar',
                'source': '*',
                'dest': TermostatoState.DESLIGADO,
            },
        ]
        self._machine = Machine(
            model=self,
            states=TermostatoState,
            initial=TermostatoState.DESLIGADO,
            transitions=transitions,
        )

    def get_state(self) -> State:
        return self.state
