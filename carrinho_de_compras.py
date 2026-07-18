carrinho = {}

sair = False
while not sair:
    print("\n---Bem vindo ao Carrinho de Compras---")
    print("Digite (1) para Adicionar produto e quantidade")
    print("Digite (2) para Atualizar quantidade de um item")
    print("Digite (3) para Remover produto do carrinho")    
    print("Digite (4) para Exibir o carrinho")
    print("Digite (5) para sair")
    escolha = input("> ")


    if escolha == '1':
        produto = input("Digite o produto que ira comprar: ")
        quantidade = int(input("Digite a quantidade: "))    
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade
    elif escolha == '2':
        produto = input('Digite o produto que ira atualizar: ')
        if produto not in carrinho:
            print('Este produto nao esta no seu carrinho para ser atualizado')
        else:
            quantidade_nova = int(input('Qual sera a nova quantidade: '))
            if quantidade_nova > 0:
                carrinho[produto] = quantidade_nova
            else:
                print('Quantidade invalida')
    elif escolha == '3':
        produto_a_deletar = input('Qual produto sera tirado: ')
        if produto_a_deletar in carrinho:
            del carrinho[produto_a_deletar]
        else:
            print('este produto nao esta no seu carrinho')
    elif escolha == '4':
        if carrinho != {}:
            for p, q in carrinho.items():   
                print(p)
                print(q)
        else:
            print('Seu carrinho esta vazio')
    elif escolha == '5':
        sair = True
    else:
        print("Escolha invalida")