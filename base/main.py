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




