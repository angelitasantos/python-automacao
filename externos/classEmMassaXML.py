#----------------------------------------------------------------------------------------------------------------
# ATUALIZAR DI DOS PROCESSOS EM MASSA


from externos.classEmMassaCapa import *


class EmMassaXML:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    def funcao(self):
        try:
            pass
        except:
            Base.alertar_error_except(self, 'classEmMassaXML', 'funcao')

class EmMassaXMLResult:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.arquivos

