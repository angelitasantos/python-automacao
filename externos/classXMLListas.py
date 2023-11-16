#----------------------------------------------------------------------------------------------------------------
# LISTA DE DADOS CLIENTE E EMPRESA ARQUIVO EM MASSA


from base.base import *
from cliente.classFiles import *


class XMLListas:

    def __init__(self, xml):
        self.xml = xml

    def __repr__(self):
        return self.xml
    
    lista_caminho = []
    lista_caminho_pc = []
    lista_arquivo_txt = []
    lista_arquivo_xml = []
    lista_sigla_pleno = []
    lista_num_pleno = []
    lista_sigla_progress = []
    lista_num_progress = []
    lista_arquivo_capa = []
    lista_capa_modelo = []

    def listar_caminhos_arquivo_em_massa(self):
        try:
            pasta_interna_imp = VarGerais.pasta_interna_imp
            pasta_interna_exp = VarGerais.pasta_interna_exp
            pasta_interna = pasta_interna_exp if RedeResult.tipo_comex == 'E' else pasta_interna_imp
            caminho_comex = Rede.escolher_caminho_comex(self, RedeResult.tipo_comex)
            caminho_movto = caminho_comex + AnoResult.ano_completo + '\\' + RedeResult.tipo_movto + '\\'

            existe_arquivo_capa, arquivo_capa_modelo = Base.pesquisar_existe_arquivo(Base.self, VarRede.caminho_modelo, VarRede.arquivo_em_massa)
            caminho_capa_modelo = VarRede.caminho_modelo + VarRede.arquivo_em_massa
            diretorio = caminho_movto
            subdiretorio = '\\' + pasta_interna
            return existe_arquivo_capa, caminho_capa_modelo, diretorio, subdiretorio
        except:
            Base.alertar_error_except(self, 'classXMLListas', 'listar_caminhos_arquivo_em_massa')

    def criar_listas_em_massa(self, caminho_capa_modelo, diretorio, subdiretorio):
        try:
            wb_obj = openpyxl.load_workbook(caminho_capa_modelo, data_only = True)
            sheet_obj = wb_obj['Planilha1']
            qtd = sheet_obj.max_row

            for i in range(2, qtd + 1):
                REFPROGRESS = sheet_obj.cell(row = i, column = 1).value
                REFPLENO = sheet_obj.cell(row = i, column = 2).value
                MODAL = str(sheet_obj.cell(row = i, column = 3).value)
                NUMPROGRESS = str(sheet_obj.cell(row = i, column = 4).value)
                SIGLAPROGRESS = str(sheet_obj.cell(row = i, column = 5).value)
                NUMPLENO = str(sheet_obj.cell(row = i, column = 6).value)
                SIGLAPLENO = str(sheet_obj.cell(row = i, column = 7).value)

                arquivo_modelo = f'{VarRede.capa_base}{MODAL} {VarGerais.apelido} - 0000.xlsx'
                caminho_modelo = arquivo_modelo
                XMLListas.lista_capa_modelo.append(caminho_modelo)

                arquivo_txt = f'{NUMPROGRESS} - DI.txt'
                XMLListas.lista_arquivo_txt.append(arquivo_txt)
                arquivo_xml = f'{NUMPROGRESS} - DI.xml'
                XMLListas.lista_arquivo_xml.append(arquivo_xml)
                XMLListas.lista_sigla_pleno.append(SIGLAPLENO)
                XMLListas.lista_num_pleno.append(NUMPLENO)
                XMLListas.lista_sigla_progress.append(SIGLAPROGRESS)
                XMLListas.lista_num_progress.append(NUMPROGRESS)

                if REFPROGRESS is not None:
                    arquivo_capa = f'{VarRede.capa_base}{MODAL} {VarGerais.apelido} - {SIGLAPROGRESS} - {NUMPROGRESS}.xlsx'
                    XMLListas.lista_arquivo_capa.append(arquivo_capa)
                    caminho = f'{diretorio}{REFPROGRESS} - {REFPLENO}\\'
                    XMLListas.lista_caminho.append(caminho)
                    caminho_pc = f'{diretorio}{REFPROGRESS} - {REFPLENO}{subdiretorio}\\'
                    XMLListas.lista_caminho_pc.append(caminho_pc)

            listas_caminho_em_massa =   [
                                            XMLListas.lista_caminho,
                                            XMLListas.lista_caminho_pc,
                                            XMLListas.lista_arquivo_txt,
                                            XMLListas.lista_arquivo_xml,
                                            XMLListas.lista_sigla_pleno,
                                            XMLListas.lista_num_pleno,
                                            XMLListas.lista_sigla_progress,
                                            XMLListas.lista_num_progress,
                                            XMLListas.lista_arquivo_capa,
                                            XMLListas.lista_capa_modelo
                                        ]
            return listas_caminho_em_massa
        except:
            Base.alertar_error_except(self, 'classXMLListas', 'criar_listas_em_massa')

