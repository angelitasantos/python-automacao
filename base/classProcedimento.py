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

    def escolher_subprocedimento_criar_pastas(self, procedimento):
        cod_proc = '1' if procedimento == Proc.procedimento1 else 9
        subproc11 = 'PROCESSO INDIVIDUAL'
        subproc12 = 'PROCESSOS EM MASSA'
        try:
            if cod_proc == '1':
                texto = 'Como deseja criar o(s) processo(s) ?'
                titulo = 'OPÇÃO'
                botoes = [ subproc11, subproc12, 'VOLTAR' ]
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                cod_subproc = cod_proc + '1' if subproc == subproc11 else cod_proc + '2' if subproc == subproc12 else 9
                return cod_subproc
        except:
            Base.alertar_error_except(self, 'classProcedimento', 'escolher_subprocedimento_criar_pastas')

    def escolher_subprocedimento_atualizar(self, procedimento):
        cod_proc = '2' if procedimento == Proc.procedimento2 else 9
        subproc21 = 'DADOS DI (XML)'
        subproc22 = 'DADOS SAUDE'
        subproc23 = 'DI (XML) EM MASSA'
        try:
            if cod_proc == '2':
                texto = 'O que deseja atualizar ?'
                titulo = 'OPÇÃO'
                botoes = [ subproc21, subproc22, subproc23, 'VOLTAR' ]
                subproc = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                cod_subproc = cod_proc + '1' if subproc == subproc21 else cod_proc + '2' if subproc == subproc22 else cod_proc + '3' if subproc == subproc23 else 9
                #anunciar_construcao = Base.anunciar_em_construcao(self) if cod_subproc == '22' else cod_subproc
                #cod_subproc = 9 if anunciar_construcao == 'OK' else cod_subproc
                return cod_subproc
        except:
            Base.alertar_error_except(self, 'classProcedimento', 'escolher_subprocedimento_atualizar')

