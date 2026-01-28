import csv
import os

ARQUIVO = 'financas.csv'


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#VERIFICA SE O ARQUIVO JÁ EXISTE
def verificar_arquivo_existe():

    return os.path.exists(ARQUIVO)


def registro_transacao():

    transacao = {}

    while True:
        limpar_tela()
        print('\n ---- REGISTRAR NOVA TRANSAÇÃO ----')
        try:
            tipo_input = int(input('TIPO DE REGISTRO:\n [1] RECEITA\n [2] DESPESA\nEscolha: '))
            if tipo_input == 1:
                transacao['tipo'] = 'RECEITA'
                break
            elif tipo_input == 2:
                transacao['tipo'] = 'DESPESA'
                break
            else:
                print('ERRO! DIGITE APENAS 1 OU 2')
                input('Enter para tentar novamente...')
        except ValueError:
            print('ERRO! Digite um número inteiro.')
            input('Enter para tentar novamente...')

    transacao['descricao'] = str(input('DIGITE UMA BREVE DESCRIÇÃO: ')).upper().strip()

    while True:
        try:
            valor = float(input('INFORME O VALOR DE R$: '))
            if valor > 0:
                transacao['valor'] = valor
                break
            print('VALOR DEVE SER POSITIVO.')
        except ValueError:
            print('POR FAVOR, DIGITE UM VALOR VÁLIDO!')

    return transacao


def salvar_transacao(nova_transacao):
    arquivo_existe = verificar_arquivo_existe()

    with open(ARQUIVO, mode='a', newline='', encoding='utf-8') as file:
        campos = ['tipo', 'descricao', 'valor']
        escritor = csv.DictWriter(file, fieldnames=campos)


        if not arquivo_existe:
            escritor.writeheader()


        escritor.writerow(nova_transacao)

    print(f'\n✅ {nova_transacao["tipo"]} SALVA COM SUCESSO!')
    input('Pressione ENTER para continuar...')

#FUNÇÃO PARA APAGAR ALGUM ITEM
def excluir_registro():
    limpar_tela()

    # 1. Verifica se tem o que apagar
    if not verificar_arquivo_existe():
        print("Nenhum registro para apagar.")
        input('Enter para voltar...')
        return

    # 2. Carrega TUDO para a memória
    lista_transacoes = []
    with open(ARQUIVO, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        lista_transacoes = list(leitor)  # Converte para uma lista Python normal

    if not lista_transacoes:  # Se a lista estiver vazia (mas arquivo existe)
        print("O arquivo está vazio.")
        input('Enter para voltar...')
        return

    # 3. Mostra as opções com um índice (0, 1, 2...)
    print("\n--- SELECIONE O ID PARA APAGAR ---")
    print(f"{'ID':<4} | {'TIPO':<10} | {'DESCRIÇÃO':<20} | {'VALOR':<10}")
    print("-" * 50)

    for i, item in enumerate(lista_transacoes):
        print(f"{i:<4} | {item['tipo']:<10} | {item['descricao']:<20} | R$ {item['valor']}")

    # 4. Pergunta qual apagar
    try:
        print("-" * 50)
        index_para_apagar = int(input("Digite o número do ID para apagar (ou -1 para cancelar): "))

        if index_para_apagar == -1:
            return

        if 0 <= index_para_apagar < len(lista_transacoes):

            removido = lista_transacoes.pop(index_para_apagar)


            with open(ARQUIVO, mode='w', newline='', encoding='utf-8') as file:
                campos = ['tipo', 'descricao', 'valor']
                escritor = csv.DictWriter(file, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(lista_transacoes)  # Escreve a lista inteira de uma vez

            print(f"\n✅ Item '{removido['descricao']}' apagado com sucesso!")
        else:
            print("❌ ID inválido!")

    except ValueError:
        print("❌ Digite um número válido.")

    input('Pressione ENTER para continuar...')

#FUNÇÃO PRA LER O ARQUIVO E MOSTRAR NA TELA
def ler_arquivo():

    limpar_tela()
    if not verificar_arquivo_existe():
        print("NENHUM REGISTRO ENCONTRADO.")
        input('Enter para voltar...')
        return

    print("\n--- EXTRATO DETALHADO ---")
    print(f"{'TIPO':<10} | {'DESCRIÇÃO':<20} | {'VALOR':<10}")
    print("-" * 45)

    with open(ARQUIVO, mode='r', newline='', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:

            print(f"{linha['tipo']:<10} | {linha['descricao']:<20} | R$ {float(linha['valor']):.2f}")

    input('\nPressione ENTER para voltar...')


def calcular_saldo():

    limpar_tela()
    if not verificar_arquivo_existe():
        print("Nenhum registro para calcular.")
        input('Enter para voltar...')
        return

    total_receita = 0.0
    total_despesa = 0.0

    with open(ARQUIVO, mode='r', newline='', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            valor = float(linha['valor'])
            if linha['tipo'] == 'RECEITA':
                total_receita += valor
            elif linha['tipo'] == 'DESPESA':
                total_despesa += valor

    saldo = total_receita - total_despesa

    print("\n--- BALANÇO FINANCEIRO ---")
    print(f"TOTAL RECEITAS:  R$ {total_receita:.2f}")
    print(f"TOTAL DESPESAS:  R$ {total_despesa:.2f}")
    print("-" * 30)
    print(f"SALDO FINAL:     R$ {saldo:.2f}")

    input('\nPressione ENTER para voltar...')


# --- PROGRAMA PRINCIPAL INTERAÇÃO COM O USUARIO ---
while True:
    limpar_tela()
    print("SISTEMA DE CONTROLE FINANCEIRO")
    print('-' * 30)
    print('[1] NOVO REGISTRO')
    print('[2] EXTRATO')
    print('[3] VER SALDO')
    print('[4] APAGAR REGISTRO')
    print('[5] SAIR')
    print('-' * 30)

    try:
        opcao = int(input('DIGITE O QUE VOCÊ DESEJA FAZER: '))

        if opcao == 1:

            dados = registro_transacao()

            salvar_transacao(dados)

        elif opcao == 2:
            ler_arquivo()

        elif opcao == 3:
            calcular_saldo()

        elif opcao == 4:
            excluir_registro()

        elif opcao == 5:
            print('Salvando dados e encerrando... Até logo!')
            break

        else:
            print('OPÇÃO INVÁLIDA')
            input('Pressione ENTER para tentar novamente')

    except ValueError:
        print('Por favor, digite apenas números.')
        input('Enter para continuar...')