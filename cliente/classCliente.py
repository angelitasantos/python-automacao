#----------------------------------------------------------------------------------------------------------------
# DEFINIR OS DADOS DO CLIENTE / PROCESSO


from cliente.classRede import *


class Cliente:

    def __init__(self, cliente):
        self.cliente = cliente

    def __repr__(self):
        return self.cliente
    
    if ProcResult.valida_proc and RedeResult.tipo_comex != 'Z':
        tipo_sigla = VarGerais.filiais_exp if RedeResult.tipo_comex == 'E' else VarGerais.filiais_imp
        ref_sigla = VarGerais.ref_filial if VarGerais.ref_filial != [] else tipo_sigla

    def digitar_ref_cliente(self):
        try:
            texto = 'Digite o Número Ref. ' + VarGerais.cliente + ' ...'
            titulo = 'INFORME'
            padrao = ''
            ref_cliente = Base.digitar_pyautogui(self, texto, titulo, padrao)
            while ref_cliente == '':
                ref_cliente = Base.digitar_pyautogui(self, texto, titulo, padrao)
            return ref_cliente
        except:
            Base.alertar_error_except(self, 'classCliente', 'digitar_ref_cliente')



            
    