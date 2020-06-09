# boa pratica criar variaveis privadas (sem possibilidade de acesso atraves da classe, usando '__' antes do nome
class Tarefa:
    def __init__(self, titulo, descricao, data_expiracao, prioridade, usuario):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_expiracao = data_expiracao
        self.__prioridade = prioridade
        self.__usuario = usuario

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.descricao = descricao

    @property
    def data_expiracao(self):
        return self.__data_expiracao

    @data_expiracao.setter
    def data_expiracao(self, data_expiracao):
        self.data_expiracao = data_expiracao

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.usuario = usuario

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade):
        self.prioridade = prioridade


