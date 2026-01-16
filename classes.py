## Classes é uma representação de uma coisa do mundo real, um modelo para criar objetos 
## Objetos são instâncias de classes

## Exemplo:
## Pessoa é uma classe
## João é nome de um objeto da classe Pessoa
## nome, idade e sexo são atributos da classe

## Criando uma classe pessoa
## por convensão, as classes começam com letra maiúscula
class Pessoa():
    ## __init__ é um método especial que é chamado quando um objeto é criado
    ## self é uma referência ao objeto que está sendo criado
    def __init__(self, nome, idade, sexo,estado_civil = "Solteiro(a)",conjulge = None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.conjulge = conjulge
## Métodos
    def casar(self,pessoa):
        if (self.estado_civil == "Solteiro(a)" or self.estado_civil == "Divorciado(a)") and (pessoa.estado_civil == "Solteiro(a)" or pessoa.estado_civil == "Divorciado(a)"):
                self.estado_civil = "Casado(a)"
                pessoa.estado_civil = "Casado(a)"
                self.conjulge = pessoa.nome
                pessoa.conjulge = self.nome
                print(f"{self.nome} e {pessoa.nome} se casaram")
        else:
            print("Não é possível casar")

    def divorciar(self,conjulge):
        if self.estado_civil == "Casado(a)" and self.conjulge == conjulge.nome:
            self.estado_civil = "Divorciado(a)"
            self.conjulge = None
            conjulge.estado_civil = "Divorciado(a)"
            conjulge.conjulge = None
            print(f"{self.nome} se divorciou de {conjulge.nome}")
        else:
            print("Não é possível divorciar")
