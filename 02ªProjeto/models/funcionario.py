from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa
from models.endereco import Endereco

class Funcionario: 
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, dataNascimento: str, sexo: Sexo, setor: Setor, salario: float, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg 
        self.matricula = matricula
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.setor = setor
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nData de nascimento: {self.dataNascimento} anos"
            f"\nSexo: {self.sexo.value}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: R$ {self.salario} reais"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}"
            )    