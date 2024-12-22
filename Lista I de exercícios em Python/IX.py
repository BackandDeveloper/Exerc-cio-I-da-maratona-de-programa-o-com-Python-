# Solicita os dados de entrada
numero_bino = int(input("Número de Bino: "))
numero_mariazinha = int(input("Número de Mariazinha: "))

# Calcula a soma dos números
soma = numero_bino + numero_mariazinha

# Verifica se a soma é par ou ímpar e determina o vencedor
if soma % 2 == 0:
    vencedor = "Mariazinha ganhou!"
else:
    vencedor = "Bino ganhou!"

# Exibe o resultado
print(vencedor)
