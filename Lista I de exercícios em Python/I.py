# Preços dos combustíveis
preco_gasolina = 5.89
preco_alcool = 4.99

# Dados fornecidos pelo usuário
tipo_combustivel = input("Tipo de combustível (G para gasolina, A para álcool): ")
quantidade_litros = float(input("Quantidade de litros: "))

# Cálculo do valor a ser pago
if tipo_combustivel == 'G':
    valor_total = quantidade_litros * preco_gasolina
else:
    valor_total = quantidade_litros * preco_alcool

# Exibição do valor a ser pago
print(f"O valor a ser pago pelo abastecimento é R$ {valor_total:.2f}")