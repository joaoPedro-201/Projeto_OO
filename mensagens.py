from time import sleep
from colorama import Fore, Style


def mostrar_resultado(nome1, jogada1, nome2, jogada2, vencedor):
    print(f"{nome1} escolheu: {jogada1}")
    print(f"{nome2} escolheu: {jogada2}")
    if vencedor == "jogador":
        print(Fore.GREEN + "🎉 Você venceu!" + Style.RESET_ALL)
    elif vencedor == "maquina":
        print(Fore.RED + "💔 A máquina venceu!" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "🤝 Empate!" + Style.RESET_ALL)
    sleep(1)


def mostrar_menu():
    print("Escolha o nível de dificuldade:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")
    escolha = input("Digite sua escolha (1/2/3): ").strip()
    while escolha not in ["1", "2", "3"]:
        escolha = input("Escolha inválida. Digite 1, 2 ou 3: ").strip()
    return {"1": "Fácil", "2": "Médio", "3": "Difícil"}[escolha]
