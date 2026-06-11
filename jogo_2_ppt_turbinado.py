import emojis
import random

# =============================================================
# JOGO 2 — PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK!
# Complete a função abaixo e rode o arquivo para testar!
# Quando estiver funcionando, copie a função para o arquivo
# principal e adicione ela na lista de jogos da parte 6 :)
#
# Regras:
#   Tesoura corta papel e decapita lagarto
#   Papel cobre pedra e derruba Spock
#   Pedra esmaga tesoura e esmaga lagarto
#   Lagarto envenena Spock e come papel
#   Spock vaporiza pedra e quebra tesoura
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome           = "Caramelo"
emoji_energia  = emojis.fogo
emoji_dinheiro = emojis.diamante
# -------------------------------------------------------------------


def pedra_papel_tesoura_turbinado(energia_atual):
    """
    Versão com 5 opções: pedra, papel, tesoura, lagarto, Spock!
    Custo: 1 de energia | Prêmio: 3 moedas
    """
    PREMIO = 3
    CUSTO_ENERGIA = 1
    opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]

    vence = {
        "tesoura": ["papel", "lagarto"],
        "papel":   ["pedra", "spock"],
        "pedra":   ["tesoura", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock":   ["pedra", "tesoura"],
    }

    print("\n✊ 📄 ✂️ 🦎 🖖 PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK!")
    print("Escolha: pedra, papel, tesoura, lagarto ou spock")
    # complete: use input() para ler a jogada (igual ao jogo anterior!)
    jogada = {COMPLETE AQUI!!}

    if jogada not in opcoes:
        print("Jogada inválida! Você perdeu a vez.")
        return 0, energia_atual

    # complete: o computador sorteia uma opção aleatória (igual ao jogo anterior!)
    computador = {COMPLETE AQUI!!}
    print(f"\n{nome} escolheu: {jogada}")
    print(f"Computador escolheu: {computador}")

    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    # verifica empate
    if jogada == computador:
        print("Empate! Ninguém ganhou moedas dessa vez.")
        return 0, nova_energia

    # verifica vitória: checa se o computador está na lista de quem a jogada vence
    if {COMPLETE AQUI!!}:
        print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Computador venceu! Mais sorte na próxima.")
        return 0, nova_energia


# =============================================================
# TESTE — rode o arquivo e jogue algumas rodadas!
# =============================================================
print("=" * 42)
print("  TESTANDO pedra_papel_tesoura_turbinado()!")
print("  Dica: experimente todas as 5 opções :)")
print("=" * 42)

energia_teste = 10
ganhou, energia_final = pedra_papel_tesoura_turbinado(energia_teste)

print()
print("=" * 42)
print(f"  moedas ganhas:    {ganhou}")
print(f"  energia restante: {energia_final}")
print("=" * 42)
