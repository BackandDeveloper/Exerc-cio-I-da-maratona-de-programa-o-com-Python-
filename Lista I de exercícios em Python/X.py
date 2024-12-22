# Solicita os dados de entrada
idade = int(input("Idade: "))
tempo_contribuicao = int(input("Tempo de contribuição: "))

# Verifica se o trabalhador pode se aposentar
if idade >= 65 or tempo_contribuicao >= 30 or (idade >= 60 and tempo_contribuicao >= 25):
    print("Pode se aposentar")
else:
    print("Ainda não pode se aposentar")
