from model.Vehiculo import Vehiculo

class Miniband(Vehiculo):

    def __init__(self, marca, modelo, anio, pasajero):
        super().__init__(marca, modelo, anio)
        self.pasajero=pasajero

    def descripcion(self):
        return f"{super().descripcion()}, Nro de pasajeros: {self.pasajero}"