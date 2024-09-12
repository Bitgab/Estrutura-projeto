import os
from models.enums.setor import Setor
from models.enums.Sexo import Sexo
from models.funcionarios import funcionario

os.system("cls || clear")

funcionario1 = funcionario (12,"Gabriel",23,5000,Setor.FINANCEIRO, Sexo.MASCULINO)
print(funcionario1)