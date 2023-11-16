#----------------------------------------------------------------------------------------------------------------
# RETIRAR AS INFORMAÇÕES DO ARQUIVO XML (DI)


from externos.classXMLRoot import *


class XMLExtrair:

    def __init__(self, xml):
        self.xml = xml
    
    def __repr__(self):
        return self.xml
    