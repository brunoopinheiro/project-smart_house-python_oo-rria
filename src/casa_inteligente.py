from __future__ import annotations
from typing import Callable
from functools import reduce
from observers.observer import Observer
from dispositivos.dispositivo import ObservableDevice
from dispositivos.dispositivo_factory import (
    DispositivoFactory,
    DispositivosEnum,
)
from dispositivos.luz import Luz, LuzState
from dispositivos.termostato import Termostato
from dispositivos.sistema_seguranca import SistemaSeguranca


class CasaInteligente:

    __instance = None

    @property
    def total_observers(self) -> int:
        return reduce(
            lambda t, _: t + 1,
            self.__observers,
            0
        )

    @property
    def light_control_options(self) -> dict[int, str]:
        return {
            1: 'ligar',
            2: 'desligar',
        }

    @property
    def termostate_control_options(self) -> dict[int, str]:
        return {
            1: 'aquecer',
            2: 'esfriar',
            3: 'desligar',
        }

    @property
    def sis_sec_control_options(self) -> dict[int, str]:
        return {
            1: 'armar_com_gente',
            2: 'armar_sem_ninguem',
            3: 'desarmar',
        }

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

    def __control_light(self, light: Luz, option: int) -> None:
        if option == 1:
            light.ligar()
        if option == 2:
            light.desligar()

    def __control_termostate(self, termo: Termostato, option: int) -> None:
        if option == 1:
            termo.aquecer()
        if option == 2:
            termo.esfriar()
        if option == 3:
            termo.desligar()

    def __control_sissec(self, sis_sec: SistemaSeguranca, option: int) -> None:
        if option == 1:
            sis_sec.armar_com_gente()
        if option == 2:
            sis_sec.armar_sem_ninguem()
        if option == 3:
            sis_sec.desarmar()

    def __get_device_by_name(
            self,
            device_name: str,
    ) -> ObservableDevice | None:
        for dev in self.__devices:
            if dev.name == device_name:
                return dev
        return None

    def control_single_device(
            self,
            device_name: str,
            option: int | None = None,
            _display_func: Callable | None = None,
    ) -> None:
        device = self.__get_device_by_name(device_name)
        if device is None:
            return
        if isinstance(device, Luz):
            if _display_func is not None:
                option = _display_func(self.light_control_options)
            self.__control_light(device, option)
        if isinstance(device, Termostato):
            if _display_func is not None:
                option = _display_func(self.termostate_control_options)
            self.__control_termostate(device, option)
        if isinstance(device, SistemaSeguranca):
            if _display_func is not None:
                option = _display_func(self.sis_sec_control_options)
            self.__control_sissec(device, option)

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
