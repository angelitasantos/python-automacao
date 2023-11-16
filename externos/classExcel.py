#----------------------------------------------------------------------------------------------------------------
# ATUALIZAR AS INFORMAÇÕES DO ARQUIVO XML (DI) NA PLANILHA DE EXCEL


from externos.classXMLExtrair import *


class Excel:

    def __init__(self, excel):
        self.excel = excel

    def __repr__(self):
        return self.excel
    
    