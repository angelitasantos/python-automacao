#----------------------------------------------------------------------------------------------------------------
# DEFINIR O CAMINHO NA REDE


from base.base import *
from base.classProcedimento import *


class Rede:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.rede

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

    def escolher_caminho_movto(self, tipo_comex):
        try:
            caminho_comex = Rede.escolher_caminho_comex(self, tipo_comex)
            if tipo_comex == 'Z':
                time.sleep(Base.time_sleep_1)

            elif tipo_comex == 'E':
                tipo_movto = Rede.escolher_tipo_movto(self, ProcResult.historico_proc, tipo_comex)
                if tipo_movto == 'PRE ENTRY':
                    caminho_movto = caminho_comex + tipo_movto + '\\' + AnoResult.ano_completo + '\\'
                    return caminho_comex, caminho_movto, tipo_movto
                else:
                    caminho_movto = caminho_comex + AnoResult.ano_completo + '\\'
                    return caminho_comex, caminho_movto, tipo_movto

            elif tipo_comex == 'I':
                tipo_movto = Rede.escolher_tipo_movto(self, ProcResult.historico_proc, tipo_comex)
                if ProcResult.historico_proc == 'SIM' and AnoResult.historico_ano == "SIM":
                    caminho_movto = caminho_comex + AnoResult.ano_completo + '\\'
                    return caminho_comex, caminho_movto, tipo_movto
                else:
                    caminho_movto = caminho_comex + str(AnoResult.ano_atual) + '\\' + tipo_movto + '\\'
                    return caminho_comex, caminho_movto, tipo_movto
        except:
           Base.alertar_error_except(self, 'classRede', 'escolher_caminho_movto')

class RedeResult:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.rede     

    def definir_variaveis_rede(self):
        try:
            if ProcResult.valida_proc:
                tipo_comex, tipo_comex_nome = Rede.escolher_tipo_comex(Base.self)
                if tipo_comex != 'Z':
                    caminho_comex, caminho_movto, tipo_movto = Rede.escolher_caminho_movto(self, tipo_comex)
                    if tipo_movto != 'Z' and Rede.proc_com_modal:
                        tipo_modal, tipo_modal_nome = Rede.escolher_tipo_modal(self)
                    else:
                        tipo_modal = tipo_modal_nome = 'Z'
                else:
                    tipo_comex = tipo_comex_nome = tipo_movto = tipo_modal = tipo_modal_nome = caminho_comex = caminho_movto = 'Z'
            else:
                tipo_comex = tipo_comex_nome = tipo_movto = tipo_modal = tipo_modal_nome = caminho_comex = caminho_movto = 'Z'

            if Rede.proc_com_modal and tipo_comex != 'Z':
                valida_rede = tipo_comex != 'Z' and tipo_movto != 'Z' and tipo_modal != 'Z'
            else:
                valida_rede = tipo_comex != 'Z' and tipo_movto != 'Z'
            return valida_rede, tipo_comex, tipo_comex_nome, tipo_movto, tipo_modal, tipo_modal_nome, caminho_comex, caminho_movto
        except:
            Base.alertar_error_except(self, 'classRede', 'definir_variaveis_rede')

    valida_rede, tipo_comex, tipo_comex_nome, tipo_movto, tipo_modal, tipo_modal_nome, caminho_comex, caminho_movto = definir_variaveis_rede(Base.self)




