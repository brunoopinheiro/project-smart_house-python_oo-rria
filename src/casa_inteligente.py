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
    """
    The `CasaInteligence` class for used to orchestrate
    many `ObservableDevices`.
    """

    __instance = None

    @property
    def total_observers(self) -> int:
        """
        The number of observers registered for any of the
        house devices.
        """
        return reduce(
            lambda t, _: t + 1,
            self.__observers,
            0
        )

    @property
    def total_devices(self) -> int:
        """
        The number of devices registered in the house.
        """
        return reduce(
            lambda t, _: t + 1,
            self.__devices,
            0
        )

    @property
    def max_devices(self) -> int:
        """
        The maximum amount of devices that can be registered
        in the house.
        """
        return self.__max_devices

    @property
    def light_control_options(self) -> dict[int, str]:
        """The control options for a `Luz` device.

        Returns:
            dict[int, str]: key, option description
        """
        return {
            1: 'ligar',
            2: 'desligar',
        }

    @property
    def termostate_control_options(self) -> dict[int, str]:
        """The control options for a `Termostato` device.

        Returns:
            dict[int, str]: key, option description
        """
        return {
            1: 'aquecer',
            2: 'esfriar',
            3: 'desligar',
        }

    @property
    def sis_sec_control_options(self) -> dict[int, str]:
        """The control options for a `SistemaSeguranca` device.

        Returns:
            dict[int, str]: key, option description
        """
        return {
            1: 'armar_com_gente',
            2: 'armar_sem_ninguem',
            3: 'desarmar',
        }

    def __new__(cls, *args, **kwargs) -> CasaInteligente:
        """
        Singleton implementation for the Main CLI class.
        """
        if cls.__instance is None:
            cls.__instance = super(CasaInteligente, cls).__new__(cls)
        return CasaInteligente.__instance

    def __init__(self, max_devices: int = 5) -> None:
        """
        Constructor method for the `CasaInteligente` class.

        Args:
            max_devices (int, optional): The maximum amount of devices
            the `CasaInteligente` should support. Defaults to 5.
        """
        self.__max_devices = max_devices
        self.__devices: list[ObservableDevice] = []
        self.__observers: list[Observer] = []

    def add_device(
            self,
            device_type: DispositivosEnum,
            name: str,
    ) -> None:
        """Adds a device to the list of devices synced to the
        `CasaInteligente`. The type of device chosen is
        delegated to the `DispositivoFactory` to create a device.
        This method used the `setattr` method
        to add a `name` attribute to the newly added device.

        Args:
            device_type (DispositivosEnum): The type of the device to be added.
            name (str): A name for the device.
        """
        if self.total_devices >= self.max_devices:
            print('Please, remove a device before you add another.')
            return
        new_device = DispositivoFactory.parear_dispositivo(device_type)
        if not hasattr(new_device, 'name'):
            setattr(new_device, 'name', name)
        else:
            new_device.name = name
        self.__devices.append(new_device)
        print('Dispositivo pareado com sucesso.')

    def report_status(self) -> None:
        """
        Shows the `name` and `state` of all devices paired with the house.
        """
        states = [(dev.name, dev.get_state()) for dev in self.__devices]
        for name, devstate in states:
            print(f'{name}\t\t {devstate.name}')

    def get_device_names(self) -> list[str]:
        """Returns a list of device names for all the devices
        paired with the house.

        Returns:
            list[str]: a list of device names.
        """
        return [dev.name for dev in self.__devices]

    def __control_light(self, light: Luz, option: int) -> None:
        """Parses the chosen menu option to the given `Luz` object.

        Args:
            light (Luz): An Instance of a `Luz` object
            option (int): A key that represents the function to be called.
        """
        if option == 1:
            light.ligar()
        if option == 2:
            light.desligar()

    def __control_termostate(self, termo: Termostato, option: int) -> None:
        """Parses the chosen menu option to the given `Termostato` object.

        Args:
            termo (Termostato): An Instance of a `Termostato` object
            option (int): A key that represents the function to be called.
        """
        if option == 1:
            termo.aquecer()
        if option == 2:
            termo.esfriar()
        if option == 3:
            termo.desligar()

    def __control_sissec(self, sis_sec: SistemaSeguranca, option: int) -> None:
        """Parses the chosen menu option
        to the given `SistemaSeguranca` object.

        Args:
            sis_sec (SistemaSeguranca): An Instance of
            a `SistemaSeguranca` object
            option (int): A key that represents the function to be called.
        """
        if option == 1:
            sis_sec.armar_com_gente()
        if option == 2:
            sis_sec.armar_sem_ninguem()
        if option == 3:
            sis_sec.desarmar()

    def __get_device_by_name(
        self,
        device_name: str,
        idx: bool = False,
    ) -> ObservableDevice | int | None:
        """
        Retrieves a device from the list of devices based on its name.

        Args:
            device_name (str): The name of the device to retrieve.
            idx (bool, optional): If True,
            returns the index of the device instead of the device object.
            Defaults to False.

        Returns:
            ObservableDevice | int | None: The device object if found,
            the index of the device if `idx` is True,
            or None if the device is not found.
        """
        for i, dev in enumerate(self.__devices):
            if dev.name == device_name:
                if idx is True:
                    return i
                return dev
        return None

    def add_observer(
        self,
        observer: Observer,
        device_name: str,
    ) -> None:
        """
        Adds an observer to a specific device.

        Parameters:
        - observer (Observer): The observer to be added.
        - device_name (str): The name of the device
        to which the observer will be added.
        """
        device: ObservableDevice = self.__get_device_by_name(device_name)
        device.register(observer)
        self.__observers.append(observer)

    def remove_device_by_name(
        self,
        device_name: str,
    ) -> bool:
        """
        Removes a device from the smart house by its name.

        Args:
            device_name (str): The name of the device to be removed.

        Returns:
            bool: True if the device was successfully removed, False otherwise.
        """
        dev_idx = self.__get_device_by_name(device_name, idx=True)
        if dev_idx is None:
            return False
        self.__devices.pop(dev_idx)
        return True

    def control_single_device(
        self,
        device_name: str,
        option: int | None = None,
        _display_func: Callable | None = None,
    ) -> None:
        """
        Controls a single device in the smart house.

        Args:
            device_name (str): The name of the device to control.
            option (int | None, optional): The control option for the device.
            Defaults to None.
            _display_func (Callable | None, optional): A function used
            to display control options. Defaults to None.
        """
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
        """
        Retrieves a list of all the lights in the smart house.

        Returns:
            list[Luz]: A list of `Luz` objects representing the lights.
        """
        return list(filter(lambda dev: isinstance(dev, Luz), self.__devices))

    def turn_lights_on(self) -> None:
        """
        Turns on all the lights in the smart house.

        This method retrieves the lights in the smart house
        and calls the `ligar()` method on each light object
        to turn them on.
        """
        lights = self.__get_lights()
        # Mesmo que o resultado do map não seja diretamente consumido,
        # o list() é necessário para que o map execute realmente a lambda func
        list(map(lambda x: x.ligar(), lights))

    def turn_lights_off(self) -> None:
        """
        Turns off all the lights in the smart house.
        """
        lights = self.__get_lights()
        list(map(lambda d: d.desligar(), lights))

    def get_lights_on(self, print_result: bool = False) -> list[Luz]:
        """
        Retrieves a list of lights that are currently turned on.

        Args:
            print_result (bool, optional): If True,
            prints the name and state of each light. Defaults to False.

        Returns:
            list[Luz]: A list of Luz objects representing the lights
            that are turned on.
        """
        lights = self.__get_lights()
        lights_on = list(filter(
            lambda lgt: lgt.state == LuzState.LIGADA,
            lights,
        ))
        if print_result:
            for light in lights_on:
                print(f'{light.name}\t\t {light.state.name}')
        return lights_on
