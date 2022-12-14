class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


class Professor(Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, tipo):
        super().__init__(nome, nascimento)
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos

    def set_casa(self, casa):
        self.casa = casa


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def get_diretor(self):
        return self.__diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_monitor(self):
        return self.__monitor

class Torneio:
    def __init__ (self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0 
        self.__pontos_casa2 = 0
   
    def marcar_ponto(self, casa, quantidade):
        if casa == self.casa1:
            self.__pontos_casa1 += quantidade
        else:
            self.__pontos_casa2 += quantidade

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2

    
try:
    # Cria????o do objeto Escola
    hogwarts = Escola("Escola de Magia e Bruxaria de Hogwarts")
    assert hogwarts.nome == 'Escola de Magia e Bruxaria de Hogwarts'
    print('CORRETO: Cria????o do objeto Escola')
except Exception:
    print('ERRO...: Cria????o do objeto Escola')

try:
    # Cria????o dos objetos Casa
    grifinoria = Casa("Grifin??ria", "Le??o")
    sonserina = Casa("Sonserina", "Serpente")
    corvinal = Casa("Corvinal", "Corvo")
    lufalufa = Casa("Lufa-Lufa", "Texugo")
    assert sonserina.nome == "Sonserina"
    assert sonserina.animal == "Serpente"
    print('CORRETO: Cria????o dos objetos Casa')
except Exception:
    print('ERRO...: Cria????o dos objetos Casa')

try:
    # Cria????o dos objetos Disciplina
    herbologia = Disciplina("Herbologia", "Ervas, Fungos e ??rvores M??gicas")
    transfiguracao = Disciplina("Transfiguracao", "Transfigura????o Humana")
    pocoes = Disciplina("Po????es", "Po????es Simples, Po????es Avan??adas")
    defesa = Disciplina("Defesa", "Maldi????es, Dementadores, Feiti??os verbais")
    assert defesa.nome == "Defesa"
    assert herbologia.ementa == "Ervas, Fungos e ??rvores M??gicas"
    print('CORRETO: Cria????o dos objetos Disciplina')
except Exception:
    print('ERRO...: Cria????o dos objetos Disciplina')

try:
    # Teste da classe Pessoa
    pessoa1 = Pessoa("Ana Paula", "19351004")
    assert pessoa1.nome == "Ana Paula"
    assert pessoa1.nascimento == "19351004"
    print('CORRETO: Cria????o do objeto Pessoa')
except Exception:
    print('ERRO...: Cria????o do objeto Pessoa')

try:
    # Cria????o dos objetos Professor
    minerva = Professor("Minerva McGonagall", "19351004")
    filio = Professor("F??lio Flitwick", "19301017")
    pomona = Professor("Pomona Sprout", "19410515")
    severo = Professor("Severo Snape", "19600109")
    assert minerva.nome == "Minerva McGonagall"
    assert severo.nascimento == "19600109"
    print('CORRETO: Cria????o dos objetos Professor')
except Exception:
    print('ERRO...: Cria????o dos objetos Professor')

try:
    # Cria????o dos objetos Aluno
    draco = Aluno("Draco Malfoy", "19800605", "puro-sangue")
    ernesto = Aluno("Ernesto Macmillan", "19800901", "puro-sangue")
    hermione = Aluno("Hermione Granger", "19790919", "trouxa")
    harry = Aluno("Harry Potter", "19800731", "mesti??o")
    luna = Aluno("Luna Lovegood", "19810213", "puro-sangue")
    assert luna.nome == "Luna Lovegood"
    assert luna.nascimento == "19810213"
    assert draco.tipo == "puro-sangue"
    print('CORRETO: Cria????o dos objetos Aluno')
except Exception:
    print('ERRO...: Cria????o dos objetos Aluno')

try:
    # Cria????o do objeto Torneio
    torneio = Torneio(sonserina, grifinoria)
    assert torneio.casa1.nome == "Sonserina"
    assert torneio.casa2.nome == "Grifin??ria"
    print('CORRETO: Cria????o do objeto Torneio')
except Exception:
    print('ERRO...: Cria????o do objeto Torneio')

try:
    # Inclui as casas na escola
    hogwarts.incluir_casa(grifinoria)
    hogwarts.incluir_casa(sonserina)
    hogwarts.incluir_casa(corvinal)
    hogwarts.incluir_casa(lufalufa)
    assert len(hogwarts.casas) == 4
    print('CORRETO: Inclui as casas na escola')
except Exception:
    print('ERRO...: Inclui as casas na escola')

try:
    # Defini????o dos diretores das casas (set_diretor e get_diretor)
    grifinoria.set_diretor(minerva)
    sonserina.set_diretor(severo)
    corvinal.set_diretor(filio)
    lufalufa.set_diretor(pomona)
    assert grifinoria.get_diretor().nome == "Minerva McGonagall"
    print('CORRETO: Defini????o dos diretores das casas')
except Exception:
    print('ERRO...: Defini????o dos diretores das casas')

try:
    # Definicao dos monitores das casas (set_monitor e get_monitor)
    grifinoria.set_monitor(hermione)
    sonserina.set_monitor(draco)
    corvinal.set_monitor(ernesto)
    lufalufa.set_monitor(luna)
    assert grifinoria.get_monitor().nome == "Hermione Granger"
    print('CORRETO: Definicao dos monitores das casas')
except Exception:
    print('ERRO...: Definicao dos monitores das casas')

try:
    # Defini????o das casas dos alunos
    draco.set_casa(sonserina)
    ernesto.set_casa(corvinal)
    hermione.set_casa(grifinoria)
    harry.set_casa(grifinoria)
    luna.set_casa(lufalufa)
    assert draco.casa.nome == "Sonserina"
    print('CORRETO: Defini????o das casas dos alunos')
except Exception:
    print('ERRO...: Defini????o das casas dos alunos')

try:
    # Definicao dos professores das disciplinas
    severo.incluir_disciplina(defesa)
    severo.incluir_disciplina(transfiguracao)
    minerva.incluir_disciplina(herbologia)
    filio.incluir_disciplina(transfiguracao)
    pomona.incluir_disciplina(pocoes)
    assert severo.disciplinas[1].nome == "Transfiguracao"
    print('CORRETO: Definicao dos professores das disciplinas')
except Exception:
    print('ERRO...: Definicao dos professores das disciplinas')

try:
    # Defini????o das disciplinas dos alunos
    harry.incluir_disciplina(herbologia)
    harry.incluir_disciplina(defesa)
    hermione.incluir_disciplina(herbologia)
    hermione.incluir_disciplina(transfiguracao)
    hermione.incluir_disciplina(defesa)
    draco.incluir_disciplina(transfiguracao)
    draco.incluir_disciplina(defesa)
    ernesto.incluir_disciplina(pocoes)
    ernesto.incluir_disciplina(defesa)
    luna.incluir_disciplina(defesa)
    assert len(harry.disciplinas) == 2
    assert len(hermione.disciplinas) == 3
    assert len(draco.disciplinas) == 2
    assert len(luna.disciplinas) == 1
    assert len(ernesto.disciplinas) == 2
    assert harry.disciplinas[0].nome == "Herbologia"
    print('CORRETO: Defini????o das disciplinas dos alunos')
except Exception:
    print('ERRO...: Defini????o das disciplinas dos alunos')

try:
    # Inclus??o de triunfos e mau_feitos dos alunos
    harry.incluir_triunfo(3)
    harry.incluir_mau_feito(1)
    draco.incluir_mau_feito(2)
    draco.incluir_triunfo(1)
    hermione.incluir_triunfo(4)
    harry.incluir_triunfo(2)
    assert hermione.get_triunfos() == 4
    assert draco.get_mau_feitos() == 2
    print('CORRETO: Inclus??o de triunfos e mau_feitos dos alunos')
except Exception:
    print('ERRO...: Inclus??o de triunfos e mau_feitos dos alunos')

try:
    # Marca????o de pontos no torneio de quadribol
    torneio.marcar_ponto(sonserina, 2)
    torneio.marcar_ponto(grifinoria, 1)
    torneio.marcar_ponto(grifinoria, 3)
    torneio.marcar_ponto(sonserina, 1)
    assert torneio.get_pontos_casa1() == 3
    assert torneio.get_pontos_casa2() == 4
    print('CORRETO: Marca????o de pontos no torneio de quadribol')
except Exception:
    print('ERRO...: Marca????o de pontos no torneio de quadribol')