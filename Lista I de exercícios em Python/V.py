# Solicita os dados de entrada
salario = float(input("Salário: "))
tempo_servico = int(input("Tempo de serviço (em anos): "))

# Calcula o valor do bônus
if tempo_servico >= 5:
    bonus = salario * 0.20
else:
    bonus = salario * 0.10

# Exibe o valor do bônus
print(f"Bônus: R$ {bonus:.2f}")
