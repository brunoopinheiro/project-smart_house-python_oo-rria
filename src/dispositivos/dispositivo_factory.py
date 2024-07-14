from dispositivos.dispositivo import Dispositivo
from dispositivos.luz import Luz
from dispositivos.termostato import Termostato
from dispositivos.sistema_seguranca import SistemaSeguranca
from enum import Enum, auto


class DispositivosEnum(Enum):
    """Enumeration class for different types of devices in a smart house."""

    LUZ = auto()
    TERMOSTATO = auto()
    SISTEMA_SEGURANCA = auto()


class DispositivoFactory:
    """
    A factory class for creating different types of devices.
    """

    @staticmethod
    def parear_dispositivo(
        tipo_dispositivo: DispositivosEnum,
        *args,
        **kwargs,
    ) -> Dispositivo:
        """
        Creates and returns an instance of the specified device type.

        Args:
            tipo_dispositivo (DispositivosEnum): The type of device to create.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Dispositivo: An instance of the specified device type.
        """
        if tipo_dispositivo == DispositivosEnum.LUZ:
            return Luz(*args, **kwargs)
        if tipo_dispositivo == DispositivosEnum.TERMOSTATO:
            return Termostato(*args, **kwargs)
        if tipo_dispositivo == DispositivosEnum.SISTEMA_SEGURANCA:
            return SistemaSeguranca(*args, **kwargs)
