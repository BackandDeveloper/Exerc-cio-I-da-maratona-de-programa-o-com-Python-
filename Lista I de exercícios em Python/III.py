# Solicita os dados de entrada
preco_produto = float(input("Preço do produto: R$ "))
forma_pagamento = input("Forma de pagamento (À vista ou Parcelado): ")

# Calcula o valor a ser pago
if forma_pagamento.lower() == 'à vista':
    valor_a_pagar = preco_produto * 0.9
else:
    valor_a_pagar = preco_produto

# Exibe o valor a ser pago
print(f"O valor a ser pago pelo produto é R$ {valor_a_pagar:.2f}")
