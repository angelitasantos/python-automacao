#----------------------------------------------------------------------------------------------------------------
# DEFINIR OS DADOS DO CLIENTE / PROCESSO


from cliente.classRede import *


class Cliente:

    def __init__(self, cliente):
        self.cliente = cliente

    def __repr__(self):
        return self.cliente
    