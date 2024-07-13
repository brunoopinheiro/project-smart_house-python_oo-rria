from dispositivos.dispositivo import Dispositivo
from dispositivos.luz import Luz
from dispositivos.termostato import Termostato
from dispositivos.sistema_seguranca import SistemaSeguranca
from enum import Enum, auto


class DispositivosEnum(Enum):
    LUZ = auto()
    TERMOSTATO = auto()
    SISTEMA_SEGURANCA = auto()


class DispositivoFactory:

    @staticmethod
    def parear_dispositivo(
        tipo_dispositivo: DispositivosEnum,
        *args,
        **kwargs,
    ) -> Dispositivo:
        if tipo_dispositivo == DispositivosEnum.LUZ:
            return Luz(*args, **kwargs)
        if tipo_dispositivo == DispositivosEnum.TERMOSTATO:
            return Termostato(*args, **kwargs)
        if tipo_dispositivo == DispositivosEnum.SISTEMA_SEGURANCA:
            return SistemaSeguranca(*args, **kwargs)
