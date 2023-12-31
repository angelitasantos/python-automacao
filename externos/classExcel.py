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

    def confirma_atualizacao_capa(self):
        try:
            if ProcResult.cod_proc == '21':
                texto = 'Confirma a atualização dos dados da DI(xml) na planilha ?'
                confirma_atualizacao = Base.confirmar_atualizacao(self, texto)
            elif ProcResult.cod_proc == '22':
                texto = 'Confirma a atualização dos dados da SAUDE na planilha ?'
                confirma_atualizacao = Base.confirmar_atualizacao(self, texto)
            elif ProcResult.cod_proc == '23':
                texto = 'Confirma a atualização dos dados EM MASSA das DIs(xml) ?'
                confirma_atualizacao = Base.confirmar_atualizacao(self, texto)
            return confirma_atualizacao
        except:
            Base.alertar_error_except(self, 'classExcel', 'confirma_atualizacao_capa')

    def existe_arquivos_capa_xml(self, indice, caminho=[], arquivo=[], arquivo_xml=[]):
        existe_arquivo_capa, arquivo_capa = Base.pesquisar_existe_arquivo(Base.self, caminho[indice], arquivo[indice])
        existe_arquivo_xml, caminho_arquivo_xml = Base.pesquisar_existe_arquivo(Base.self, caminho[indice], arquivo_xml[indice])

        if not existe_arquivo_capa or not existe_arquivo_xml:
            mensagem = f'Arquivos:\n\n{arquivo_capa}\n\ne/ou\n\n{caminho_arquivo_xml}\n\nNão encontrados. Processo não atualizado !!!'
            Base.alertar_pyautogui(self, mensagem)
            time.sleep(Base.time_sleep_1)
            return False

        elif existe_arquivo_capa and existe_arquivo_xml:
            return True

    def atualizar_planilha_xml(self, indice, arquivo=[]):
        try:
            existe_arquivos = Excel.existe_arquivos_capa_xml(self, indice, XMLRootResult.lista_caminho_pc, XMLRootResult.lista_arquivo_capa, XMLRootResult.lista_arquivo_xml)
            if existe_arquivos:
                while VarGerais.tentativas <= VarGerais.total_tentativas:
                    try:
                        if CliResult.valida_cliente:
                            lista_caminho_pc = XMLRootResult.lista_caminho_pc
                            for indice, root in enumerate(XMLRootResult.lista_processos):
                                if root not in lista_caminho_pc:
                                    Excel.atualizar_dados_planilha(Base.self, indice, lista_caminho_pc, XMLRootResult.lista_arquivo_capa)
                                    lista_caminho_pc.append(root)
                                    mensagem = f'PLANILHA:\n\n{arquivo[indice]}\n\nATUALIZADA COM SUCESSO !!!'
                                    Base.alertar_pyautogui(self, mensagem)
                    except:
                        tentativas_validas = VarGerais.total_tentativas - VarGerais.tentativas
                        mensagem = f'PLANILHA ABERTA !!!\nVocê tem {tentativas_validas} tentativa(s) para fechá-la!!!\nA planilha não foi atualizada !!!'
                        Base.alertar_pyautogui(self, mensagem)
                    time.sleep(1)
                    VarGerais.tentativas += 1            
        except:
            Base.alertar_error_except(self, 'classExcel', 'atualizar_planilha_xml')


