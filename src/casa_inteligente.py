from __future__ import annotations


class CasaInteligente:

    __instance = None

    def __new__(cls, *args, **kwargs) -> CasaInteligente:
        if cls.__instance is None:
            cls.__instance = super(CasaInteligente, cls).__new__(cls)
        return CasaInteligente.__instance
