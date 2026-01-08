import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True}, {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}] #lista de dicionários

def exibir_nome_app():
    print("""
𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼
    """)

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulos('Finalizando o app...\n')

def voltar_menu():
    input('\nPressione Enter para voltar ao menu principal:')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4) 
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''
    Função respon´savel por cadastrar um restaurante.

    Inputs:
    - nome: nome do restaurante a ser cadastrado.
    - categoria: categoria do restaurante a ser cadastrado.
    
    Output:
    - Adiciona um novo restaurante na lista de restaurantes com o status inativo.
    '''
    exibir_subtitulos('Cadastrar Restaurante\n')
    nome = input(f'Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante "{nome}": ')
    dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False} #regra: todo restaurante criado na plataforma inicia como inativo
    restaurantes.append(dados_restaurante)
    print(f'Restaurante "{nome}" cadastrado com sucesso!\n')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulos('Lista de restaurantes:\n')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado' 
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_menu()

def alternar_estado_restaurante():
    exibir_subtitulos('Alternando estado do restaurante:\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante "{nome_restaurante}" foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante "{nome_restaurante}" foi desativado com sucesso!' #ternário
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado na plataforma.')
    voltar_menu()

def escolher_opcao():   
    try:
        op = int (input('Escolha uma opção: '))

        if op == 1:
            cadastrar_restaurante()
        elif op == 2:
            listar_restaurantes()
        elif op == 3:
            alternar_estado_restaurante()
        elif op == 4:
            finalizar_app()
        else:
            opcao_invalida()
            listar_restaurantes()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
