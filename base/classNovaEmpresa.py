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

    def criar_novos_caminhos(self):
        try:
            Base.abrir_powershell(self)
            Base.executar_comando_cd(self, VarGerais.dir_rede)
            Base.executar_comando_mkdir(self, VarGerais.empresa)
            Base.executar_comando_cd(self, VarGerais.empresa)
            Base.executar_comando_mkdir(self, VarRede.pasta_arquivos_modelo)
            Base.executar_comando_mkdir(self, VarSaude.pasta_financeiro)
            Base.fechar_powershell(self)
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_novos_caminhos')

            
