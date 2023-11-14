#----------------------------------------------------------------------------------------------------------------
# CRIAR PASTAS E GERAR ARQUIVOS MODELOS PARA NOVA EMPRESA


from base.main import *


class NovaEmpresa:

    def __init__(self, main):
        self.geral = main

    def __repr__(self):
        return self.main

    def criar_nova_empresa(self):
        try:
            if VarGerais.dir_rede == 'C:\\':
                criar_caminho = True
                return criar_caminho
            else:
                criar_caminho = False
                return criar_caminho
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_nova_empresa')


