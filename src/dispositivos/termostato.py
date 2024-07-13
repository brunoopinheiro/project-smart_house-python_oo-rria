from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class TermostatoState(State):

    DESLIGADO = 'desligado'
    AQUECENDO = 'aquecendo'
    ESFRIANDO = 'esfriando'


class Termostato(ObservableDevice):
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
        return self.state

    def notify(self) -> None:
        for observer in self.observers:
            observer.notify(state=self.state)
