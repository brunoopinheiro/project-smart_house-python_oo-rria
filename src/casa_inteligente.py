from __future__ import annotations
from functools import reduce
from observers.observer import Observer
from dispositivos.dispositivo import ObservableDevice
from dispositivos.dispositivo_factory import (
    DispositivoFactory,
    DispositivosEnum,
)
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

    def add_device(
            self,
            device_type: DispositivosEnum,
            name: str,
    ) -> None:
        new_device = DispositivoFactory.parear_dispositivo(device_type)
        if not hasattr(new_device, 'name'):
            setattr(new_device, 'name', name)
        else:
            new_device.name = name
        self.__devices.append(new_device)

    def report_status(self) -> None:
        states = [(dev.name, dev.get_state()) for dev in self.__devices]
        for name, devstate in states:
            print(f'{name}\t\t {devstate.name}')

    def get_device_names(self) -> list[str]:
        return [dev.name for dev in self.__devices]

    def __get_device_by_name(
            self,
            device_name: str,
    ) -> ObservableDevice | None:
        for dev in self.__devices:
            if dev.name == device_name:
                return dev
        return None

    def __get_lights(self) -> list[Luz]:
        return list(filter(lambda dev: isinstance(dev, Luz), self.__devices))

    def turn_lights_on(self) -> None:
        lights = self.__get_lights()
        # Mesmo que o resultado do map não seja diretamente consumido,
        # o list() é necessário para que o map execute realmente a lambda func
        list(map(lambda x: x.ligar(), lights))

    def turn_lights_off(self) -> None:
        lights = self.__get_lights()
        list(map(lambda d: d.desligar(), lights))

    def get_lights_on(self, print_result: bool = False) -> list[Luz]:
        lights = self.__get_lights()
        lights_on = list(filter(
                lambda lgt: lgt.state == LuzState.LIGADA,
                lights,
            ))
        if print_result:
            for light in lights_on:
                print(f'{light.name}\t\t {light.state.name}')
        return lights_on
