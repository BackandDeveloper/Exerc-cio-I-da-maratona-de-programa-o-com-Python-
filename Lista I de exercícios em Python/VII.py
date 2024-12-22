# Solicita os dados de entrada
hora_inicio = int(input("Hora de início: "))
hora_fim = int(input("Hora de fim: "))

# Calcula a duração da partida
if hora_fim >= hora_inicio:
    duracao = hora_fim - hora_inicio
else:
    duracao = (24 - hora_inicio) + hora_fim

# Exibe a duração da partida
print(f"Duração da partida: {duracao}h")
