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
                cnpj = Numero[0:2] + "." + Numero[2:5] + "." + Numero[5:8] + "/" + Numero[8:12] + '-' + Numero[-2:]
                di_Len = len(numeroDI)
                num_DI = numeroDI[0] + numeroDI[1] + "/" + numeroDI[2:9] + '-' + numeroDI[-1]
                dta_Len = len(dta)
                num_DTA = dta[0] + dta[1] + "/" + dta[2:9] + '-' + dta[-1]
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


