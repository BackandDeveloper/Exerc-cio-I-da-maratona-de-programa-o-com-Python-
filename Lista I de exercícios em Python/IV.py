# Solicita os dados de entrada
hora_entrada = int(input("Hora de entrada: "))
minuto_entrada = int(input("Minuto de entrada: "))
hora_saida = int(input("Hora de saída: "))
minuto_saida = int(input("Minuto de saída: "))

# Calcula o tempo total de estacionamento em horas
tempo_total = (hora_saida + (minuto_saida / 60)) - (hora_entrada + (minuto_entrada / 60))

# Arredonda para cima para cobrar a hora cheia
import math
tempo_total = math.ceil(tempo_total)

# Calcula o valor a ser pago
if tempo_total <= 1:
    valor_a_pagar = 8.00
else:
    valor_a_pagar = 8.00 + (tempo_total - 1) * 1.00

# Exibe o valor a ser pago
print(f"O valor a ser pago pelo estacionamento é R$ {valor_a_pagar:.2f}")
