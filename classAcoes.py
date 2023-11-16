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

    def escolher_proc_criar_pastas(self, cod_procedimento):
        try:
            if cod_procedimento == '11':
                if CliResult.valida_cliente:
                    existe_arquivo_capa, arquivo_capa = Base.pesquisar_existe_arquivo(Base.self, FilesResult.processo_pc, FilesResult.capa_novo)

                    if existe_arquivo_capa:
                        mensagem = 'O arquivo deste processo já foi criado anteriormente !!!'
                        Base.alertar_pyautogui(self, mensagem)
                        Files.abrir_pasta_processo(self, FilesResult.processo)
                    else:
                        mouse_listener = pynput.mouse.Listener(suppress = True)
                        mouse_listener.start()
                        Base.abrir_powershell(self)
                        Files.criar_nova_pasta(self, FilesResult.processo_pc)
                        Files.copiar_novo_arquivo(self, FilesResult.processo_pc, FilesResult.capa_novo)
                        Files.abrir_pasta_processo(self, FilesResult.processo)
                        mouse_listener.stop()

            elif cod_procedimento == '12':
                texto = 'Confirma a criação das pastas em massa ?'
                confirma_atualizacao = Base.confirmar_atualizacao(self, texto)
                mouse_listener = pynput.mouse.Listener(suppress = True)
                mouse_listener.start()
                EmMassaCapa.criar_pastas_em_massa(self, confirma_atualizacao)
                mouse_listener.stop()
        except:
            Base.alertar_error_except(self, 'classAcoes', 'escolher_proc_criar_pastas')

    def escolher_proc_atualizar_dados(self, cod_procedimento):
        try:
            if cod_procedimento == '21' and CliResult.valida_cliente and CliResult.valida_filial:
                if CliResult.valida_cliente:
                    for indice, root in enumerate(XMLRootResult.lista_processos):
                        mouse_listener = pynput.mouse.Listener(suppress = True)
                        mouse_listener.start()
                        Excel.atualizar_planilha_xml(Base.self, indice, XMLRootResult.lista_arquivo_capa)
                        mouse_listener.stop()

            elif cod_procedimento == '22':
                Saude.atualizar_planilha_saude(self)
                Files.abrir_arquivo_capa(self, FilesResult.processo_pc, FilesResult.capa_novo)

            elif cod_procedimento == '23':
                len_root = len(Excel.lista_root)
                len_processos = XMLRootResult.qtd_processos
                if len_root == len_processos:
                    if CliResult.valida_cliente:
                        for indice, root in enumerate(XMLRootResult.lista_processos):
                            mouse_listener = pynput.mouse.Listener(suppress = True)
                            mouse_listener.start()
                            Excel.atualizar_planilha_xml(Base.self, indice, XMLRootResult.lista_arquivo_capa)
                            mouse_listener.stop()
                else:
                    mensagem = 'Nem todos os arquivos de DI foram encontrados.\n\nNão foi possível atualizar os processos em massa !!!'
                    Base.alertar_pyautogui(self, mensagem)
        except:
            Base.alertar_error_except(self, 'classAcoes', 'escolher_proc_atualizar_dados')        
            
                   