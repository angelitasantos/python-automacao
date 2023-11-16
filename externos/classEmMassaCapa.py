#----------------------------------------------------------------------------------------------------------------
# GERAR CAPA DOS PROCESSOS A PARTIR DO ARQUIVO EM MASSA


from externos.classSaude import *


class EmMassaCapa:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    try:
        arquivo_em_massa = VarRede.arquivo_em_massa
    except:
        Base.alertar_error_except(Base.self, 'classEmMassaCapa', 'EmMassaCapa')
    
    def renomear_pasta(self, caminho_modelo, caminho_pc, arquivo_modelo, arquivo_novo):
        try:
            Base.abrir_powershell(self)
            copy_item = f'copy "{caminho_modelo}" "{caminho_pc}"'
            pyperclip.copy(copy_item)
            time.sleep(Base.time_sleep_1)
            Base.executar_hotkey_colar(self)
            pasta_nova = caminho_pc + '\\' + arquivo_modelo
            rename_item = f'Rename-Item "{pasta_nova}" "{arquivo_novo}"'
            pyperclip.copy(rename_item)
            time.sleep(Base.time_sleep_1)
            Base.executar_hotkey_colar(self)
            Base.fechar_powershell(self)
        except:
            Base.alertar_error_except(self, 'classEmMassaCapa', 'renomear_pasta')




            