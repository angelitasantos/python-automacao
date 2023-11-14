#----------------------------------------------------------------------------------------------------------------
# DEFINIR O CAMINHO NA REDE


from base.base import *
from base.classProcedimento import *


class Rede:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.excel

    pastas_em_massa = 'SIM' if ProcResult.cod_proc != '12' else 'NÃO'
    arquivo_em_massa = 'SIM' if ProcResult.cod_proc != '23' else 'NÃO'
    pasta_modelo = 'SIM' if ProcResult.cod_proc != '33' else 'NÃO'
    excel_em_massa = 'SIM' if ProcResult.cod_proc != '34' else 'NÃO'
    pasta_comex = 'SIM' if ProcResult.cod_proc != '35' else 'NÃO'
    auditoria = 'SIM' if ProcResult.procedimento != 'AUDITORIA' else 'NÃO'
    proc_com_modal = pastas_em_massa == 'SIM' and pasta_modelo == 'SIM' and excel_em_massa == 'SIM' and pasta_comex == 'SIM' and arquivo_em_massa == 'SIM' and auditoria == 'SIM'

    def escolher_tipo_comex(self):
        try:
            if Ano.pesquisar_tipo_processo(self) == 'completo' and ProcResult.procedimento != Proc.procedimento4:
                texto = 'Escolha uma Opção ...'
                titulo = 'OPÇÃO'
                botoes = [ 'IMPORTAÇÃO', 'EXPORTAÇÃO' ]
                tipo_comex_nome = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                tipo_comex = 'E' if tipo_comex_nome == 'EXPORTAÇÃO' else 'I' if tipo_comex_nome == 'IMPORTAÇÃO' else 'Z'
                return tipo_comex, tipo_comex_nome
            
            elif VarGerais.comex == 'IMPORTAÇÃO':
                tipo_comex = 'I'
                tipo_comex_nome = 'IMPORTAÇÃO'
                return tipo_comex, tipo_comex_nome
            
            elif VarGerais.comex == 'EXPORTAÇÃO':
                tipo_comex = 'E'
                tipo_comex_nome = 'EXPORTAÇÃO'
                return tipo_comex, tipo_comex_nome
        except:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_comex')

    def escolher_tipo_movto(self, procedimento, tipo_comex):
        try:
            if Ano.pesquisar_tipo_processo(self) == 'completo' and ProcResult.procedimento != Proc.procedimento4:
                if procedimento == 'SIM' and AnoResult.historico_ano == "SIM" and tipo_comex != 'E':
                    tipo_movto = ''
                    return tipo_movto
                else:
                    texto = 'Escolha uma Opção ...'
                    titulo = 'OPÇÃO'
                    botoes = [ 'DESEMBARAÇO', 'PRE ENTRY' ]
                    tipo_movto_nome = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                    tipo_movto = 'PRE ENTRY' if tipo_movto_nome == 'PRE ENTRY' else 'DESEMBARAÇO' if tipo_movto_nome == 'DESEMBARAÇO' else 'Z'
                    return tipo_movto
                
            elif VarGerais.movto == 'DESEMBARAÇO':
                tipo_movto = 'DESEMBARAÇO'
                return tipo_movto
            
            elif VarGerais.movto == 'PRE_ENTRY':
                tipo_movto = 'PRE ENTRY'
                return tipo_movto
        except:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_movto')

    def escolher_tipo_modal(self):
        try:
            if Rede.proc_com_modal and ProcResult.procedimento != Proc.procedimento4:
                texto = 'Escolha uma Opção ...'
                titulo = 'OPÇÃO'
                botoes = [ 'AÉREA', 'MARÍTIMA', 'RODOVIÁRIA' ]
                tipo_modal_nome = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                tipo_modal = 'R' if tipo_modal_nome == 'RODOVIÁRIA' else 'M' if tipo_modal_nome == 'MARÍTIMA' else 'A' if tipo_modal_nome == 'AÉREA' else 'Z'
                tipo_modal_nome = VarRede.modal_rodoviario if tipo_modal_nome == 'RODOVIÁRIA' else VarRede.modal_maritimo if tipo_modal_nome == 'MARÍTIMA' else VarRede.modal_aereo if tipo_modal_nome == 'AÉREA' else 'Z'
                return tipo_modal, tipo_modal_nome
            
            elif ProcResult.procedimento == Proc.procedimento4:
                tipo_modal = 'Z'
                tipo_modal_nome = 'Z'
                return tipo_modal, tipo_modal_nome
            
            else:
                tipo_modal = 'Z'
                tipo_modal_nome = 'Z'
                return tipo_modal, tipo_modal_nome
        except:
            Base.alertar_error_except(self, 'classRede', 'escolher_tipo_modal')

    def escolher_caminho_comex(self, tipo_comex):
        try:
            caminho_comex_exp = VarRede.caminho_rede + VarRede.caminho_exp
            caminho_comex_imp = VarRede.caminho_rede + VarRede.caminho_imp
            caminho_comex = caminho_comex_imp if tipo_comex == 'I' else caminho_comex_exp if tipo_comex == 'E' else ''
            return caminho_comex
        except:
            Base.alertar_error_except(self, 'classRede', 'escolher_caminho_comex')



