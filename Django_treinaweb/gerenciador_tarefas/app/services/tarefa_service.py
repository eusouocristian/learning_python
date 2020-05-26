from ..models import Tarefa

# cadastrar os métodos para manipular as tarefas no banco de dados


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao,
                          prioridade=tarefa.prioridade, data_expiracao=tarefa.data_expiracao,
                          usuario=tarefa.usuario)


def listar_tarefas(usuario):
    # mesmo que fazer <SELECT * FROM app_tarefa> no SQL
    #return Tarefa.objects.all()

    return Tarefa.objects.filter(usuario=usuario).all()


def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)


def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.prioridade = tarefa_nova.prioridade
    tarefa_bd.save(force_update=True)


def remover_tarefa(tarefa_bd):
    tarefa_bd.delete()
