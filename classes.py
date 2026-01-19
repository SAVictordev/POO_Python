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

## Métodos da classe pessoa

    def casar(self,pessoa):
        if (self.estado_civil == "Solteiro(a)" or self.estado_civil == "Divorciado(a)") and (pessoa.estado_civil == "Solteiro(a)" or pessoa.estado_civil == "Divorciado(a)"):
                self.estado_civil = "Casado(a)"
                pessoa.estado_civil = "Casado(a)"
                self.conjulge = pessoa.nome
                pessoa.conjulge = self.nome
                print(f"{self.nome} e {pessoa.nome} se casaram")
        else:
            print(f'{self.nome} não pode se casar com {pessoa.nome}')

    def divorciar(self,conjulge):
        if self.estado_civil == "Casado(a)" and self.conjulge == conjulge.nome:
            self.estado_civil = "Divorciado(a)"
            self.conjulge = None
            conjulge.estado_civil = "Divorciado(a)"
            conjulge.conjulge = None
            print(f"{self.nome} se divorciou de {conjulge.nome}")
        else:
            print(f'{self.nome} não atende os requisitos para divorciar.')

    def apresentar(self):
        if self.estado_civil == "Casado(a)":
            print(f"Meu nome é {self.nome}, tenho {self.idade} anos e sou casado com {self.conjulge}")
        elif self.estado_civil == "Divorciado(a)":
            print(f"Meu nome é {self.nome}, tenho {self.idade} anos e sou divorciado(a)")
        else:
            print(f"Meu nome é {self.nome}, tenho {self.idade} anos e sou solteiro(a)")

## Classe Clinica para treinar o uso de classes dependentes de outras classes
class Clinica ():
    def __init__(self,especialidade):   
        self.especialidade = especialidade
        self.consultas = []

# Métodos da classe Clinica
    def adicionar_consulta(self,consulta):
        self.consultas.append(consulta)

    def listar_consultas(self):
        for consulta in self.consultas:
            print(consulta)

# Classe Consulta que é uma classe que depende de outras classes (Pessoa e Clinica) e é uma classe abstrata
class Consulta ():
    def __init__(self,paciente,clinica):
        self.paciente = paciente
        self.clinica = clinica

# Métodos da classe Consulta
    def agendar_consulta(self):
        print(f'{self.paciente.nome} agendou uma consulta para {self.clinica.especialidade}')
        self.clinica.adicionar_consulta(self)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} - {self.clinica.especialidade}"


# Instanciamento de objetos
p1 = Pessoa("João", 30, "Masculino")
c1 = Clinica("Cardiologia")

# Instanciamento de objetos da classe Consulta
consul1 = Consulta(p1, c1)
consul1.agendar_consulta()

# Listagem de consultas da Classe Clinica
c1.listar_consultas()


