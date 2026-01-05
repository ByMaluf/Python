from utils import console_log, title

list_tasks = []

def add_contact():
    title("MODO ADICIONAR CONTATO")
    name = input("Digite o nome do contato: ")
    phone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorite = input("O contato é favorito? (sim/não): ").lower() == "sim"

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": favorite
    }

    list_tasks.append(contact)
    console_log("\n############################")
    console_log(f"#  Contato adicionado com sucesso!: {name}   #")
    console_log("############################\n")

def view_contacts():
    title("CONTATOS")
    if not list_tasks:
        console_log("# Nenhum contato cadastrado. #\n")
    else:
        console_log(f"#  Contatos cadastrados: {len(list_tasks)}   #\n")
        for index, contact in enumerate(list_tasks, start=1):
            favorite_status = "Favorito" if contact["favorite"] else "Normal"
            console_log(f"{index}. Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}, Status: {favorite_status}")
    console_log("\n")

def edit_contact(index):
    title("EDITAR CONTATO")
    index_convert = int(index) - 1

    if index_convert < 0 or index_convert >= len(list_tasks):
        console_log(f"\n### Contato {index} não encontrado. Tente novamente. ###\n")
        return

    contact = list_tasks[index_convert]
    console_log(f"Editando contato: {contact['name']}")

    contact['name'] = input("Digite o novo nome do contato: ") or contact['name']
    contact['phone'] = input("Digite o novo telefone do contato: ") or contact['phone']
    contact['email'] = input("Digite o novo email do contato: ") or contact['email']
    favorite = input("O contato é favorito? (sim/não): ").lower()
    contact['favorite'] = True if favorite == "sim" else contact['favorite']

    console_log("\n############################")
    console_log(f"# Contato atualizado com sucesso! #")
    console_log("############################\n")

def toggle_favorite(index):
    title("MARCAR/DESMARCAR FAVORITO")
    index_convert = int(index) - 1

    if index_convert < 0 or index_convert >= len(list_tasks):
        console_log(f"\n### Contato {index} não encontrado. Tente novamente. ###\n")
        return

    contact = list_tasks[index_convert]
    contact['favorite'] = not contact['favorite']
    status = "Favorito" if contact['favorite'] else "Normal"

    console_log("\n############################")
    console_log(f"# Contato atualizado para: {status} #")
    console_log("############################\n")

def view_favorites():
    title("CONTATOS FAVORITOS")
    favorites = [contact for contact in list_tasks if contact['favorite']]

    if not favorites:
        console_log("# Nenhum contato favorito encontrado. #\n")
    else:
        console_log(f"# Contatos favoritos: {len(favorites)} #\n")
        for index, contact in enumerate(favorites, start=1):
            console_log(f"{index}. Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}")
    console_log("\n")

def delete_contact(index):
    title("APAGAR CONTATO")
    index_convert = int(index) - 1

    if index_convert < 0 or index_convert >= len(list_tasks):
        console_log(f"\n### Contato {index} não encontrado. Tente novamente. ###\n")
        return

    contact = list_tasks.pop(index_convert)
    console_log("\n############################")
    console_log(f"# Contato {contact['name']} apagado com sucesso! #")
    console_log("############################\n")

def show_options():
    console_log("Escolha uma das opções abaixo:")
    console_log("1. Adicionar um contato")
    console_log("2. Visualizar contatos cadastrados")
    console_log("3. Editar um contato existente")
    console_log("4. Marcar/Desmarcar um contato como favorito")
    console_log("5. Visualizar contatos favoritos")
    console_log("6. Apagar um contato")
    console_log("7. Sair")

    choice = input("Digite o número da sua escolha: ")
    return choice

if __name__ == "__main__":
    while True:
        user_choice = show_options()
        if user_choice == "1":
            add_contact()
        elif user_choice == "2":
            view_contacts()
        elif user_choice == "3":
            view_contacts()
            selection_index = input("Digite o número do contato que deseja editar: ")
            edit_contact(selection_index)
        elif user_choice == "4":
            view_contacts()
            selection_index = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
            toggle_favorite(selection_index)
        elif user_choice == "5":
            view_favorites()
        elif user_choice == "6":
            view_contacts()
            selection_index = input("Digite o número do contato que deseja apagar: ")
            delete_contact(selection_index)
        elif user_choice == "7":
            console_log("Saindo do aplicativo...")
            break
        else:
            console_log(f"Você escolheu a opção {user_choice}. Implementação pendente.")

