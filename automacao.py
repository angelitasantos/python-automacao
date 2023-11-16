#----------------------------------------------------------------------------------------------------------------
# ESCOLHER A AÇÃO PRINCIPAL


from base.base import *
from base.main import *
from base.classNovaEmpresa import *
from base.classAno import *
from base.classProcedimento import *

from cliente.classRede import *
from cliente.classCliente import *
from cliente.classFiles import *

from externos.classXMLListas import *
from externos.classXMLRoot import *
from externos.classXMLExtrair import *
from externos.classExcel import *

from externos.classPDF import *
from externos.classSaude import *
from externos.classEmMassaCapa import *
from externos.classEmMassaXML import *

from classAcoes import *


if ProcResult.valida_proc:
    Acoes.escolher_procedimento(Base.self, ProcResult.procedimento, ProcResult.cod_proc)
