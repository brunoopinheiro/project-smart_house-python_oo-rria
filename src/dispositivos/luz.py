from dispositivos.dispositivo import ObservableDevice, State
from transitions import Machine


class LuzState(State):

    DESLIGADA = False
    LIGADA = True


class Luz(ObservableDevice):

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
        return self.state

    def notify(self) -> None:
        if len(self.observers) > 0:
            for observer in self.observers:
                observer.notify(state=self.state)
