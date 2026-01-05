
def title(name):
    largura = len(name) + 6
    console_log("\n┌" + "─" * largura + "┐")
    console_log(f"│   {name}   │")
    console_log("└" + "─" * largura + "┘\n")

def console_log(text):
  print(text)