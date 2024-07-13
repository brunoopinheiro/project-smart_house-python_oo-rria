from __future__ import annotations
from casa_inteligente import CasaInteligente
from dispositivos.dispositivo_factory import DispositivosEnum


class Main:

    __instance = None

    @property
    def __menu_options(self) -> dict[int, str]:
        return {
            1: 'adicionar dispositivo',
            2: 'listar dispositivos',
            3: 'status dos dispositivos',
            4: 'ligar todas as luzes',
            5: 'desligar todas as luzes',
            0: 'sair',
        }

    def __new__(cls) -> Main:
        if cls.__instance is None:
            cls.__instance = super(Main, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.__house = CasaInteligente()

    def __menu_display(self, options_dict: dict[int, str]) -> None:
        menuopts = ''
        for key, value in options_dict.items():
            menuopts = menuopts + f'[{key}] - {value.upper()}\n'
        print(menuopts)

    def __get_option(self, options_dict: dict[int, str]) -> int:
        self.__menu_display(options_dict)
        option = None
        while option not in options_dict.keys():
            try:
                option = int(input('>> '))
            except TypeError:
                print('Invalid Option')
        return option

    def __choose_device(self) -> DispositivosEnum:
        opts = DispositivosEnum._value2member_map_
        options_dict = {key: value.name for key, value in opts.items()}
        option_key = self.__get_option(options_dict)
        return opts[option_key]

    def start(self) -> None:
        stopcond = False
        while not stopcond:
            print()
            print('== CONTROLE: Casa Inteligente ==')
            option = self.__get_option(self.__menu_options)
            if option == 0:
                stopcond = True
            elif option == 1:
                device = self.__choose_device()
                name = input('Dê um nome ao dispositivo: ')
                self.__house.add_device(device, name)
                print('Dispositivo pareado com sucesso.')
            elif option == 2:
                names = self.__house.get_device_names()
                for name in names:
                    print(f'Device: {name.upper()}')
            elif option == 3:
                self.__house.report_status()
            elif option == 4:
                self.__house.turn_lights_on()
            elif option == 5:
                self.__house.turn_lights_off()
            else:
                print('Opção Indisponível')


if __name__ == '__main__':
    m = Main()
    m.start()
