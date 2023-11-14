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
            
