import random

print("Felipe da Silva Bertoni Castelão")
print("Instagram: @_fbertoni")

# Solicita o valor mínimo e máximo
min_val = int(input("Digite o valor mínimo: "))
max_val = int(input("Digite o valor máximo: "))

# Verifica se os valores estão corretos
while min_val > max_val:
    print("O valor mínimo deve ser menor que o valor máximo. Tente novamente.")
    min_val = int(input("Digite o valor mínimo: "))
    max_val = int(input("Digite o valor máximo: "))


sorteio = random.randrange(min_val, max_val + 1)

lista = []
tentativa = 0
palpite = None

# Loop de adivinhação
while palpite != sorteio:
    palpite = int(input("Digite o seu palpite: "))
    lista.append(palpite)
    tentativa += 1

    if palpite > sorteio:
        print("Digite um valor menor.")
    elif palpite < sorteio:
        print("Digite um valor maior.")
    else:
        print("Acertou!")
        print(f"Foram {tentativa} palpites até você acertar.")
        print(f"Seus palpites foram esses: {lista}")
