from dispositivos.termostato import Termostato


def main():
    t1 = Termostato()
    t2 = Termostato()
    print(t1)
    print(t2)
    t1.aquecer()
    print(t1)
    t2.esfriar()
    print(t2)
    t1.desligar()
    print(t1.get_state())


if __name__ == '__main__':
    main()
