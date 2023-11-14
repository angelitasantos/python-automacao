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

    def definir_variaveis(self):
        try:
            pasta_imp = f'{Files.tipo_sigla}-{Files.ref_cliente} - {Files.tipo_ref}-{Files.ref_empresa}-{AnoResult.ano_simples}'
            pasta_exp = f'{Files.tipo_ref}-{Files.ref_empresa}-{AnoResult.ano_simples} - {Files.tipo_sigla}-{Files.ref_cliente}'
            pasta = pasta_exp if Files.tipo_comex == 'E' else pasta_imp

            pasta_interna_imp = VarGerais.pasta_interna_imp
            pasta_interna_exp = VarGerais.pasta_interna_exp
            pasta_interna = pasta_interna_exp if Files.tipo_comex == 'E' else pasta_interna_imp

            caminho = Files.caminho_movto
            processo = caminho + pasta
            processo_pc = caminho + pasta + '\\' + pasta_interna

            file_imp_new = f'{VarRede.capa_base}{Files.tipo_modal_nome} {VarGerais.apelido} - {Files.tipo_sigla} - {Files.ref_cliente}.xlsx'
            file_exp_new = f'{VarRede.capa_base}Exportação {VarGerais.apelido} - {Files.tipo_sigla}{Files.ref_cliente}.xlsx'
            capa_novo = file_exp_new if Files.tipo_comex== 'E' else file_imp_new

            return caminho, pasta, pasta_interna, processo, processo_pc, Files.capa_modelo, capa_novo
        except:
            Base.alertar_error_except(self, 'classFiles', 'definir_variaveis')

    def abrir_pasta_modelo(self):
        try:
            Base.abrir_pasta(self, VarRede.caminho_modelo)
        except:
            Base.alertar_error_except(self, 'classFiles', 'abrir_pasta_modelo')
            

