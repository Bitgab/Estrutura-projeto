import os
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.funcionario import Funcionario
from models.Dono import Dono
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

funcionario1 = Funcionario(12,"Gabriel","123.456.789-00","12.345.678-90","120924","12/09/2024",Sexo.MASCULINO,Setor.DIRETOR,"10000","(71) 91234-5678","gabriel@gmail.com", Endereco("Rua A", "12","Perto da casa","12.345-678", "Vera Cruz", UnidadeFederativa.BAHIA))
                            
print(funcionario1)