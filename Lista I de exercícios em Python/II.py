# Solicita os dados de entrada
altura = float(input("Altura (em metros): "))
sexo = input("Sexo (M para masculino, F para feminino): ")

# Calcula o peso ideal
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

# Exibe o peso ideal
print(f"O peso ideal é {peso_ideal:.2f} kg")