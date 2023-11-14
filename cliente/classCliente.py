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

    def escolher_ref_interna(self, tipo_comex, tipo_sigla_index):
        try:
            ref_interna_processo = VarGerais.ref_interna_exp if tipo_comex == 'E' else VarGerais.ref_interna_imp
            if VarGerais.ref_filial == []:
                ref_interna = ref_interna_processo[tipo_sigla_index]
                return ref_interna
            else:
                ref_interna_imp = VarGerais.ref_interna_imp[tipo_sigla_index]
                ref_interna_exp = VarGerais.ref_interna_exp[tipo_sigla_index]
                ref_interna = ref_interna_imp if tipo_comex == 'I' else ref_interna_exp if tipo_comex == 'E' else ''
                return ref_interna
        except:
            Base.alertar_error_except(self, 'classCliente', 'escolher_ref_interna')

    def retornar_informacoes_cliente(self):
        try:
            sigla_comex, sigla_comex_index = Cliente.escolher_sigla_comex(self, RedeResult.tipo_comex)
            ref_interna = Cliente.escolher_ref_interna(self, RedeResult.tipo_comex, sigla_comex_index)
            if sigla_comex != 'Z':
                ref_cliente = Cliente.digitar_ref_cliente(self)
                ref_empresa = Cliente.digitar_ref_empresa(self)
            else:
                ref_cliente = ''
                ref_empresa = ''
            return ref_cliente, ref_empresa, sigla_comex, sigla_comex_index, ref_interna
        except:
            Base.alertar_error_except(self, 'classCliente', 'retornar_informacoes_cliente')

    def retornar_dados(self):
        try:
            if Rede.proc_com_modal:
                ref_cliente, ref_empresa, sigla_comex, sigla_comex_index, ref_interna = Cliente.retornar_informacoes_cliente(self)
                lista_dados_ref =   [   
                                        ref_cliente, ref_empresa,
                                        RedeResult.tipo_comex,
                                        RedeResult.tipo_comex_nome,
                                        RedeResult.tipo_movto,
                                        RedeResult.tipo_modal,
                                        RedeResult.tipo_modal_nome,
                                        RedeResult.caminho_movto,
                                        sigla_comex, sigla_comex_index, ref_interna
                                    ]
                return lista_dados_ref
            else:
                ref_cliente = ref_empresa = sigla_comex = sigla_comex_index = ref_interna = 'Z'
                lista_dados_ref =   [   
                                        ref_cliente, ref_empresa,
                                        RedeResult.tipo_comex,
                                        RedeResult.tipo_comex_nome,
                                        RedeResult.tipo_movto,
                                        RedeResult.tipo_modal,
                                        RedeResult.tipo_modal_nome,
                                        RedeResult.caminho_movto,
                                        sigla_comex, sigla_comex_index, ref_interna
                                    ]
                return lista_dados_ref
        except:
            Base.alertar_error_except(self, 'classCliente', 'retornar_dados')

    def apresentar_tela_dados(self, lista_dados_ref=[]):
        try:
            if lista_dados_ref[8] != 'Z':
                dados_digitados_cliente = f'Ref. {VarGerais.cliente}: {lista_dados_ref[0]}'
                dados_digitados_empresa = f'Ref. {VarGerais.empresa}: {lista_dados_ref[1]}'
                dados_digitados_ref = f'{dados_digitados_cliente}\n{dados_digitados_empresa}'
                dados_digitados_tipo = f'Processo: {lista_dados_ref[2]} - {lista_dados_ref[3]}\nTipo: {lista_dados_ref[4]}'
                modal = f'Modal: {lista_dados_ref[6]}'
                caminho_rede = lista_dados_ref[7]
                caminho_processo = f'Caminho Rede: {caminho_rede}'

                texto = f'Confirma os dados digitados ?\n\n{dados_digitados_ref}\n\n{dados_digitados_tipo}\n{modal}\n\n{caminho_processo}'
                titulo = 'CONFIRMA'
                botoes = [ 'SIM', 'NÃO', 'CANCELAR' ]
                confirma_dados = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                return confirma_dados
        except:
            Base.alertar_error_except(self, 'classCliente', 'apresentar_tela_dados')

    def tentar_confirmar(self, confirma_dados_ref):
        try:
            if Rede.proc_com_modal:
                confirma_dados = confirma_dados_ref
                while VarGerais.tentativas <= VarGerais.total_tentativas and confirma_dados == 'NÃO':
                    var_dif = VarGerais.total_tentativas - VarGerais.tentativas
                    mensagem = f'Você tem {var_dif} tentativa(s) para corrigí-los!!!'
                    Base.alertar_pyautogui(self, mensagem)
                    tipo_comex, tipo_comex_nome = Rede.escolher_tipo_comex(self)

                    if tipo_comex != 'Z':
                        caminho_comex, caminho_movto, tipo_movto = Rede.escolher_caminho_movto(self, tipo_comex)
                        if tipo_movto != 'Z':
                            tipo_modal, tipo_modal_nome = Rede.escolher_tipo_modal(self)
                    else:
                        tipo_comex = tipo_comex_nome = tipo_movto = tipo_modal = tipo_modal_nome = caminho_comex = caminho_movto = 'Z'
                        
                    if tipo_comex != 'Z':
                        ref_cliente, ref_empresa, sigla_comex, sigla_comex_index, ref_interna = Cliente.retornar_informacoes_cliente(self)
                        lista_dados_conf =  [  
                                                ref_cliente, ref_empresa,
                                                tipo_comex, tipo_comex_nome, 
                                                tipo_movto, 
                                                tipo_modal, tipo_modal_nome, caminho_movto,
                                                sigla_comex, sigla_comex_index, ref_interna
                                            ]
                        confirma_dados = Cliente.apresentar_tela_dados(self, lista_dados_conf)
                    else:
                        confirma_dados = 'SIM'
                        lista_dados_conf = ['', '']
                    VarGerais.tentativas += 1

                    if confirma_dados == 'CANCELAR':
                        AnoResult.ano_processo = None
                        ProcResult.cod_proc = 0
                return confirma_dados, lista_dados_conf
        except:
            Base.alertar_error_except(self, 'classCliente', 'tentar_confirmar')

    def confirmar_dados(self):
        try:
            lista_dados_ref = Cliente.retornar_dados(self)
            if Rede.proc_com_modal:
                confirma_dados_ref = Cliente.apresentar_tela_dados(self, lista_dados_ref)

                if confirma_dados_ref == 'SIM':
                    AnoResult.ano_processo = AnoResult.ano_processo
                    ProcResult.cod_proc = ProcResult.cod_proc

                elif confirma_dados_ref == 'CANCELAR':
                    AnoResult.ano_processo = None
                    ProcResult.cod_proc = 0

                elif confirma_dados_ref == 'NÃO':
                    confirma = confirma_dados_ref
                    confirma_tentativa, lista_dados_tent = Cliente.tentar_confirmar(self, confirma)

                dados = lista_dados_tent if confirma_dados_ref == 'NÃO' else lista_dados_ref
                return dados
        except:
            Base.alertar_error_except(self, 'classCliente', 'confirmar_dados')



            
