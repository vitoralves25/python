listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')

# 2f - Para ter duas casas decimais

# :>7 - Joga o Elemento pra direita

#:<30 - Joga o elemento pra esquerda

#:^30 - Centraliza o Elemento

# Final
