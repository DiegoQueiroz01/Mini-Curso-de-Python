# ---------------------------------------------------------------------------------------
# To-Do List, no terminal do VsCode.
# ---------------------------------------------------------------------------------------
# O que iremos fazer? uma lista de tarefas, onde o usuário pode adicionar, remover, salvar e visualizar tarefas.
# Para isso iremos usar listas, funções e manipulação de arquivos.
# Criaremos também um menu com while, e uma entrada de dados do usuário.

# ---------------------------------------------------------------------------------------

import os # importa o módulo para o sistema operacional, limpar o terminal

NOME_ARQUIVO = "tarefas.txt" # definir uma constante nome arquivo, vai ser onde ficará salva as notas

def limpar_terminal(): # define uma função limpar terminal
    "Limpa a tela do terminal" 
    os.system('cls' if os.name == 'nt' else 'clear') # verificar o sistema operacional da máquina, se for windows ('nt'), ou se for linux ou mac ('clear')

def carregar_tarefas(nome_arquivo): # carregar uma função que recebe o nome do arquivo como argumento.
    "Carregar as tarefas do arquivo .txt"
    tarefa = [] # criar uma lista chamada 'tarefa, que inicializa as tarefas lidas do arquivo.

    try: 
        with open(nome_arquivo, 'r', econding = 'utf-8') as arquivo: # abrir o arquivo em modo leitura ('r') e com condificação utf-8
            for linha in f: # ler cada linha do arquivo.
                tarefa.append(linha.strip()) # adicionar uma linha na lista de tarefas, além de remover os espaços
        print("Tarefas carregas com sucesso! '{nome_arquivo}'") #informar ao usuário que as tarefas foram carregadas com sucesso.
    except FileNotFoundError: # caso o arquivo não seja encontrado, ele imprime uma mensagem de erro.
        print(f"Arquivo {nome_arquivo} . NNão encontrado. Começando com uma lista vazia.") # Informa ao usuário que o arquivo não foi encontrado, e continua com uma lista vazia.
    except Exception as e: #se caso ocorrer outro erro, ele imprime uma mensagem de erro.
        print(f"Ocorreu um erro ao carregar as tarefas: {e}") ## informar o erro.
    return tarefa # retornar a listaa de tarefas,ele também pode esvaziar a lista de tarefas, se caso o arquivo não for encontrado. 

def salvar_tarefas(nome_arquivo, tarefas): #essa função recebe o nome do arquivo e a lista de tarefas com argumentos.
    "Salvar as atrefas em arquivo .txt"
    try: #faz um tratamento de exceções ao salvar o arquivo.
        with open(nome_arquivo, 'w', enconding = 'utf-8') as arquivo: # abrir um arquivo em modo de escrita ('w') com condificação utf-8.
            for tarefa in tarefas: #para cada tarefa criada na lista de tarefas, ele vai escrever um arquivo.
                f.write(tarefa + '\n') # escrever a tarefa no arquivo
            print(f"Tarefa salva com sucesso '{nome_arquivo}' .") # informa as tarefas salvas ao usuário.
    except Exception as e: #se tiver algum erro, ele captura o erro, e imprime uma mensagem de erro.
        print(f"Ocorreu um erro de salvamento da tarefa. {e}") #informar sobre o erro.

def adicionar_tarefa(tarefas): #adicionar uma função chamada tarefas, e receber de tarefas como argumento.
    "Adicionar uma nova tarefa"
    limpar_terminal() #chamada a função de limpar terminal
    print("Adiconar nova tarefa") #imprimir uma mensagem no cabeçalho da seção
    nova_tarefa = input("Digite a nova tarefa: ") #solicitar pro usuário uma nova tarefa.
    if nova_tarefa: #verifica se o usuário digitou algo.
        tarefas.append(nova_tarefa) #adiciona uma nova tarefa na lista de tarefas.
        print(f"Tarefa '{nova_tarefa}' adicionada.")
    else: #se o usuário não inserir nenhuma informação.
        print("Nehuma informação/tarefa inserida")
    input("Pressione enter para continuar...")

def visualizar_tarefa(tarefas): #criar uma função que permite ao usuário visualizar tarefas criadas.
    "Visualizar as tarefas criadas"
    limpar_terminal()
    print("Lista de tarefas")
    if not tarefas: #verifica se a lista está vazia.
        print("Nehuma tarefa encontrada.") 
        input("Pressione entre para continuar...")
    else: #se a lista não está vazia, ele imprime as tarefas.
        for i, tarefa in enumerate(tarefas, start=1): #numerar as tarefas com enumerate.
            print(f"{i}. {tarefa}") #imprime o número de tarefas já criadas.
    input("\nPressione enter para continuar...")

def remover_tarefas(tarefas): #permite remover tarefas já criadas.
    "Remover uma tarefa"
    limpar_terminal()
    print("Remover tarefas")
    if not tarefas: # verifica se a lista de tarefas está vazia.
        print("Nehuma tarefa encontrada.")
        input("\nPressione enter para continuar...")
        return # se a lista estiver vazia, ele sai da função e retorna pro menu inicial
    
    for i, tarefa in enumerate(tarefas, start=1): #exibe as tarefas enumeradas pro usuário
        print(f"{i}. {tarefas}") #imprime o número de tarefas ao usuário.

    while True: #inicia um loop para remover tarefas.
        try: #lida com entrada inválida do usuário.
            num_tarefa_str = input("\nDigite o número de tarefas que deseja remover (ou 'sair' para voltar ao menu):")
            num_tarefa = int(num_tarefa_str) #converte o comando do usuário, de uma string para um valor inteiro.

            if num_tarefa == 0: #se o usuário digitar zero
                print("Remoção cancelada.")
                break #sai do loop e voltar pro menu.
            elif 1 <= num_tarefa <= len(tarefas): #verifica se o que o usuário digitou, está dentor de um intervalo válido de tarefas.
                tarefa_removida = tarefas.pop(num_tarefa - 1) #remove da lista de tarefas, e armazena em tarefas removidas.
                print(f"Tarefa '{tarefa_removida}' removida com sucesso.")
                break #sai do loop e volta pro menu.
            else: #se o usuário digitou um número inválido.
                print("Número de tarefas inválido. Pro favor, digite um número válido.") #pede pro usuário digitar um número válido.
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido ou 'sair' para voltar ao menu.")
        except Exception as e: #se ocorrer algum possível erro.
            print(f"Ocorreu um erro ao remover tarefa. {e}") 
        input("\nPressionar enter para voltar ao menu...")

def mostrar_menu(): #chama a função menu.
    "Exibe o menu de opções"
    limpar_terminal()
    print("\n--------To-Do List--------")
    print("1. Adiconar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefas")
    print("4. Salvar tarefas")
    print("5. Sair sem salvar")

def main(): #chama a função principal.
    "Função principal do programa"
    lista_de_tarefas = carregar_tarefas(NOME_ARQUIVO) #chama a função carregar tarefas, para obter a lista de tarefaas e arquivos armazenados.

    while True: #incia um loop até que o usuário decida sair do programa.
        mostrar_menu() #chama a função para exibir o menu de opções.
        escolha = input("Escolha uma opção (1~5): ")

        if escolha == '1': 
            adicionar_tarefa(lista_de_tarefas)
        elif escolha == '2':
            visualizar_tarefa(lista_de_tarefas)
        elif escolha == '3':
            remover_tarefas(lista_de_tarefas)
        elif escolha == '4':
            salvar_tarefas(NOME_ARQUIVO, lista_de_tarefas)
            print("Saindo do programa, até logo")
            break 
        elif escolha == '5':
            confirmar_saida = input("Tem certeza que deseja sair sem salvar? (s/n): ")
            if confirmar_saida.lower() == 's':
                print("Saindo do programa, até logo...")
                break
            else: 
                print("Retonando ao menu...")
                break
        else:
            print("Resposta inválida. Por favor, escolha uma opção válida (1~5).")
            input("Pressione enter para continuar...")

if __name__ == "__main__": #verifica se o arquivo está sendo executado corretamente.
        main() #chama o main que é a funão principal do programa.