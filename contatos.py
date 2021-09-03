from Classes.agenda import Agenda
from Classes.tarefa import Tarefa
from Classes.contato import Contato

agenda = Agenda('nome', 2021)
tarefa = Tarefa('descricao', 'status')
contato = Contato('12313', 'Nome', 'teste@teesx')

agenda.nome = input('Fale o nome da agenda: ')
agenda.ano = int(input('Fale o ano em que a agenda foi feita: '))

continuar = True

while continuar:
    fazer = int(input('----------------------------\nDigite 1 se quiser criar um contato \n2 se quiser listar os contatos\n3 se quiser excluir contato\n4 se quiser criar tarefa\n5 se quiser listar as tarefas\n6 se quiser excluir as tarefas: '))

    if fazer == 1:
        contato.Cadastrar('Gabriela', '9 9485-6582')
        print('Um contato foi salvo')
    elif fazer == 2:
        print(contato.Listar())
    elif fazer == 3:
        contato.Excluir()
        print('Um contato foi excluído')
    elif fazer == 4:
        tarefa.Criar("Ligar para Mãe", "Pendente")
        print('Tarefa criada')
    elif fazer == 5:
        print(tarefa.Listar())
    elif fazer == 6:
        tarefa.Excluir()
        print('Tarefa excluída')
    else:
        print('Favor informar um numero de 1 a 10')
    verifica = int(input('informe 0 se quiser fazer mais um processo: '))

    if verifica == 0:
        continue
    else:
        continuar = False
