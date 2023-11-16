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


            