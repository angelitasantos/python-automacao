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
