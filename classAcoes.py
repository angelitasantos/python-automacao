#----------------------------------------------------------------------------------------------------------------
# ESCOLHER A AÇÃO A SER EXECUTADA


from base.base import *
from externos.classEmMassaXML import *


class Acoes:

    def __init__(self, acao):
        self.acao = acao

    def __repr__(self):
        return self.acao
    
    def escolher_procedimento(self, procedimento, cod_procedimento):
        try:
            if ProcResult.valida_proc:
                if procedimento == Proc.procedimento1:                    
                    Acoes.escolher_proc_criar_pastas(self, cod_procedimento)
                    Base.alertar_finalizado(self)

                elif procedimento == Proc.procedimento2:
                    confirma_atualizacao = Excel.confirma_atualizacao_capa(self)
                    if confirma_atualizacao == 'SIM': 
                        Acoes.escolher_proc_atualizar_dados(self, cod_procedimento)
                        Base.alertar_finalizado(self)
                    elif confirma_atualizacao == 'NÃO':
                        mensagem = 'Planilha Não Atualizada !!!'
                        Base.alertar_pyautogui(self, mensagem)
                        time.sleep(Base.time_sleep_1)

                elif procedimento == Proc.procedimento3:
                    Acoes.escolher_proc_historico(self, cod_procedimento)
                    Base.alertar_finalizado(self)

                elif procedimento == Proc.procedimento4:
                    Acoes.escolher_proc_auditoria(self, cod_procedimento)

                else:
                    time.sleep(Base.time_sleep_1)
        except:
            Base.alertar_error_except(self, 'classAcoes', 'escolher_procedimento')
