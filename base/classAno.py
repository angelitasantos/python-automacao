#----------------------------------------------------------------------------------------------------------------
# ESCOLHER O ANO


from base.classNovaEmpresa import *


class Ano:

    def __init__(self, ano):
        self.ano = ano

    def __repr__(self):
        return self.ano

    executar = EmpresaResult.criar_novas_pastas_arquivos(Base.self)

    def pesquisar_tipo_processo(self):
        try:
            processo_ativo = None
            busca = VarGerais.processo
            for s in VarGerais.lista_processos:
                if busca in s:
                    processo_ativo = s
                    break
            if processo_ativo:
                return processo_ativo
        except:
            Base.alertar_error_except(self, 'classAno', 'pesquisar_tipo_processo')

    def gerar_data_atual(self):
        try:
            data_atual = date.today()
            ano_atual = date.today().year
            data_formatada_br = data_atual.strftime('%d/%m/%Y')
            ano_anterior_default = ano_atual - 1
            return ano_atual, data_formatada_br, ano_anterior_default
        except:
            Base.alertar_error_except(self, 'classAno', 'gerar_data_atual')

    def escolher_ano_anterior(self):
        try:
            ano_atual, data_atual, ano_anterior_default = Ano.gerar_data_atual(self)
            texto = f'Digite o Ano do Processo.\nEscreva quatro digítos para continuar.'
            escolher_ano_anterior = Base.digitar_pyautogui(self, texto, 'INFORME', ano_anterior_default)
            if escolher_ano_anterior != None:
                ano_anterior = escolher_ano_anterior
                len_escolha = len(escolher_ano_anterior)
                return ano_anterior, len_escolha
            else:
                ano_anterior = ''
                len_escolha = 4
                return ano_anterior, len_escolha
        except:
            Base.alertar_error_except(self, 'classAno', 'escolher_ano_anterior')

    def validar_ano_anterior(self):
        try:
            ano_anterior, len_escolha = Ano.escolher_ano_anterior(self)
            if ano_anterior != None:
                while len_escolha != 4:
                    try:
                        mensagem = f'Você não digitou um ANO válido!\nLembre-se de escrever os quatro digítos do ANO.'
                        Base.alertar_pyautogui(self, mensagem)
                        ano_anterior, len_escolha = Ano.escolher_ano_anterior(self)
                    except:
                        Base.alertar_error_except(self, 'classAno', 'validar_ano_anterior while')
                return ano_anterior
        except:
            Base.alertar_error_except(self, 'classAno', 'validar_ano_anterior')

    def escolher_tipo_ano(self):
        try:
            texto = 'Escolha o Ano do Processo ...'
            titulo = 'OPÇÃO'
            botoes = [ 'ANO ATUAL', 'ANO ANTERIOR' ]
            tipo_ano = Base.confirmar_pyautogui(self, texto, titulo, botoes)
            return tipo_ano
        except:
            Base.alertar_error_except(self, 'classAno', 'escolher_tipo_ano')




