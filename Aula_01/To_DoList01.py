
# -----------------------------------------------------------------------------
# Projeto: To-Do List no Terminal
# Conceitos: listas, entrada de usuário, menu com while, funções,
#            persistência com arquivos .txt
# -----------------------------------------------------------------------------

import os # Importa o módulo 'os' para interagir com o sistema operacional, usado aqui para limpar o terminal.

NOME_ARQUIVO = "tarefas.txt" # Define uma constante para o nome do arquivo onde as tarefas serão salvas.

def limpar_terminal(): # Define uma função chamada 'limpar_terminal'.
    """Limpa a tela do terminal.""" # Docstring explicando o que a função faz.
    os.system('cls' if os.name == 'nt' else 'clear') # Executa o comando 'cls' se o sistema for Windows ('nt'), ou 'clear' para outros sistemas (Linux, macOS) para limpar o terminal.

def carregar_tarefas(nome_arquivo): # Define uma função chamada 'carregar_tarefas' que recebe 'nome_arquivo' como argumento.
    """Carrega as tarefas de um arquivo .txt.""" # Docstring da função.
    tarefas = [] # Inicializa uma lista vazia chamada 'tarefas' para armazenar as tarefas lidas do arquivo.
    try: # Inicia um bloco 'try' para tratamento de exceções (erros) que podem ocorrer ao tentar ler o arquivo.
        with open(nome_arquivo, 'r', encoding='utf-8') as f: # Abre o arquivo especificado por 'nome_arquivo' em modo de leitura ('r') com codificação 'utf-8'.
                                                             # O 'with' garante que o arquivo será fechado automaticamente. 'f' é o objeto do arquivo.
            for linha in f: # Itera sobre cada linha no arquivo 'f'.
                tarefas.append(linha.strip()) # Remove espaços em branco do início e fim da 'linha' (usando strip()) e adiciona a linha à lista 'tarefas'.
        print(f"Tarefas carregadas de '{nome_arquivo}'.") # Informa ao usuário que as tarefas foram carregadas.
    except FileNotFoundError: # Se o arquivo não for encontrado (exceção 'FileNotFoundError').
        print(f"Arquivo '{nome_arquivo}' não encontrado. Começando com lista vazia.") # Informa ao usuário e continua com a lista vazia.
    except Exception as e: # Captura qualquer outra exceção que possa ocorrer durante a leitura. 'e' contém informações sobre o erro.
        print(f"Ocorreu um erro ao carregar as tarefas: {e}") # Informa sobre o erro.
    return tarefas # Retorna a lista de tarefas (pode estar vazia se o arquivo não existir ou houver erro).

def salvar_tarefas(tarefas, nome_arquivo): # Define uma função chamada 'salvar_tarefas' que recebe a lista 'tarefas' e 'nome_arquivo'.
    """Salva as tarefas em um arquivo .txt.""" # Docstring da função.
    try: # Inicia um bloco 'try' para tratamento de exceções ao salvar o arquivo.
        with open(nome_arquivo, 'w', encoding='utf-8') as f: # Abre o arquivo em modo de escrita ('w'), o que sobrescreverá o conteúdo existente ou criará um novo arquivo.
                                                             # Usa codificação 'utf-8'.
            for tarefa in tarefas: # Itera sobre cada 'tarefa' na lista 'tarefas'.
                f.write(tarefa + "\n") # Escreve a 'tarefa' no arquivo, seguida por um caractere de nova linha ('\n') para que cada tarefa fique em uma linha separada.
        print(f"Tarefas salvas em '{nome_arquivo}'.") # Informa que as tarefas foram salvas.
    except Exception as e: # Captura qualquer exceção que possa ocorrer durante a escrita.
        print(f"Ocorreu um erro ao salvar as tarefas: {e}") # Informa sobre o erro.

def adicionar_tarefa(tarefas): # Define uma função chamada 'adicionar_tarefa' que recebe a lista 'tarefas'.
    """Adiciona uma nova tarefa à lista.""" # Docstring da função.
    limpar_terminal() # Chama a função para limpar a tela do terminal.
    print("--- Adicionar Nova Tarefa ---") # Imprime um cabeçalho para a seção.
    nova_tarefa = input("Digite a descrição da tarefa: ").strip() # Pede ao usuário para digitar a descrição da tarefa e remove espaços extras com strip().
    if nova_tarefa: # Verifica se 'nova_tarefa' não está vazia (se o usuário digitou algo).
        tarefas.append(nova_tarefa) # Adiciona a 'nova_tarefa' à lista 'tarefas'.
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!") # Informa que a tarefa foi adicionada.
    else: # Se 'nova_tarefa' estiver vazia.
        print("Nenhuma tarefa adicionada. A descrição não pode ser vazia.") # Informa que a tarefa não foi adicionada.
    input("\nPressione Enter para continuar...") # Pausa o programa até o usuário pressionar Enter.

def visualizar_tarefas(tarefas): # Define uma função chamada 'visualizar_tarefas' que recebe a lista 'tarefas'.
    """Exibe todas as tarefas da lista.""" # Docstring da função.
    limpar_terminal() # Limpa a tela do terminal.
    print("--- Suas Tarefas ---") # Imprime um cabeçalho.
    if not tarefas: # Verifica se a lista 'tarefas' está vazia.
        print("Nenhuma tarefa na lista.") # Informa que não há tarefas.
    else: # Se a lista não estiver vazia.
        for i, tarefa in enumerate(tarefas, start=1): # Itera sobre a lista 'tarefas' usando 'enumerate' para obter o índice (começando em 1 com 'start=1') e o valor.
            print(f"{i}. {tarefa}") # Imprime o número da tarefa (i) e a descrição da tarefa.
    input("\nPressione Enter para continuar...") # Pausa o programa.

def remover_tarefa(tarefas): # Define uma função chamada 'remover_tarefa' que recebe a lista 'tarefas'.
    """Remove uma tarefa da lista.""" # Docstring da função.
    limpar_terminal() # Limpa a tela.
    print("--- Remover Tarefa ---") # Imprime um cabeçalho.
    if not tarefas: # Verifica se a lista 'tarefas' está vazia.
        print("Nenhuma tarefa para remover.") # Informa que não há tarefas.
        input("\nPressione Enter para continuar...") # Pausa.
        return # Sai da função, pois não há o que remover.

    for i, tarefa in enumerate(tarefas, start=1): # Itera e exibe as tarefas numeradas para o usuário.
        print(f"{i}. {tarefa}") # Imprime cada tarefa com seu número.

    while True: # Inicia um loop infinito que só será quebrado por um 'break'.
        try: # Inicia um bloco 'try' para lidar com entrada inválida do usuário.
            num_tarefa_str = input("\nDigite o número da tarefa a ser removida (ou 0 para cancelar): ") # Pede ao usuário o número da tarefa.
            num_tarefa = int(num_tarefa_str) # Tenta converter a entrada do usuário (string) para um número inteiro.

            if num_tarefa == 0: # Se o usuário digitou 0.
                print("Remoção cancelada.") # Informa que a remoção foi cancelada.
                break # Sai do loop 'while'.
            elif 1 <= num_tarefa <= len(tarefas): # Verifica se o número digitado está dentro do intervalo válido de tarefas.
                tarefa_removida = tarefas.pop(num_tarefa - 1) # Remove a tarefa da lista usando 'pop()'.
                                                              # 'num_tarefa - 1' porque as listas são indexadas a partir de 0, mas o usuário vê a partir de 1.
                                                              # 'pop()' remove o item e o retorna, então o guardamos em 'tarefa_removida'.
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!") # Informa que a tarefa foi removida.
                break # Sai do loop 'while'.
            else: # Se o número for inválido (fora do intervalo).
                print("Número inválido. Por favor, digite um número da lista.") # Pede para o usuário tentar novamente.
        except ValueError: # Se a conversão para 'int' falhar (ex: usuário digitou texto).
            print("Entrada inválida. Por favor, digite um número.") # Informa sobre a entrada inválida.
        except Exception as e: # Captura outros possíveis erros.
            print(f"Ocorreu um erro: {e}") # Informa sobre o erro.
    input("\nPressione Enter para continuar...") # Pausa o programa.

def mostrar_menu(): # Define uma função chamada 'mostrar_menu'.
    """Exibe o menu de opções.""" # Docstring da função.
    limpar_terminal() # Limpa a tela do terminal.
    print("\n--- To-Do List no Terminal ---") # Imprime o título do menu.
    print("1. Adicionar Tarefa") # Opção 1 do menu.
    print("2. Visualizar Tarefas") # Opção 2 do menu.
    print("3. Remover Tarefa") # Opção 3 do menu.
    print("4. Salvar e Sair") # Opção 4 do menu.
    print("5. Sair sem Salvar") # Opção 5 do menu.

def main(): # Define a função principal do programa, chamada 'main'.
    """Função principal do programa.""" # Docstring da função.
    lista_de_tarefas = carregar_tarefas(NOME_ARQUIVO) # Chama 'carregar_tarefas' para obter a lista de tarefas do arquivo e armazena em 'lista_de_tarefas'.

    while True: # Inicia o loop principal do programa, que continuará até o usuário decidir sair.
        mostrar_menu() # Chama a função para exibir o menu de opções.
        escolha = input("Escolha uma opção: ") # Pede ao usuário para digitar sua escolha.

        if escolha == '1': # Se a escolha for '1'.
            adicionar_tarefa(lista_de_tarefas) # Chama a função para adicionar uma tarefa, passando a lista atual.
        elif escolha == '2': # Se a escolha for '2'.
            visualizar_tarefas(lista_de_tarefas) # Chama a função para visualizar as tarefas.
        elif escolha == '3': # Se a escolha for '3'.
            remover_tarefa(lista_de_tarefas) # Chama a função para remover uma tarefa.
        elif escolha == '4': # Se a escolha for '4'.
            salvar_tarefas(lista_de_tarefas, NOME_ARQUIVO) # Chama a função para salvar as tarefas no arquivo.
            print("Saindo do programa. Até logo!") # Mensagem de despedida.
            break # Quebra o loop 'while True', encerrando o programa.
        elif escolha == '5': # Se a escolha for '5'.
            confirmar_saida = input("Tem certeza que deseja sair sem salvar? (s/n): ").lower() # Pede confirmação para sair sem salvar, convertendo a resposta para minúsculas.
            if confirmar_saida == 's': # Se o usuário confirmar com 's'.
                print("Saindo do programa sem salvar. Até logo!") # Mensagem de despedida.
                break # Quebra o loop 'while True', encerrando o programa.
            else: # Se o usuário não confirmar com 's'.
                print("Retornando ao menu.") # Informa que está retornando ao menu.
                input("\nPressione Enter para continuar...") # Pausa.
        else: # Se a escolha não for nenhuma das opções válidas.
            print("Opção inválida. Tente novamente.") # Informa que a opção é inválida.
            input("\nPressione Enter para continuar...") # Pausa.

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (e não importado como módulo).
    main() # Chama a função 'main' para iniciar o programa.
