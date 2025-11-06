from collections import deque

def fazer_pergunta(texto: str) -> bool:
    """Faz uma pergunta ao usuário e retorna True para 'sim' e False para 'não'."""
    while True:
        resposta = input(f"{texto} (sim/não): ").strip().lower()
        if resposta in ("sim", "s"):
            return True
        elif resposta in ("não", "nao", "n"):
            return False
        else:
            print("❌ Resposta inválida. Digite apenas 'sim' ou 'não'.")


def adivinhar_animal() -> str:
    """Executa o jogo de adivinhação de animais com base em perguntas lógicas."""
    print("\n🔍 Vamos tentar descobrir qual animal você está pensando!\n")

    # --- Mamíferos ---
    if fazer_pergunta("O animal é um mamífero?"):
        if fazer_pergunta("Ele tem quatro patas?"):
            if fazer_pergunta("Ele se alimenta de carne?"):
                return "Leão"
            else:
                return "Cavalo"
        elif fazer_pergunta("Ele anda sobre duas pernas?"):
            if fazer_pergunta("Ele come tanto carne quanto vegetais?"):
                return "Ser humano"
            else:
                return "Macaco"
        elif fazer_pergunta("Ele é capaz de voar?"):
            return "Morcego"
        else:
            return "Baleia"

    # --- Aves ---
    elif fazer_pergunta("O animal é uma ave?"):
        if fazer_pergunta("Ela não consegue voar?"):
            if fazer_pergunta("Ela vive em regiões quentes?"):
                return "Avestruz"
            else:
                return "Pinguim"
        elif fazer_pergunta("Ela nada com frequência?"):
            return "Pato"
        else:
            return "Águia"

    # --- Répteis ---
    elif fazer_pergunta("O animal é um réptil?"):
        if fazer_pergunta("Ele possui casco?"):
            return "Tartaruga"
        elif fazer_pergunta("Ele é carnívoro?"):
            return "Crocodilo"
        else:
            return "Cobra"

    else:
        return "Animal desconhecido 🐾"


def exibir_historico(historico: deque):
    """Mostra os últimos 10 animais descobertos."""
    print("\n📜 HISTÓRICO DOS ÚLTIMOS ANIMAIS IDENTIFICADOS:")
    if not historico:
        print("Ainda não há registros.")
    else:
        for i, animal in enumerate(historico, start=1):
            print(f"{i}. {animal}")


def exibir_menu():
    """Mostra o menu principal do jogo."""
    print("\n=== MENU PRINCIPAL ===")
    print("1 – Jogar")
    print("2 – Ver últimos animais identificados")
    print("3 – Sair")


def iniciar_jogo():
    """Função principal que gerencia o menu e as interações."""
    historico = deque(maxlen=10)

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            animal = adivinhar_animal()
            print(f"\n✅ O animal identificado foi: {animal}\n")
            historico.append(animal)

        elif escolha == "2":
            exibir_historico(historico)

        elif escolha == "3":
            print("\n👋 Encerrando o jogo. Até a próxima!\n")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_jogo()
