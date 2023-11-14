#----------------------------------------------------------------------------------------------------------------
# DEFINIR AS VARIÁVEIS


from base.base import *


class ExcelExterno:

    def __init__(self, excel):
        self.excel = excel
    
    def __repr__(self):
        return self.excel
