from __future__ import annotations
from getopt import getopt
from sys import argv
from casa_inteligente import CasaInteligente
from dispositivos.dispositivo_factory import DispositivosEnum
from observers.celular import Celular
from observers.email import EMail


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
            9: 'adicionar celular',
            10: 'adicionar e-mail',
            0: 'sair',
        }

    def __new__(cls, *args, **kwargs) -> Main:
        if cls.__instance is None:
            cls.__instance = super(Main, cls).__new__(cls)
        return cls.__instance

    def __init__(self, max_devices: int = 5) -> None:
        self.__house = CasaInteligente(max_devices)
        self.__phone = None
        self.__mail = None

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

    def __add_phone(self) -> None:
        print('Adicionando um Celular')
        print('Digite o número do celular a ser cadastrado.')
        num = input('>> ')
        self.__phone = Celular(num)

    def __add_email(self) -> None:
        print('Adicione um e-mail para receber notificações:')
        email = input('>> ')
        self.__mail = EMail(email)

    def __register_phone_notification(self) -> None:
        print('Escolha o dispositivo a ser vinculado com o celular')
        self.__show_device_names()
        print()
        dev_name = input('>> ')
        self.__house.add_observer(
            observer=self.__phone,
            device_name=dev_name,
        )

    def __register_email_notification(self) -> None:
        print('Escolha o dispositivo a ser vinculado com o e-mail')
        self.__show_device_names()
        print()
        dev_name = input('>> ')
        self.__house.add_observer(
            observer=self.__mail,
            device_name=dev_name,
        )

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
            elif option == 9:
                self.__add_phone()
                self.__register_phone_notification()
            elif option == 10:
                self.__add_email()
                self.__register_email_notification()
            else:
                print('Opção Indisponível')


if __name__ == '__main__':
    max_devices = 5
    args_list = argv[1:]
    try:
        options, args = getopt(args_list, 'm:', ['max-devices='])
    except Exception as err:
        print('Invalid Program Execution', err)
    for name, value in options:
        if name in ['-m', '--max-devices']:
            max_devices = int(value)
    m = Main(max_devices)
    m.start()
