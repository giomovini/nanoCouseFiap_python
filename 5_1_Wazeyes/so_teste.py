import platform
import getpass
from datetime import datetime

# print("Nome da máquina:............", platform.node())
# print("Arquitetura:................", platform.architecture())
# print("Sistema Operacional:........", platform.system())
# print("Versão do SO:...............", platform.release())
# print("Processador:................", platform.processor())
# print("Versão do Python............", platform.python_version())

# print(datetime.now().date())

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:....")

if usuario == 'vinig' and senha == "Hello":
    print("Bem vindo")
else:
    print("Você não tem acesso")