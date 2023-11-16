#----------------------------------------------------------------------------------------------------------------
# GERAR CAPA DOS PROCESSOS A PARTIR DO ARQUIVO EM MASSA


from externos.classSaude import *


class EmMassaCapa:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    try:
        arquivo_em_massa = VarRede.arquivo_em_massa
    except:
        Base.alertar_error_except(Base.self, 'classEmMassaCapa', 'EmMassaCapa')
    