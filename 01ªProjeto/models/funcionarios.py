from models.enums.Sexo import Sexo
from models.enums.setor import Setor
class funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo ) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (
                f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade} anos"
                f"\nSalário... R${self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}"                   
                )    
