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
            6: 'exibir luzes acesas',
            7: 'controlar dispositivo individual',
            8: 'remover dispositivo',
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

    def _get_option(self, options_dict: dict[int, str]) -> int:
        self.__menu_display(options_dict)
        option = None
        while option not in options_dict.keys():
            try:
                option = int(input('>> '))
            except TypeError:
                print('Invalid Option')
        return option

    def __show_device_names(self) -> None:
        names = self.__house.get_device_names()
        for name in names:
            print(f'Device: {name}')

    def __choose_device(self) -> DispositivosEnum:
        opts = DispositivosEnum._value2member_map_
        options_dict = {key: value.name for key, value in opts.items()}
        option_key = self._get_option(options_dict)
        return opts[option_key]

    def __control_single_device(self) -> None:
        print('Qual dispositivo deseja controlar?')
        self.__show_device_names()
        print()
        dev_name = input('>> ')
        self.__house.control_single_device(
            device_name=dev_name,
            _display_func=self._get_option,
        )

    def __remove_device(self) -> None:
        print('Qual dispostivo deseja remover?')
        self.__show_device_names()
        print()
        dev_name = input('>> ')
        result = self.__house.remove_device_by_name(dev_name)
        if result is True:
            print(f'{dev_name} removido com sucesso.')
        else:
            print(f'Falha ao remover {dev_name}')

    def start(self) -> None:
        stopcond = False
        while not stopcond:
            print()
            print('== CONTROLE: Casa Inteligente ==')
            option = self._get_option(self.__menu_options)
            if option == 0:
                stopcond = True
            elif option == 1:
                device = self.__choose_device()
                name = input('Dê um nome ao dispositivo: ')
                self.__house.add_device(device, name)
                print('Dispositivo pareado com sucesso.')
            elif option == 2:
                self.__show_device_names()
            elif option == 3:
                self.__house.report_status()
            elif option == 4:
                self.__house.turn_lights_on()
            elif option == 5:
                self.__house.turn_lights_off()
            elif option == 6:
                self.__house.get_lights_on(print_result=True)
            elif option == 7:
                self.__control_single_device()
            elif option == 8:
                self.__remove_device()
            else:
                print('Opção Indisponível')


if __name__ == '__main__':
    m = Main()
    m.start()
