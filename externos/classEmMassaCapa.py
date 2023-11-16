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

    def criar_pastas_em_massa(self, confirma_atualizacao):
        try:
            existe_arquivo_em_massa, arquivo_em_massa = Base.pesquisar_existe_arquivo(Base.self, VarRede.caminho_modelo, VarRede.arquivo_em_massa)
            caminho_arquivo_em_massa = VarRede.caminho_modelo + VarRede.arquivo_em_massa

            if existe_arquivo_em_massa and confirma_atualizacao == 'SIM':
                try:
                    caminho_em_massa = XMLRootResult.listas_caminho_em_massa
                    EmMassaCapa.gerar_pastas_em_massa(self, caminho_em_massa[8], caminho_em_massa[1], caminho_em_massa[9], caminho_em_massa[0])
                    '' if RedeResult.tipo_comex == 'Z' else Files.abrir_pasta_comex(self)

                    mensagem = 'Pastas Criadas !!!'
                    Base.alertar_pyautogui(self, mensagem)
                except:
                    Base.alertar_error_except(self, 'classEmMassaCapa', 'criar_pastas_em_massa if')

            elif not existe_arquivo_em_massa and confirma_atualizacao == 'SIM' :
                mensagem = f'Arquivo em Massa não está salvo na pasta !!!\n\nCaminho Rede: {caminho_arquivo_em_massa} \n\nSalve-o para continuar !!!'
                Base.alertar_pyautogui(self, mensagem)
                Files.abrir_pasta_modelo(self)

            elif confirma_atualizacao == 'NÃO':
                mensagem = 'Pastas não criadas !!!'
                Base.alertar_pyautogui(self, mensagem)
                time.sleep(Base.time_sleep_1)
            return confirma_atualizacao
        except:
            Base.alertar_error_except(self, 'classEmMassaCapa', 'criar_pastas_em_massa')

class EmMassaCapaResult:

    def __init__(self, arquivos):
        self.arquivos = arquivos

    def __repr__(self):
        return self.arquivos

    valida_em_massa = RedeResult.tipo_comex != 'Z' and ProcResult.valida_proc and ProcResult.cod_proc == '12'



