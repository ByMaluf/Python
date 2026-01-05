# Variáveis globais
numero_escolhido = 0
list_tasks = []
# ------------------

def title(name):
    largura = len(name) + 6
    console_log("\n┌" + "─" * largura + "┐")
    console_log(f"│   {name}   │")
    console_log("└" + "─" * largura + "┘\n")

def console_log(text):
  print(text)
  
def add_task():
  title("MODO ADICIONAR TAREFA")
  task = input("Digite a nova tarefa: ")
  list_tasks.append({"task": task, "completed": False})
  console_log("\n############################")
  console_log(f"#  Tarefa adicionada com sucesso!: {task}   #")
  console_log("############################\n")
  
def view_tasks():
  title("LISTA")
  if not list_tasks:  
    console_log("# Nenhuma tarefa cadastrada. #\n")
  else:
    console_log(f"#  Tarefas cadastradas: {len(list_tasks)}   #\n")
    for index, task in enumerate(list_tasks, start=1):
      is_active = "Completa" if task['completed'] else "Pendente"
      is_checked = "✓" if task['completed'] else " "
      task_name = task['task']
      show_task = f"| {index}. [{is_checked}] Nome: {task_name} -- Status: {is_active} |"
      console_log(show_task)
  console_log("\n")

def update_task(index):
  title("MODO ATUALIZAR TAREFA")
  index_convert = int(index) - 1
  new_name = input("Digite o novo nome da tarefa: ")
  list_tasks[index_convert]["task"] = new_name
  console_log("\n############################")
  console_log(f"#  Tarefa {index} atualizada com sucesso!: {new_name}   #")
  console_log("############################\n")
  
def check_task(index):
  title("MODO MARCAR TAREFA COMO CONCLUÍDA")
  index_convert = int(index) - 1
  list_tasks[index_convert]["completed"] = True
  console_log("\n############################")
  console_log(f"#  Tarefa {index} marcada como concluída com sucesso!   #")
  console_log("############################\n")

def remove_task(index):
  title("MODO REMOVER TAREFA")
  index_convert = int(index) - 1
  list_tasks.pop(index_convert)
  console_log("\n############################")
  console_log(f"#  Tarefa {index} removida com sucesso!   #")
  console_log("############################\n")
  
def exists_task(index):
  index_convert = int(index) - 1
  if index_convert < 0 or index_convert >= len(list_tasks):
    console_log(f"\n### Tarefa {index} não encontrada. Tente novamente. ###\n")
    return False
  return True

def validate_number(numero_escolhido):
  convert_number = int(numero_escolhido)
  if convert_number < 1 or convert_number > 6:
    console_log("### Opção inválida. Tente novamente. ###\n")
  elif convert_number == 1:
    add_task()
  elif convert_number == 2:
    view_tasks()
  elif convert_number == 3:
    view_tasks()
    selection_index = input("Digite o número da tarefa que deseja atualizar: ")
    if exists_task(selection_index):
     update_task(selection_index)
  elif convert_number == 4:
    view_tasks()
    selection_index = input("Digite o número da tarefa que deseja remover: ")
    if exists_task(selection_index):
      remove_task(selection_index)
  elif convert_number == 5:
    view_tasks()
    selection_index = input("Digite o número da tarefa que deseja marcar como concluída: ")
    if exists_task(selection_index):
      check_task(selection_index)
  elif convert_number == 6:
    return True
    
while numero_escolhido != 6:
  console_log("########## MENU ##########")
  console_log("1 - Adicionar tarefa")
  console_log("2 - Listar tarefas")
  console_log("3 - Atualizar tarefa")
  console_log("4 - Remover tarefa")
  console_log("5 - Marcar tarefa como concluída")
  console_log("6 - Sair")
  numero_escolhido = int(input("\nEscolha uma opção: "))
  format_number = validate_number(numero_escolhido)
  if format_number: break