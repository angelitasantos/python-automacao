#----------------------------------------------------------------------------------------------------------------
# RETIRAR AS INFORMAÇÕES DO ARQUIVO XML (DI)


from externos.classXMLListas import *


class XMLRoot:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.xml
    
    def existe_arquivo_txt(self, caminho, arquivo):
        try:
            existe_arquivo_txt, arquivo_di_txt = Base.pesquisar_existe_arquivo(Base.self, caminho, arquivo)
            return existe_arquivo_txt, arquivo_di_txt, caminho
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'existe_arquivo_txt')



            