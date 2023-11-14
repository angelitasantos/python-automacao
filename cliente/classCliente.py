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

    def digitar_ref_empresa(self):
        try:
            texto = 'Digite o Número Ref. ' + VarGerais.empresa + ' ...'
            titulo = 'INFORME'
            padrao = ''
            ref_empresa = Base.digitar_pyautogui(self, texto, titulo, padrao)
            while ref_empresa == '':
                ref_empresa = Base.digitar_pyautogui(self, texto, titulo, padrao)
            return ref_empresa
        except:
            Base.alertar_error_except(self, 'classCliente', 'digitar_ref_empresa')

    def escolher_sigla_comex(self, tipo_comex):
        try:
            if Rede.proc_com_modal:
                ref_filial_processo = VarGerais.filiais_exp if tipo_comex == 'E' else VarGerais.filiais_imp

                if VarGerais.ref_filial == []:
                    texto = 'Escolha a Filial ' + VarGerais.cliente + ' ...'
                    titulo = 'OPÇÃO'
                    botoes = [ item for item in VarGerais.filiais_nomes ]
                    filial = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                    if filial != None:
                        sigla_comex_index = VarGerais.filiais_nomes.index(filial)
                        sigla_comex = ref_filial_processo[sigla_comex_index]
                        return sigla_comex, sigla_comex_index
                    else:
                        sigla_comex = filial = 'Z'
                        sigla_comex_index = 0
                        return sigla_comex, sigla_comex_index 
                else:
                    if tipo_comex == 'I':
                        filial = VarGerais.filiais_nomes[0]
                        sigla_comex = VarGerais.filiais_imp[0]
                        sigla_comex_index = VarGerais.filiais_imp.index(sigla_comex)
                        return sigla_comex, sigla_comex_index
                    
                    elif tipo_comex == 'E':
                        filial = VarGerais.filiais_nomes[0]
                        sigla_comex = VarGerais.filiais_exp[0]
                        sigla_comex_index = VarGerais.filiais_exp.index(sigla_comex)
                        return sigla_comex, sigla_comex_index
        except:
            Base.alertar_error_except(self, 'classCliente', 'escolher_sigla_comex')



            
    