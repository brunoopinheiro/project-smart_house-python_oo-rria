from __future__ import annotations
from functools import reduce
from observers.observer import Observer
from dispositivos.dispositivo import ObservableDevice
from dispositivos.luz import Luz, LuzState


class CasaInteligente:

    __instance = None

    @property
    def total_observers(self) -> int:
        return reduce(
            lambda t, _: t + 1,
            self.__observers,
            0
        )

    def __new__(cls, *args, **kwargs) -> CasaInteligente:
        if cls.__instance is None:
            cls.__instance = super(CasaInteligente, cls).__new__(cls)
        return CasaInteligente.__instance

    def __init__(self) -> None:
        self.__devices: list[ObservableDevice] = []
        self.__observers: list[Observer] = []

    def report_status(self) -> None:
        states = [dev.get_state() for dev in self.__devices]
        for devstate in states:
            print(devstate)

    def __get_lights(self) -> list[Luz]:
        return list(filter(lambda dev: isinstance(dev, Luz), self.__devices))

    def turn_lights_on(self) -> None:
        lights = self.__get_lights()
        map(lambda d: d.ligar(), lights)

    def turn_lights_off(self) -> None:
        lights = self.__get_lights()
        map(lambda d: d.desligar(), lights)

    def get_lights_on(self) -> list[ObservableDevice]:
        lights = self.__get_lights()
        lights_on = list(filter(
                lambda lgt: lgt.state == LuzState.LIGADA,
                lights,
            ))
        return lights_on
