#----------------------------------------------------------------------------------------------------------------
# ESCOLHER O ARQUIVO DE MODELO


from cliente.classCliente import *


class Files:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.excel
    
    if CliResult.valida_cliente:
        ref_cliente = CliResult.dados_lista[0]
        ref_empresa = CliResult.dados_lista[1]
        tipo_comex = CliResult.dados_lista[2]
        tipo_comex_nome = CliResult.dados_lista[3]
        tipo_movto = CliResult.dados_lista[4]
        tipo_modal = CliResult.dados_lista[5]
        tipo_modal_nome = CliResult.dados_lista[6]
        caminho_movto = CliResult.dados_lista[7]
        tipo_sigla = CliResult.dados_lista[8]
        tipo_ref = CliResult.dados_lista[10]
        file_imp = f'{VarRede.capa_base}{tipo_modal_nome} {VarGerais.apelido} - 0000.xlsx'
        file_exp = f'{VarRede.capa_base}Exportação {VarGerais.apelido}0000.xlsx'
        capa_modelo = file_exp if tipo_comex == 'E' else file_imp
        