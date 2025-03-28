import json


def exibir_menu():
    print("=== CONTROLE DE ESTOQUE ===")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Alterar Quantidade")
    print("4. Remover Produto")
    print("5. Sair")




def adicionar_produto(lista, nome, quantidade, preco):
        dicionario_de_produtos = {}    
        dicionario_de_produtos['nome'] = nome
        dicionario_de_produtos['quantidade'] = quantidade
        dicionario_de_produtos['preco'] = preco
        lista.append(dicionario_de_produtos)
        print(f'produto {nome} registrado com sucesso')
        salvar_dados(lista)
    


def listar_produtos(lista):
    print('Lista de produtos')
    if lista:
        for indice, produto in enumerate(lista):
            print(f'indice: {indice} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: R${produto["preco"]}')
    else:
        print(f'Lista vazia')
        

def alterar_quantidade(indice_produto, lista, nova_quantidade, opcao_aumentar_diminuir):
        quantidade_atual = lista[indice_produto]['quantidade']  
        quantidade_a_remover = nova_quantidade
        if opcao_aumentar_diminuir == '+':
            lista[indice_produto]['quantidade'] += nova_quantidade
            salvar_dados(lista)
        elif opcao_aumentar_diminuir == '-':
            if quantidade_a_remover > quantidade_atual:
                print("Erro: Não é possível remover mais produtos do que o disponível.")
            else :
                lista[indice_produto]['quantidade'] -= nova_quantidade
                print(f"Quantidade atualizada: {lista[indice_produto]['quantidade']}")
                salvar_dados(lista)
        else:
            print(f'escolha invalida')
                     
                     
def remover_produto(indice_produto, lista):
    print(f'produto {lista[indice_produto]['nome']} removido com sucesso') 
    lista.pop(indice_produto)
    salvar_dados(lista)
    
    
def salvar_dados(Lista):
    with open('produtos.json', 'w') as arquivo:
        json.dump([produto for produto in Lista], arquivo, indent=4)
        

def carregar_dados():
    try:
        with open('produtos.json', 'r') as arquivo:
            lista_de_produtos = json.load(arquivo)
            return [produto for produto in lista_de_produtos]
    except (FileNotFoundError, json.JSONDecodeError):
        return []    
        
                        