#----------------------------------------------------------------------------------------------------------------
# ATUALIZAR AS INFORMAÇÕES DO ARQUIVO XML (DI) NA PLANILHA DE EXCEL


from externos.classXMLExtrair import *


class Excel:

    def __init__(self, excel):
        self.excel = excel

    def __repr__(self):
        return self.excel
    
    lista_root = XMLExtResult.definir_variaveis_extrair_xml(Base.self)

    def extrair_todos_dados_xml(self, lista_root):
        if ProcResult.cod_proc == '21' or ProcResult.cod_proc == '23':
            lista_dados_gerais = []
            lista_dados_adicoes = []
            lista_conhecimentos = []
            lista_qtd_faturas = []
            lista_faturas = []
            for indice, root in enumerate(lista_root):
                dados_gerais = XMLExtrair.extrair_dados_gerais(Base.self, root, indice)
                lista_dados_gerais.append(dados_gerais)
                dados_adicoes = XMLExtrair.extrair_dados_adicoes(Base.self, indice, XMLRootResult.lista_caminho_pc, XMLRootResult.lista_arquivo_xml)
                lista_dados_adicoes.append(dados_adicoes)
                conhecimentos = XMLExtrair.extrair_dados_conhecimento(Base.self, indice, XMLRootResult.lista_caminho_pc, XMLRootResult.lista_arquivo_xml)
                lista_conhecimentos.append(conhecimentos)
                qtd_faturas, faturas = XMLExtrair.extrair_dados_faturas(Base.self, indice, XMLRootResult.lista_caminho_pc, XMLRootResult.lista_arquivo_xml)
                lista_qtd_faturas.append(qtd_faturas)
                lista_faturas.append(faturas)
        return lista_dados_gerais, lista_dados_adicoes, lista_conhecimentos, lista_qtd_faturas, lista_faturas
    



    