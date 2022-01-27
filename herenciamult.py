from turtle import Vec2D


class acelerar:
    def __init__(self):
        pass
    
    def acelerar(self):
        print('Voy acelerando')

class frenar:
    def __init__(self):
        pass

    def frenar(self):
        print('Voy frenando')

class pitar:
    def __init__(self):
        pass
    
    def pitar(self):
        print('Estoy pitando')


class vehiculo(acelerar,frenar,pitar):
    def __del__(self):
        pass

carro = vehiculo()

print(carro.acelerar())
print(carro.frenar())
print(carro.pitar())