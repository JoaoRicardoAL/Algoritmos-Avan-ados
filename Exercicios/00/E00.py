# recebe a entrada do número de cadastros a serem feitos
cadastros = int(input())
estoque = {}

# Lê os cadastros e armazena-os no dicionário estoque, de forma unica
# Se o código já existir, informa que o produto já está cadastrado
for i in range(cadastros):
    codigo, preco = input().split()
    if codigo in estoque:
        print(f"Produto com código {codigo} já cadastrado.")
    else:
        estoque[codigo] = float(preco)

# Recebe a entrada do número de compras a serem feitas
compras = 0
while True:
    compras = int(input())
    if compras < 0:
        break
    else:
        # Recebe os códigos dos produtos e os pesos comprados, verifica se estão no estoque e calcula o preço total
        total = 0.0
        for i in range(compras):
            codigo, peso = input().split()
            if codigo in estoque:
                total += estoque[codigo] * float(peso)
            else:
                print(f"Produto com código {codigo} não cadastrado.")
        print(f"R${total:.2f}")
        
