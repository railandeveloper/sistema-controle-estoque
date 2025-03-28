from modulo import exibir_menu, adicionar_produto, listar_produtos, alterar_quantidade, remover_produto, carregar_dados
import time


lista_de_produtos = carregar_dados()

while True:
    print()
    exibir_menu()
    print()
    opcao_menu = input('Qual opcao voce escolhe?[1/ 2/ 3/ 4/ 5]: ')
    try:
        opcao_usuario = int(opcao_menu)
    except:
        print(f'digite um numero inteiro valido')
        continue
    
    
    if opcao_usuario == 1:
        print(f'Preencha os dados do produto')
        nome_produto = str(input(f'Digite o nome do produto: ')).strip().upper()
          
        while True:
            try:    
                quantidade_do_produto = int(input(f'digite a quantidade do produto {nome_produto}: '))
            except:
                print('digite a quantidade em formato numero inteiro')
                continue
            if quantidade_do_produto > 0:
                break
            else:
                print(f'a quantidade nao pode ser um numero negativo')
        
        while True:
            try:       
                preco_produto = float(input(f'Digite o preço do produto: '))
            except: 
                print('preco invalido')
                continue
            if preco_produto > 0:
                break    
        adicionar_produto(lista_de_produtos, nome_produto, quantidade_do_produto, preco_produto)
      
        
        
        
    elif opcao_usuario == 2:
        listar_produtos(lista_de_produtos)
        
    
    elif opcao_usuario == 3:
        if lista_de_produtos:
            print(f'escolha o indice do produto que vc gostaria de alterar_a_quantidade: ')
            listar_produtos(lista_de_produtos)
            while True:
                try:
                    indice_produto_alterar_quantidade = int(input('Digite o índice: '))
                    if 0 <= indice_produto_alterar_quantidade < len(lista_de_produtos):
                        break  
                    else:
                        print('Índice fora do alcance. Tente novamente.')
                except ValueError:
                    print('O índice deve ser um número inteiro válido.')
                
            aumentar_diminuir = str(input(f'Voce quer aumentar ou diminuir a quantidade do produto{lista_de_produtos[indice_produto_alterar_quantidade]} [+ para aumentar] ou [- para diminuir]: '))
            if aumentar_diminuir == '+':
                while True:
                    try:
                        qtd_aumentada = int(input(f'quanto produtos a mais voce esta adicionando para {lista_de_produtos[indice_produto_alterar_quantidade]}: '))
                    except:
                        print(f'digite um numero inteiro valido')
                        continue
                    if qtd_aumentada > 0:
                            break    
                alterar_quantidade(indice_produto_alterar_quantidade, lista_de_produtos, qtd_aumentada, aumentar_diminuir)
                
                    
            elif aumentar_diminuir == '-':
                while True:
                    try:
                        qtd_diminuida = int(input(f'quanto produtos voce quer remover de {lista_de_produtos[indice_produto_alterar_quantidade]}: '))
                    except:
                        print(f'digite um numero inteiro valido')
                        continue
                    if qtd_diminuida > 0 :
                        break
                    else:
                        print(f'nao e possivel diminuir essa quantidade')  
                alterar_quantidade(indice_produto_alterar_quantidade, lista_de_produtos, qtd_diminuida, aumentar_diminuir)
            else:
                print('A escolha deve ser entre [+ para aumentar] ou [- para diminuir] ')
        else:
            print(f'A Lista esta vazia')                   
    
         
    elif opcao_usuario == 4:
        if lista_de_produtos:
            listar_produtos(lista_de_produtos)
            print()
            print('digite o indice do produto que gostaria de remover')
            
            while True:
                try:
                    indice_produto_a_ser_removido = int(input('Digite o indice do produto a ser removido: '))
                except:
                    print(f'o indice deve ser um numero inteiro ')
                if indice_produto_a_ser_removido >=0 and indice_produto_a_ser_removido < len(lista_de_produtos):
                    remover_produto(indice_produto_a_ser_removido, lista_de_produtos)
                    break
                else:
                    print(f'digite um indice que exista na lista') 
        else:
            print('lista vazia')
    
    
    elif opcao_usuario == 5:
        print(f'Saindo do programa...')
        time.sleep(2)
        break
    
    
    else:
        print("\033[91mOpcao invalida.\033[0m")                                  
             