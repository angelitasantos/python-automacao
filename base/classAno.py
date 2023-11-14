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
