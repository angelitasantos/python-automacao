#----------------------------------------------------------------------------------------------------------------
# DEFINIR O CAMINHO NA REDE


from base.base import *
from base.classProcedimento import *


class Rede:

    def __init__(self, rede):
        self.rede = rede

    def __repr__(self):
        return self.excel

    pastas_em_massa = 'SIM' if ProcResult.cod_proc != '12' else 'NÃO'
    arquivo_em_massa = 'SIM' if ProcResult.cod_proc != '23' else 'NÃO'
    pasta_modelo = 'SIM' if ProcResult.cod_proc != '33' else 'NÃO'
    excel_em_massa = 'SIM' if ProcResult.cod_proc != '34' else 'NÃO'
    pasta_comex = 'SIM' if ProcResult.cod_proc != '35' else 'NÃO'
    auditoria = 'SIM' if ProcResult.procedimento != 'AUDITORIA' else 'NÃO'
    proc_com_modal = pastas_em_massa == 'SIM' and pasta_modelo == 'SIM' and excel_em_massa == 'SIM' and pasta_comex == 'SIM' and arquivo_em_massa == 'SIM' and auditoria == 'SIM'

    