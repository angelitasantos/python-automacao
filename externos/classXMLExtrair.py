#----------------------------------------------------------------------------------------------------------------
# RETIRAR AS INFORMAÇÕES DO ARQUIVO XML (DI)


from externos.classXMLRoot import *


class XMLExtrair:

    def __init__(self, xml):
        self.xml = xml
    
    def __repr__(self):
        return self.xml
    
    def extrair_dados_gerais(self, root, indice):
        try:            
            for child in list(root):
                numeroDI = XMLRoot.get_text(self, child, 'numeroDI')
                dataRegistro = XMLRoot.get_text(self, child, 'dataRegistro')
                viaTransporteNome = XMLRoot.get_text(self, child, 'viaTransporteNome')
                totalAdicoes = XMLRoot.get_text(self, child, 'totalAdicoes')
                sequencialRetificacao = XMLRoot.get_text(self, child, 'sequencialRetificacao')
                Numero = XMLRoot.get_text(self, child, 'importadorNumero')
                imp_nome = XMLRoot.get_text(self, child, 'importadorNome')
                imp_cidade = XMLRoot.get_text(self, child, 'importadorEnderecoMunicipio')
                imp_uf = XMLRoot.get_text(self, child, 'importadorEnderecoUf')
                dta = XMLRoot.get_text(self, child, 'documentoChegadaCargaNumero')

                data_atual = AnoResult.data_atual

                if ProcResult.cod_proc == '23':
                    sigla_empresa = XMLRootResult.lista_sigla_empresa[indice]
                    num_empresa = XMLRootResult.lista_num_empresa[indice]
                    sigla_cliente = XMLRootResult.lista_sigla_cliente[indice]
                    num_cliente = XMLRootResult.lista_num_cliente[indice]
                else:
                    sigla_empresa = CliResult.dados_lista[10]
                    num_empresa = CliResult.dados_lista[1]
                    sigla_cliente = CliResult.dados_lista[8]
                    num_cliente = CliResult.dados_lista[0]

                Numero_Len = len(Numero)
                cnpj = Numero[0:2] + '.' + Numero[2:5] + '.' + Numero[5:8] + '/' + Numero[8:12] + '-' + Numero[-2:]
                di_Len = len(numeroDI)
                num_DI = numeroDI[0] + numeroDI[1] + '/' + numeroDI[2:9] + '-' + numeroDI[-1]
                dta_Len = len(dta)
                num_DTA = dta[0] + dta[1] + '/' + dta[2:9] + '-' + dta[-1]
                modal = viaTransporteNome
                seq_retif = sequencialRetificacao
                conf_retif = 'Sim' if seq_retif != '00' else 'Não'

            dados_gerais =  [
                                cnpj,
                                imp_cidade,
                                imp_uf,
                                imp_nome,
                                AnoResult.ano_completo,
                                sigla_empresa,
                                num_empresa,
                                sigla_cliente,
                                num_cliente,
                                modal,
                                seq_retif,
                                num_DI,
                                num_DTA,
                                conf_retif,
                                data_atual
                            ]
            return dados_gerais
        except:
            Base.alertar_error_except(self, 'classXMLExtrair', 'extrair_dados_gerais')

    def extrair_dados_adicoes(self, indice, caminho=[], arquivo=[]):
        try:
            adicoes = []
            caminho_xml = caminho[indice] + arquivo[indice]
            arquivos = [caminho_xml]
            for arquivo in arquivos:
                prstree = ETree.parse(arquivo)
                root = prstree.getroot()

                regimes = []
                exportadores = []
                cod_fund_legais = []
                fund_legais = []
                todas_LI = []
                
                for child in root.iter('adicao'):
                    numDI = XMLRoot.get_text(self, child, 'numeroDI')
                    numeroLI = XMLRoot.get_text(self, child, 'numeroLI')
                    adicao = XMLRoot.get_text(self, child, 'numeroAdicao')
                    atipico = XMLRoot.get_text(self, child, 'iiRegimeTributacaoNome')
                    exportador = XMLRoot.get_text(self, child, 'fornecedorNome')
                    cod_fund_legal = XMLRoot.get_text(self, child, 'iiFundamentoLegalCodigo')
                    fund_legal_existe = []
                    for infoss in root.iterfind('declaracaoImportacao/adicao/iiFundamentoLegalNome'):
                        fund_legal_existe.append(infoss.text)
                    fund_legal = 'SEM FUNDAMENTO LEGAL' if fund_legal_existe == [] else XMLRoot.get_text(self, child, 'iiFundamentoLegalNome')

                    li_Len = len(numeroLI)
                    num_LI = numeroLI[0] + numeroLI[1] + '/' + numeroLI[2:9] + '-' + numeroLI[-1]
                
                    regimes.append(atipico)
                    exportadores.append(exportador)
                    cod_fund_legais.append(cod_fund_legal)
                    fund_legais.append(fund_legal)
                    todas_LI.append(num_LI)   

                qtd_regime, lista_regime, boolean = XMLRoot.get_lista(self, regimes)
                qtd_exp, lista_exp, boolean = XMLRoot.get_lista(self, exportadores)
                qtd_Tot_LI, lista_LI, boolean_LI = XMLRoot.get_lista(self, todas_LI)
                qtd_cod_fund_legal, lista_cod_fund_legal, boolean = XMLRoot.get_lista(self, cod_fund_legais)
                qtd_fund_legal, lista_fund_legal, boolean = XMLRoot.get_lista(self, fund_legais)

                trib_atipica = 'Sim' if 'SUSPENSAO' in lista_regime else 'Não'
                drawback = 'Sim' if '16' in lista_cod_fund_legal else 'Não'
                
            dados_adicoes =  [   
                                qtd_exp,
                                lista_exp,
                                qtd_Tot_LI,
                                lista_LI,
                                boolean_LI,
                                trib_atipica,
                                lista_cod_fund_legal,
                                qtd_fund_legal,
                                lista_fund_legal,
                                drawback
                            ]
            return dados_adicoes
        except:
            Base.alertar_error_except(self, 'classXMLExtrair', 'extrair_dados_adicoes')

    def extrair_dados_conhecimento(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_xml = caminho[indice] + arquivo[indice]
            xmldata = caminho_xml
            prstree = ETree.parse(xmldata)
            root = prstree.getroot()

            lista_conhecimento = []
            all_conhecimentos = []
            cod_conhecimento = '28'

            for child in root.iter('documentoInstrucaoDespacho'):
                cod = XMLRoot.get_text(self, child, 'codigoTipoDocumentoDespacho')
                nome = XMLRoot.get_text(self, child, 'nomeDocumentoDespacho')
                numero = XMLRoot.get_text(self, child, 'numeroDocumentoDespacho')
                if child.tag == 'documentoInstrucaoDespacho':
                    for attr in child:
                        if attr.text == cod_conhecimento:
                            for child in child:
                                break
                                
                            lista_conhecimento = numero.replace(' ', '')
                            all_conhecimentos.append(lista_conhecimento)
            
            xmlToDf3 = pd.DataFrame(all_conhecimentos, columns=['Numero'])
            conhecimentos = XMLRoot.get_replace_caracteres(self, all_conhecimentos)

            return conhecimentos
        except:
            Base.alertar_error_except(self, 'classXMLExtrair', 'extrair_dados_conhecimento')

    def extrair_dados_faturas(self, indice, caminho=[], arquivo=[]):
        try:
            caminho_xml = caminho[indice] + arquivo[indice]
            xmldata = caminho_xml
            prstree = ETree.parse(xmldata)
            root = prstree.getroot()

            lista_fatura = []
            all_faturas = []
            cod_fatura = '01'

            for child in root.iter('documentoInstrucaoDespacho'):
                cod = XMLRoot.get_text(self, child, 'codigoTipoDocumentoDespacho')
                nome = XMLRoot.get_text(self, child, 'nomeDocumentoDespacho')
                numero = XMLRoot.get_text(self, child, 'numeroDocumentoDespacho')
                if child.tag == 'documentoInstrucaoDespacho':
                    for attr in child:
                        if attr.text == cod_fatura:
                            for child in child:
                                break
                                
                            lista_fatura = numero.replace(' ', '')
                            all_faturas.append(lista_fatura)

            xmlToDf4 = pd.DataFrame(all_faturas, columns=['Numero'])
            qtd_faturas = len(all_faturas)
            faturas = XMLRoot.get_replace_caracteres(self, all_faturas)

            return qtd_faturas, faturas
        except:
            Base.alertar_error_except(self, 'classXMLExtrair', 'extrair_dados_faturas')



            