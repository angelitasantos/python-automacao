#----------------------------------------------------------------------------------------------------------------
# DEFINIR AS VARIÁVEIS


from base.base import *


class ExcelExterno:

    def __init__(self, excel):
        self.excel = excel
    
    def __repr__(self):
        return self.excel

    nome_arquivo = 'main_variaveis_senha_2023.xlsx'
    dir_arquivo = 'C:\\'
    caminho_arquivo = dir_arquivo + nome_arquivo
    existe_arquivo_main_variaveis, arquivo_main_variaveis = Base.pesquisar_existe_arquivo(Base.self, dir_arquivo, nome_arquivo)

    mensagem = f'O arquivo:\n{nome_arquivo}\nnão está salvo no local correto !!!\nSalve-o corretamente e refaça o procedimento !!!'
    
    if not existe_arquivo_main_variaveis:
        Base.alertar_pyautogui(Base.self, mensagem)

    else:
        workbook = load_workbook(caminho_arquivo, data_only = True)
        var_gerais = workbook['var_gerais']
        var_rede = workbook['var_rede']
        var_saude = workbook['var_saude']
        var_auditoria = workbook['var_auditoria']
        listas = workbook['listas']
        m_row = listas.max_row

    def listar_dados(self, m_row, listas, coluna):
        exportados = []
        for i in range(2, m_row + 1):
            cell_obj = listas.cell(row = i, column = coluna)
            exportados.append(cell_obj.value)
        return exportados

class VarGerais:

    def __init__(self, variaveis_geral):
        self.variaveis_geral = variaveis_geral

    def __repr__(self):
        return self.variaveis_geral
    
    try:
        dir_rede = ExcelExterno.var_gerais['C3'].value
        dir_financeiro = ExcelExterno.var_gerais['C4'].value
        grupo = ExcelExterno.var_gerais['C5'].value
        lista_empresas =    [
                                'EMPRESA 1',
                                'EMPRESA 2',
                                'EMPRESA 3'
                            ]
        empresa = ExcelExterno.var_gerais['C6'].value
        cliente = ExcelExterno.var_gerais['C7'].value
        apelido = ExcelExterno.var_gerais['C8'].value

        filiais_nomes = ExcelExterno.listar_dados(Base.self, ExcelExterno.m_row, ExcelExterno.listas, 2)
        filiais_imp = ExcelExterno.listar_dados(Base.self, ExcelExterno.m_row, ExcelExterno.listas, 3)
        filiais_exp = ExcelExterno.listar_dados(Base.self, ExcelExterno.m_row, ExcelExterno.listas, 4)
        ref_filial = []
        ref_interna_imp = ExcelExterno.listar_dados(Base.self, ExcelExterno.m_row, ExcelExterno.listas, 5)
        ref_interna_exp = ExcelExterno.listar_dados(Base.self, ExcelExterno.m_row, ExcelExterno.listas, 6)

        pasta_interna_imp = ExcelExterno.var_gerais['C9'].value
        pasta_interna_exp = ExcelExterno.var_gerais['C10'].value

        total_tentativas = int(ExcelExterno.var_gerais['C11'].value)
        tentativas = int(ExcelExterno.var_gerais['C12'].value)

        lista_processos =   [
                                'auditoria',
                                'importação-desembaraço',
                                'importação-pre-entry',
                                'exportação-desembaraço',
                                'exportação-pre-entry',
                                'importação-histórico',
                                'exportação-histórico',
                                'completo'
                            ]
        processo = ExcelExterno.var_gerais['C13'].value
        comex = ExcelExterno.var_gerais['C14'].value
        movto = ExcelExterno.var_gerais['C15'].value
    except:
        Base.alertar_error_except(Base.self, 'main', 'VarGerais')




