#----------------------------------------------------------------------------------------------------------------
# ESCOLHER O PROCEDIMENTO


from base.classAno import *


class Proc:

    def __init__(self, procedimento):
        self.procedimento = procedimento

    def __repr__(self):
        return self.ano

    procedimento1 = 'CRIAR PASTAS/ARQUIVO'
    procedimento2 = 'ATUALIZAR PLANILHA'
    procedimento3 = 'HISTÓRICO'
    procedimento4 = 'AUDITORIA'

    subproc31 = 'PASTA DO PROCESSO'
    subproc32 = 'CAPA DO PROCESSO'
    subproc33 = 'PASTA MODELOS'
    subproc34 = 'EXCEL EM MASSA'
    subproc35 = 'PASTA COMEX'

    subproc41 = 'EADI USIFAST'
    subproc42 = 'SANTOS BRASIL'
    subproc43 = 'BH AIRPORT'
    subproc44 = 'GRU AIRPORT'
    subproc45 = 'VCP AIRPORT'
    subproc46 = 'CWB'

    def escolher_procedimento(self, historico):
        try:
            texto = 'Qual o procedimento deseja executar ?'
            titulo = 'OPÇÃO'
            if (historico == 'SIM'):
                botoes = [ Proc.procedimento2, Proc.procedimento3, Proc.procedimento4, 'SAIR' ]
                procedimento = Base.confirmar_pyautogui(self, texto, titulo, botoes)
            elif (historico == 'NÃO'):
                botoes = [ Proc.procedimento2, Proc.procedimento1, Proc.procedimento3, Proc.procedimento4, 'SAIR' ]
                procedimento = Base.confirmar_pyautogui(self, texto, titulo, botoes)
            if procedimento == None:
                procedimento = 'SAIR'
                return procedimento
            else:
                return procedimento
        except:
            Base.alertar_error_except(self, 'classProcedimento', 'escolher_procedimento')



            
