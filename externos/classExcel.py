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
    
    def atualizar_dados_planilha(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_capa = caminho[indice] + arquivo[indice]
            workbook = load_workbook(caminho_capa)
            sheet = workbook['CAPA']
            planilha_atualizada = sheet['C6'].value

            lista_dados_gerais, lista_dados_adicoes, lista_conhecimentos, lista_qtd_faturas, lista_faturas = Excel.extrair_todos_dados_xml(Base.self, Excel.lista_root)

            if planilha_atualizada == 'Não':
                # dados processo
                sheet['C2'] = lista_dados_gerais[indice][0]
                sheet['C3'] = lista_dados_gerais[indice][1]
                sheet['E3'] = lista_dados_gerais[indice][2]
                sheet['C4'] = lista_dados_gerais[indice][3]
                sheet['C7'] = AnoResult.ano_completo
                sheet['D8'] = lista_dados_gerais[indice][5]
                sheet['D9'] = lista_dados_gerais[indice][6]
                sheet['C10'] = lista_dados_gerais[indice][7]
                sheet['D10'] = lista_dados_gerais[indice][8]
                sheet['H7'] = lista_dados_gerais[indice][9]
                sheet['H8'] = lista_dados_gerais[indice][10]
                sheet['D13'] = lista_dados_gerais[indice][11]
                sheet['D22'] = lista_dados_gerais[indice][12]
                sheet['I8'] = lista_dados_gerais[indice][13]
                sheet['E2'] = lista_dados_gerais[indice][14]
                sheet['C6'] = 'Sim'
                sheet['E6'] = lista_dados_gerais[indice][14]
                
                # dados adições
                sheet['C5'] = lista_dados_adicoes[indice][0]
                sheet['D5'] = lista_dados_adicoes[indice][1]
                sheet['D15'] = lista_dados_adicoes[indice][2]
                sheet['E14'] = lista_dados_adicoes[indice][3]
                sheet['C14'] = lista_dados_adicoes[indice][4]
                sheet['I7'] = lista_dados_adicoes[indice][5]
                sheet['L21'] = lista_dados_adicoes[indice][6]
                sheet['M21'] = lista_dados_adicoes[indice][8]
                sheet['I9'] = lista_dados_adicoes[indice][9]

                # dados conhecimentos / faturas
                sheet['D12'] = lista_conhecimentos[indice]
                sheet['C17'] = lista_qtd_faturas[indice]
                sheet['D17'] = lista_faturas[indice]
                
                workbook.save(caminho_capa)
            else:
                workbook.save(caminho_capa)
        except:
            Base.alertar_error_except(self, 'classExcel', 'atualizar_dados_planilha')



