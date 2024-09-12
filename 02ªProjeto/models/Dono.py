from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enums.unidade_federativa import  UnidadeFederativa
from models.endereco import Endereco

class Dono: 
    def __init__(self,nome: str, idade: int, Setor: Setor, Salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.setor = Setor
        self.salario = Salario
        self.endereco = endereco 

    def __str__(self) -> str:
        return (

            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade} anos"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: R$ {self.salario} reais"
            f"\nEndereço: {self.endereco}"
        )   
