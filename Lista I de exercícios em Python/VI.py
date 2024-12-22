# Solicita os dados de entrada
valor_emprestimo = float(input("Valor do empréstimo: "))
numero_parcelas = int(input("Número de parcelas: "))
salario = float(input("Salário: "))

# Calcula o valor das parcelas
valor_parcela = valor_emprestimo / numero_parcelas

# Verifica se o empréstimo pode ser aprovado
if valor_parcela <= salario * 0.30:
    print("Empréstimo aprovado")
    print(f"Valor do empréstimo: R$ {valor_emprestimo:.2f}")
    print(f"Número de parcelas: {numero_parcelas}")
    print(f"Valor das parcelas: R$ {valor_parcela:.2f}")
else:
    print("Empréstimo não aprovado")
