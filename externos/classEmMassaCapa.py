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

    def gerar_pastas_em_massa(self, lista_arquivo_capa=[], lista_caminho_pc=[], lista_capa_modelo=[], lista_caminho=[]):
        try:            
            for indice, dados in enumerate(lista_arquivo_capa):
                existe_arquivo_capa, arquivo_capa = Base.pesquisar_existe_arquivo(Base.self, lista_caminho_pc[indice], lista_arquivo_capa[indice])
                caminho_modelo = VarRede.caminho_modelo + lista_capa_modelo[indice]
                if existe_arquivo_capa == False:
                    if not os.path.exists(lista_caminho_pc[indice]):
                        os.makedirs(lista_caminho_pc[indice])
                        EmMassaCapa.renomear_pasta(self, caminho_modelo, lista_caminho_pc[indice], lista_capa_modelo[indice], lista_arquivo_capa[indice])
                    elif os.path.exists(lista_caminho_pc[indice]):
                        EmMassaCapa.renomear_pasta(self, caminho_modelo, lista_caminho_pc[indice], lista_capa_modelo[indice], lista_arquivo_capa[indice])
                    elif os.path.exists(lista_caminho):
                        os.makedirs(lista_caminho_pc[indice])
                        EmMassaCapa.renomear_pasta(self, caminho_modelo, lista_caminho_pc[indice], lista_capa_modelo[indice], lista_arquivo_capa[indice])
        except:
            Base.alertar_error_except(self, 'classEmMassaCapa', 'gerar_pastas_em_massa')

    
