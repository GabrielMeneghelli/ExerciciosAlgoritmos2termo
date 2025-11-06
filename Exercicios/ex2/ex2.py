from typing import List

def ler_inteiro(mensagem: str, minimo: int | None = None) -> int:
    """Lê um número inteiro com verificação de erros."""
    while True:
        try:
            numero = int(input(mensagem))
            if minimo is not None and numero < minimo:
                print(f"⚠️  Valor inválido! O número deve ser maior ou igual a {minimo}.")
                continue
            return numero
        except ValueError:
            print("❌ Entrada inválida. Digite um número inteiro.")


def ler_decimal(mensagem: str, minimo: float | None = None) -> float:
    """Lê um número decimal (float) com verificação de erros."""
    while True:
        try:
            numero = float(input(mensagem))
            if minimo is not None and numero < minimo:
                print(f"⚠️  O valor deve ser maior ou igual a {minimo}.")
                continue
            return numero
        except ValueError:
            print("❌ Valor inválido. Digite um número decimal válido.")


def escolher_genero() -> str:
    """Lê e valida o gênero informado pelo usuário."""
    while True:
        genero = input("Informe o gênero (homem / mulher / não informado): ").strip().lower()
        if genero in ("homem", "mulher"):
            return genero
        elif genero in ("não informado", "nao informado"):
            return "não informado"
        else:
            print("⚠️  Opção inválida. Digite apenas 'homem', 'mulher' ou 'não informado'.")


def resumo_residencia(num_residencia: int, qtd_pessoas: int, soma_idades: int,
                      salarios_homens: List[float], salarios_mulheres: List[float]):
    """Mostra um pequeno relatório de uma residência."""
    media_idades = soma_idades / qtd_pessoas if qtd_pessoas else 0
    media_sal_homens = sum(salarios_homens) / len(salarios_homens) if salarios_homens else 0
    media_sal_mulheres = sum(salarios_mulheres) / len(salarios_mulheres) if salarios_mulheres else 0

    print(f"\n🏠 RESIDÊNCIA {num_residencia}")
    print(f"👥 Pessoas na casa: {qtd_pessoas}")
    print(f"📊 Média de idades: {media_idades:.1f} anos")
    print(f"💰 Média salarial (homens): R$ {media_sal_homens:.2f}")
    print(f"💰 Média salarial (mulheres): R$ {media_sal_mulheres:.2f}\n")


def executar_censo():
    """Executa o levantamento demográfico de forma interativa."""
    print("\n📋 CENSO DEMOGRÁFICO 2025\n")

    total_casas = total_pessoas = soma_idades_geral = 0
    total_homens = total_mulheres = total_nao_inf = 0
    salarios_totais = []

    while True:
        moradores = ler_inteiro("Quantas pessoas vivem nesta residência? ", minimo=0)

        if moradores == 0:
            print("\n✅ Fim da coleta de dados.\n")
            break

        total_casas += 1
        total_pessoas += moradores
        soma_idades_casa = 0
        sal_homens, sal_mulheres = [], []

        for i in range(1, moradores + 1):
            print(f"\n🧍 Pessoa {i}:")
            idade = ler_inteiro("Idade: ", minimo=0)
            soma_idades_geral += idade
            soma_idades_casa += idade

            genero = escolher_genero()
            if genero == "homem":
                total_homens += 1
            elif genero == "mulher":
                total_mulheres += 1
            else:
                total_nao_inf += 1

            salario = ler_decimal("Salário (R$): ", minimo=0)
            salarios_totais.append(salario)

            if genero == "homem":
                sal_homens.append(salario)
            elif genero == "mulher":
                sal_mulheres.append(salario)

        resumo_residencia(total_casas, moradores, soma_idades_casa, sal_homens, sal_mulheres)

    # --- Relatório final ---
    media_idade_geral = soma_idades_geral / total_pessoas if total_pessoas else 0
    media_salario_geral = sum(salarios_totais) / len(salarios_totais) if salarios_totais else 0

    print("\n" + "=" * 48)
    print("📈 RELATÓRIO FINAL DO CENSO 2025")
    print("=" * 48)
    print(f"🏘️  Total de residências: {total_casas}")
    print(f"👨‍👩‍👧‍👦 Total de pessoas: {total_pessoas}")
    print(f"📊 Média geral de idades: {media_idade_geral:.1f} anos")
    print(f"♂️ Homens: {total_homens} | ♀️ Mulheres: {total_mulheres} | ❔ Não informado: {total_nao_inf}")
    print(f"💵 Média salarial geral: R$ {media_salario_geral:.2f}")
    print("=" * 48 + "\n")


if __name__ == "__main__":
    executar_censo()
