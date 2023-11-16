#----------------------------------------------------------------------------------------------------------------
# RETIRAR AS INFORMAÇÕES DO ARQUIVO XML (DI)


from externos.classXMLListas import *


class XMLRoot:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.xml
    
    def pesquisar_existe_arquivo_txt(self, caminho, arquivo):
        try:
            existe_arquivo_txt, arquivo_di_txt = Base.pesquisar_existe_arquivo(Base.self, caminho, arquivo)
            return existe_arquivo_txt, arquivo_di_txt, caminho
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'existe_arquivo_txt')

    def listar_caminho_arquivos_txt_xml(self, lista_caminho=[], lista_caminho_pc=[], lista_arquivo_txt=[], lista_arquivo_xml=[]):
        try:
            lista_caminho_txt = []
            lista_caminho_pc_txt = []
            lista_caminho_xml = []
            lista_caminho_pc_xml = []

            for caminho in lista_caminho:
                index_lista_caminho = lista_caminho.index(caminho)
                existe_txt, arquivo_txt, caminho_txt, = XMLRoot.existe_arquivo_txt(Base.self, lista_caminho[index_lista_caminho], lista_arquivo_txt[index_lista_caminho])
                lista_txt = [existe_txt, arquivo_txt, caminho_txt]
                lista_caminho_txt.append(lista_txt)
            for caminho in lista_caminho_pc:
                index_lista_caminho = lista_caminho_pc.index(caminho)
                existe_txt_pc, arquivo_txt_pc, caminho_pc_txt = XMLRoot.existe_arquivo_txt(Base.self, lista_caminho_pc[index_lista_caminho], lista_arquivo_txt[index_lista_caminho])
                lista_pc_txt = [existe_txt_pc, arquivo_txt_pc, caminho_pc_txt]
                lista_caminho_pc_txt.append(lista_pc_txt)
            for caminho in lista_caminho:
                index_lista_caminho = lista_caminho.index(caminho)
                existe_arquivo_xml, arquivo_di_xml, caminho_xml = XMLRoot.existe_arquivo_txt(Base.self, lista_caminho[index_lista_caminho], lista_arquivo_xml[index_lista_caminho])
                lista_xml = [existe_arquivo_xml, arquivo_di_xml, caminho_xml]
                lista_caminho_xml.append(lista_xml)
            for caminho in lista_caminho_pc:
                index_lista_caminho = lista_caminho_pc.index(caminho)
                existe_arquivo_xml_pc, arquivo_di_pc_xml, caminho_pc_xml = XMLRoot.existe_arquivo_txt(Base.self, lista_caminho_pc[index_lista_caminho], lista_arquivo_xml[index_lista_caminho])
                lista_pc_xml = [existe_arquivo_xml_pc, arquivo_di_pc_xml, caminho_pc_xml]
                lista_caminho_pc_xml.append(lista_pc_xml)
            return lista_caminho_txt, lista_caminho_pc_txt, lista_caminho_xml, lista_caminho_pc_xml
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'listar_caminho_arquivo')

    def listar_arquivo_xml_ausente(self, lista_caminho_pc_xml=[]):
        try:
            lista_arquivo_di_xml = []
            lista_pasta_origem  = []
            lista_pasta_destino  = []
            lista_processo = []

            for caminho in lista_caminho_pc_xml:
                for indice, dados in enumerate(caminho):
                    if indice == 0:
                        existe_arquivo_xml_pc = caminho[indice]
                        if existe_arquivo_xml_pc == False:
                            caminho_processo = caminho[2]
                            caminho_proc = caminho_processo.replace('PC\\', '')
                            arquivo_txt = caminho[1]
                            arquivo_txt_novo = arquivo_txt.replace('.xml', '.txt')
                            lista_arquivo_di_xml.append(caminho[1])
                            lista_pasta_origem.append(caminho_proc)
                            lista_pasta_destino.append(caminho[2])
            for caminho in lista_caminho_pc_xml:
                for indice, dados in enumerate(caminho):
                    if indice == 0:
                        existe_arquivo_xml_pc = caminho[indice]
                        arquivo_txt = caminho[1]
                        arquivo_txt_novo = arquivo_txt.replace(' - DI.xml', '')
                        lista_processo.append(arquivo_txt_novo)
            return lista_arquivo_di_xml, lista_pasta_origem, lista_pasta_destino, lista_processo
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'listar_arquivo_xml_ausente')

    def listar_arquivo_txt_xml_existentes(self, lista_caminho_txt=[], lista_caminho_pc_txt=[], lista_caminho_xml=[]):
        try:
            lista_processo_txt = []
            lista_processo_pc_txt  = []
            lista_processo_xml = []
            for caminho in lista_caminho_txt:
                for indice, dados in enumerate(caminho):
                    if indice == 0:
                        existe_arquivo_xml_pc = caminho[indice]
                        if existe_arquivo_xml_pc == True:
                            lista_processo_txt.append(caminho[1])
            for caminho in lista_caminho_pc_txt:
                for indice, dados in enumerate(caminho):
                    if indice == 0:
                        existe_arquivo_xml_pc = caminho[indice]
                        if existe_arquivo_xml_pc == True:
                            lista_processo_pc_txt.append(caminho[1])
            for caminho in lista_caminho_xml:
                for indice, dados in enumerate(caminho):
                    if indice == 0:
                        existe_arquivo_xml_pc = caminho[indice]
                        if existe_arquivo_xml_pc == True:
                            lista_processo_xml.append(caminho[1])
            return lista_processo_txt, lista_processo_pc_txt, lista_processo_xml
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'listar_arquivo_txt_existentes')

    def trocar_txt_xml(self, ref_cliente=[], lista_processo_txt=[], lista_processo_pc_txt=[], lista_processo_xml=[], lista_arquivo_di_xml=[], lista_pasta_destino=[], lista_pasta_origem=[]):
        try:
            processo_txt = Base.procurar_arquivo(self, ref_cliente, lista_processo_txt)
            processo_pc_txt = Base.procurar_arquivo(self, ref_cliente, lista_processo_pc_txt)
            processo_xml = Base.procurar_arquivo(self, ref_cliente, lista_processo_xml)
            processo_pc_xml = Base.procurar_arquivo(self, ref_cliente, lista_arquivo_di_xml)
            pasta_destino = Base.procurar_arquivo(self, ref_cliente, lista_pasta_destino)
            pasta_origem = Base.procurar_arquivo(self, ref_cliente, lista_pasta_origem)
            pasta_origem_f = f'{pasta_origem}{processo_pc_xml}'
            pasta_destino_f = f'{pasta_destino}{processo_pc_xml}'

            if processo_xml != None and processo_pc_xml != None:
                Base.abrir_powershell(self)
                time.sleep(Base.time_sleep_1)
                move_pastas = f'move "{pasta_origem_f}" "{pasta_destino_f}"'
                pyperclip.copy(move_pastas)
                time.sleep(Base.time_sleep_1)
                Base.executar_hotkey_colar(self)
                Base.fechar_powershell(self)
            elif processo_txt != None and processo_pc_xml != None:
                Base.abrir_powershell(self)
                time.sleep(Base.time_sleep_1)
                rename_item = f'Rename-Item "{pasta_origem}{processo_txt}" "{pasta_origem}{processo_pc_xml}"'
                pyperclip.copy(rename_item)
                time.sleep(Base.time_sleep_1)
                Base.executar_hotkey_colar(self)
                move_pastas = f'move "{pasta_origem_f}" "{pasta_destino_f}"'
                pyperclip.copy(move_pastas)
                time.sleep(Base.time_sleep_1)
                Base.executar_hotkey_colar(self)
                Base.fechar_powershell(self)
                return processo_pc_xml
            elif processo_pc_txt != None and processo_pc_xml != None:
                Base.abrir_powershell(self)
                time.sleep(Base.time_sleep_1)
                rename_item = f'Rename-Item "{pasta_destino}{processo_pc_txt}" "{pasta_destino}{processo_pc_xml}"'
                pyperclip.copy(rename_item)
                time.sleep(Base.time_sleep_1)
                Base.executar_hotkey_colar(self)
                Base.fechar_powershell(self)
                return processo_pc_xml
            else:
                return processo_pc_xml
                    
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'trocar_txt_xml')

    def confirmar_dados_xml(self, lista_caminho=[], lista_caminho_pc=[], lista_arquivo_txt=[], lista_arquivo_xml=[]):
        try:
            lista_caminho_txt, lista_caminho_pc_txt, lista_caminho_xml, lista_caminho_pc_xml = XMLRoot.listar_caminho_arquivos_txt_xml(Base.self, lista_caminho, lista_caminho_pc, lista_arquivo_txt, lista_arquivo_xml)
            lista_arquivo_di_xml, lista_pasta_origem, lista_pasta_destino, lista_processo = XMLRoot.listar_arquivo_xml_ausente(Base.self, lista_caminho_pc_xml)
            lista_processo_txt, lista_processo_pc_txt, lista_processo_xml = XMLRoot.listar_arquivo_txt_xml_existentes(Base.self, lista_caminho_txt, lista_caminho_pc_txt, lista_caminho_xml)

            for processo in lista_processo:
                executar = XMLRoot.trocar_txt_xml(Base.self, processo, lista_processo_txt, lista_processo_pc_txt, lista_processo_xml, lista_arquivo_di_xml, lista_pasta_destino, lista_pasta_origem)
            return lista_caminho_pc_xml, lista_processo
        except:
            Base.alertar_error_except(self, 'classXMLRoot', 'confirmar_dados_xml')

