import emojis
import random

# =============================================================
# JOGO 3 — JOGO DE APOSTAS (dado)
# Complete a função abaixo e rode o arquivo para testar!
# Quando estiver funcionando, copie a função para o arquivo
# principal e adicione ela na lista de jogos da parte 6 :)
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome           = "Caramelo"
emoji_energia  = emojis.fogo
emoji_dinheiro = emojis.diamante
# -------------------------------------------------------------------


def jogo_de_apostas(energia_atual):
    """
    Adivinhe em qual número o dado vai cair (1 a 6).
    Custo: 2 de energia | Prêmio: 4 moedas
    """
    PREMIO = 4
    CUSTO_ENERGIA = 2

    print("\n🎲 JOGO DE APOSTAS — adivinhe o dado!")
    print("Escolha um número de 1 a 6:")

    entrada = input("> ").strip()

    if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 6:
        print("Número inválido! Escolha entre 1 e 6.")
        return 0, energia_atual

    # converte a entrada para inteiro e armazena na variável "aposta"
    aposta = {COMPLETE AQUI!!}

    # o dado cai em um número aleatório entre 1 e 6
    # random.randint(a, b) sorteia um número inteiro entre a e b — complete com os valores corretos
    dado = random.randint({COMPLETE AQUI!!})

    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"\n{nome} apostou em: {aposta}")
    print(f"O dado caiu em: {dado}")
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    # verifica se acertou: se aposta for igual ao dado
    if {COMPLETE AQUI!!}:
        print(f"🏆 Acertou! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        # complete a mensagem de derrota
        print({COMPLETE AQUI!!})
        return 0, nova_energia


# =============================================================
# TESTE — rode o arquivo e tente adivinhar o dado!
# =============================================================
print("=" * 42)
print("  TESTANDO jogo_de_apostas()!")
print("  Dica: a chance de acertar é 1 em 6... boa sorte! 🎲")
print("=" * 42)

energia_teste = 10
ganhou, energia_final = jogo_de_apostas(energia_teste)

print()
print("=" * 42)
print(f"  moedas ganhas:    {ganhou}")
print(f"  energia restante: {energia_final}")
print("=" * 42)
