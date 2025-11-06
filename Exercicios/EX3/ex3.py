def limpar_tela():
    """Limpa a tela simulando várias quebras de linha."""
    print("\n" * 6)


def exibir_cabecalho():
    """Mostra o cabeçalho da urna eletrônica."""
    print("=" * 60)
    print("🗳️  ELEIÇÕES GRANTIETÊ 2025 - URNA ELETRÔNICA")
    print("=" * 60)


def votar(candidatos, numero_aluno, votantes, votos, extras):
    """Processa o voto de um aluno, com validações e confirmação."""
    if numero_aluno in votantes:
        print("⚠️  Este aluno já votou! Não é permitido votar novamente.")
        return

    while True:
        try:
            escolha = int(input("Digite o número do candidato (ou 0 para Branco): "))
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")
            continue

        # --- Voto válido ---
        if escolha in candidatos:
            nome_candidato = candidatos[escolha]
            confirmar = input(f"Confirma seu voto em '{nome_candidato}'? (sim/não): ").strip().lower()
            if confirmar == "sim":
                votos[escolha] += 1
                votantes.append(numero_aluno)
                print("✅ Voto computado com sucesso!")
                break
            else:
                print("↩️  Voto cancelado. Escolha novamente.")

        # --- Voto em branco ---
        elif escolha == 0:
            confirmar = input("Confirma seu voto em BRANCO? (sim/não): ").strip().lower()
            if confirmar == "sim":
                extras["brancos"] += 1
                votantes.append(numero_aluno)
                print("🟦 Voto registrado como BRANCO.")
                break
            else:
                print("↩️  Voto cancelado. Escolha novamente.")

        # --- Voto nulo ---
        else:
            confirmar = input("Confirma seu voto NULO? (sim/não): ").strip().lower()
            if confirmar == "sim":
                extras["nulos"] += 1
                votantes.append(numero_aluno)
                print("🟥 Voto registrado como NULO.")
                break
            else:
                print("↩️  Voto cancelado. Escolha novamente.")


def exibir_resultado(candidatos, votos, extras):
    """Exibe o resultado final da eleição."""
    limpar_tela()
    print("=" * 60)
    print("📊 RESULTADO DAS ELEIÇÕES GRANTIETÊ 2025")
    print("=" * 60)

    total_validos = sum(votos.values())
    total_geral = total_validos + extras["brancos"] + extras["nulos"]

    print(f"\n🗳️  Total de votos computados: {total_geral}")
    print("-" * 60)
    print("📋 Votos por candidato:")

    vencedor = None
    maior_votacao = -1

    for numero, nome in candidatos.items():
        qtd = votos[numero]
        percentual = (qtd / total_validos * 100) if total_validos > 0 else 0
        print(f"• {nome}: {qtd} voto(s) ({percentual:.1f}%)")

        if qtd > maior_votacao:
            maior_votacao = qtd
            vencedor = nome

    print("\n⚪ Votos em branco:", extras["brancos"])
    print("⚫ Votos nulos:", extras["nulos"])
    print("-" * 60)

    if vencedor:
        nome_final = vencedor.split("-")[0].strip()
        print(f"🏆 Candidato vencedor: {nome_final} ({maior_votacao} voto(s))")
    else:
        print("❌ Nenhum voto válido foi registrado.")


def executar_urna():
    """Função principal que coordena o processo de votação."""
    candidatos = {
        13: "Márcio - Partido da Tecnologia (PT)",
        35: "Capella - Partido dos Matemáticos (PM)",
        51: "Gallo - Partido da Coordenação (PC)",
        60: "José Mangili - Partido das Arquiteturas de Computador (PAC)"
    }

    votos = {num: 0 for num in candidatos}
    extras = {"brancos": 0, "nulos": 0}
    votantes = []

    while True:
        exibir_cabecalho()
        entrada = input("Digite o número do aluno (ou 0 para encerrar): ").strip()

        if not entrada.isdigit():
            print("⚠️  Digite apenas números!")
            continue

        numero_aluno = int(entrada)

        if numero_aluno == 0:
            print("\n🧮 Encerrando votação e apurando resultados...\n")
            break

        votar(candidatos, numero_aluno, votantes, votos, extras)
        limpar_tela()

    exibir_resultado(candidatos, votos, extras)


if __name__ == "__main__":
    executar_urna()
