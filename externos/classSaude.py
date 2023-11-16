#----------------------------------------------------------------------------------------------------------------
# RETIRAR AS INFORMAÇÕES DO ARQUIVO SAUDE (EXCEL)


from externos.classPDF import *


class Saude:

    def __init__(self, financeiro):
        self.financeiro = financeiro

    def __repr__(self):
        return self.financeiro
    
    if CliResult.valida_cliente:
        if Rede.proc_com_modal or CliResult.dados_lista[8] == None: 
            processo = int(CliResult.dados_lista[1] if CliResult.valida_cliente else 0)
            ref_empresa = '' if FilesResult.valida_files == False else CliResult.dados_lista[1]

    def extrair_dados(self, df, nome_banco):
        try:
            df.NF = df.NF.fillna('', inplace=False)
            df.Credito = df.Credito.fillna('', inplace=False)
            df.Debito = df.Debito.fillna('', inplace=False)

            df['Data'] = pd.to_datetime(df.Data)
            df = df.sort_values(by='Data')

            df_filtrado = df[df['Numero'] == str(Saude.processo)]
            new_df = df_filtrado.assign(Banco = nome_banco)
            return new_df
        except:
            Base.alertar_error_except(self, 'classSaude', 'extrair_dados')
    