import random

def mostrar_titulo():
    """Exibe o título principal do jogo."""
    print("\n" + "=" * 60)
    print("🎯 DESAFIO DO NÚMERO MISTERIOSO 🎯".center(60))
    print("=" * 60 + "\n")


def pedir_palpite(tentativa, max_tentativas):
    """Lê e valida o palpite do jogador."""
    while True:
        try:
            numero = int(input(f"Tentativa {tentativa}/{max_tentativas} → Escolha um número entre 1 e 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("⚠️  O número deve estar entre 1 e 100!\n")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.\n")


def rodada_jogo():
    """Executa uma rodada do jogo de adivinhação."""
    mostrar_titulo()

    secreto = random.randint(1, 100)
    max_tentativas = 8

    for tentativa in range(1, max_tentativas + 1):
        palpite = pedir_palpite(tentativa, max_tentativas)

        if palpite == secreto:
            print("\n🎉 PARABÉNS! Você adivinhou o número secreto!")
            print(f"🔢 Número secreto: {secreto}")
            print(f"💪 Tentativas usadas: {tentativa}\n")
            break
        elif palpite < secreto:
            print("⬆️  Muito baixo! Tente um número MAIOR.\n")
        else:
            print("⬇️  Muito alto! Tente um número MENOR.\n")

        if tentativa == max_tentativas:
            print("\n😢 Suas tentativas acabaram!")
            print(f"🔐 O número secreto era {secreto}.\n")


def iniciar_jogo():
    """Controla o fluxo principal do jogo."""
    while True:
        rodada_jogo()
        jogar_novamente = input("🔁 Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente not in ("s", "sim"):
            print("\n👋 Obrigado por jogar o DESAFIO DO NÚMERO MISTERIOSO!")
            print("Até a próxima rodada!\n")
            break


if __name__ == "__main__":
    iniciar_jogo()
