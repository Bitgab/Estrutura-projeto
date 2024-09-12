import os
from models.pessoas import Pessoa
from models.enums.sexo import Sexo

os.system("cls || clear")
aluno = Pessoa ("Fuboca", 22, Sexo.MASCULINO)
print(aluno)