#----------------------------------------------------------------------------------------------------------------
# CRIAR PASTAS E GERAR ARQUIVOS MODELOS PARA NOVA EMPRESA


from base.main import *


class NovaEmpresa:

    def __init__(self, main):
        self.geral = main

    def __repr__(self):
        return self.main

    def criar_nova_empresa(self):
        try:
            if VarGerais.dir_rede == 'C:\\':
                criar_caminho = True
                return criar_caminho
            else:
                criar_caminho = False
                return criar_caminho
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_nova_empresa')

    def criar_novos_caminhos(self):
        try:
            Base.abrir_powershell(self)
            Base.executar_comando_cd(self, VarGerais.dir_rede)
            Base.executar_comando_mkdir(self, VarGerais.empresa)
            Base.executar_comando_cd(self, VarGerais.empresa)
            Base.executar_comando_mkdir(self, VarRede.pasta_arquivos_modelo)
            Base.executar_comando_mkdir(self, VarSaude.pasta_financeiro)
            Base.fechar_powershell(self)
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_novos_caminhos')

    def criar_pastas_internas(self):
        try:
            ano_atual = str(date.today().year)
            Base.abrir_powershell(self)
            Base.executar_comando_cd(self, VarGerais.dir_rede)
            Base.executar_comando_cd(self, VarGerais.empresa)
            auditoria_imp = VarAuditoria.caminho_auditoria_imp
            desembaraco_imp = VarRede.caminho_imp + ano_atual + '\\' + VarRede.caminho_desembaraco
            desembaraco_exp = VarRede.caminho_exp + ano_atual + '\\' + VarRede.caminho_desembaraco
            pre_entry_imp = VarRede.caminho_imp + ano_atual + '\\' + VarRede.caminho_pre_entry
            pre_entry_exp = VarRede.caminho_exp + ano_atual + '\\' + VarRede.caminho_pre_entry
            Base.executar_comando_mkdir(self, auditoria_imp)
            Base.executar_comando_mkdir(self, desembaraco_imp)
            Base.executar_comando_mkdir(self, desembaraco_exp)
            Base.executar_comando_mkdir(self, pre_entry_imp)
            Base.executar_comando_mkdir(self, pre_entry_exp)
            Base.fechar_powershell(self)
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_pastas_internas')

    def pesquisar_existe_arquivos_modelos(self, caminho_modelo):
        try:
            if caminho_modelo == None:
                existe_arquivos_modelos = False
                return existe_arquivos_modelos
            else:
                existe_em_massa, arquivo = Base.pesquisar_existe_arquivo(self, caminho_modelo, VarRede.modelo_em_massa)
                existe_capa, arquivo = Base.pesquisar_existe_arquivo(self, caminho_modelo, VarRede.modelo_capa)
                existe_financeiro, arquivo = Base.pesquisar_existe_arquivo(self, caminho_modelo, VarRede.modelo_financeiro)
                if existe_em_massa and existe_capa and existe_financeiro:
                    existe_arquivos_modelos = True
                    return existe_arquivos_modelos
                else:
                    time.sleep(Base.time_sleep_1)
                    mensagem = f'Os arquivos modelos não estão salvos no mesmo local!\nSalve-os corretamente e refaça o procedimento.'
                    Base.alertar_pyautogui(self, mensagem)
                    existe_arquivos_modelos = False
                    return existe_arquivos_modelos
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'pesquisar_existe_arquivos_modelos')

    def copiar_arquivos(self, caminho_modelo):
        try:
            origem_em_massa = caminho_modelo + '\\' + VarRede.modelo_em_massa
            origem_capa = caminho_modelo + '\\' + VarRede.modelo_capa
            origem_financeiro = caminho_modelo + '\\' + VarRede.modelo_financeiro
            existe_arquivos_modelos = NovaEmpresa.pesquisar_existe_arquivos_modelos(self, caminho_modelo)
            if existe_arquivos_modelos:
                Base.abrir_powershell(self)
                Base.executar_comando_cd(self, VarGerais.dir_rede)
                destino_capa = VarGerais.dir_rede + VarGerais.empresa + '\\' + VarRede.pasta_arquivos_modelo
                destino_financeiro = VarGerais.dir_rede + VarGerais.empresa + '\\' + VarSaude.pasta_financeiro
                Base.executar_hotkey_copiar(self, origem_em_massa, destino_capa)
                Base.executar_hotkey_copiar(self, origem_capa, destino_capa)
                Base.executar_hotkey_copiar(self, origem_financeiro, destino_financeiro)
                Base.fechar_powershell(self)
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'copiar_arquivos')

class EmpresaResult:

    def __init__(self, geral):
        self.geral = geral
    
    def __repr__(self):
        return self.geral

    def criar_novas_pastas_arquivos(self):
        try:
            cria_caminho = NovaEmpresa.criar_nova_empresa(self)

            if cria_caminho != None and cria_caminho == True:
                caminho = VarGerais.dir_rede + VarGerais.empresa
                existe_caminho, caminho = Base.pesquisar_existe_caminho_rede(self, caminho)
                if cria_caminho and not existe_caminho:
                    texto = 'Deseja criar as pastas para o cliente ?'
                    titulo = 'CONFIRMA'
                    botoes = [ 'SIM', 'NÃO' ]
                    cria_pastas = Base.confirmar_pyautogui(self, texto, titulo, botoes)
                    if cria_pastas == 'SIM':
                        texto = 'Digite o caminho dos arquivos de modelo ...'
                        caminho_modelo = f'{Base.digitar_pyautogui(self, texto, "INFORME", "")}\\'
                        existe_arquivos_modelos = NovaEmpresa.pesquisar_existe_arquivos_modelos(self, caminho_modelo)
                        
                        if existe_arquivos_modelos and caminho_modelo != None:
                            mouse_listener = pynput.mouse.Listener(suppress = True)
                            mouse_listener.start()
                            NovaEmpresa.criar_novos_caminhos(self)
                            NovaEmpresa.criar_pastas_internas(self)
                            NovaEmpresa.copiar_arquivos(self, caminho_modelo)
                            mouse_listener.stop()
                            Base.alertar_finalizado(self)
                            executar = 'EXECUTAR'
                            return executar
                        else:
                            executar = 'CANCELAR'
                            return executar
                    else:
                            executar = 'CANCELAR'
                            return executar
                else:
                    executar = 'EXECUTAR'
                    return executar
            else:
                executar = 'EXECUTAR'
                return executar
        except:
            Base.alertar_error_except(self, 'classNovaEmpresa', 'criar_novas_pastas_arquivos')



