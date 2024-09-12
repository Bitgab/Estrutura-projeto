from  abc import ABC, abstractmethod
from models.Endereco import Endereco
from models.enums.Sexo import Sexo
from models.Fisica import Fisica
from models.enums.Setor import  Setor

class Funcionario(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.matricula = matricula
        self.setor     = setor
        self.salario   = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"{super().__str__()}"
               f"\nMatrícula: {self.matricula}"
               f"\nSetor: {self.setor.value}"
               f"\nSalário: R$ {self.salario} reais" 
               f"\nSalário final: R$ {self.salario_final()} reais"
               )    