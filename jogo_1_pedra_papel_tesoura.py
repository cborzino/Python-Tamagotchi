import emojis
import random

# =============================================================
# JOGO 1 — PEDRA, PAPEL, TESOURA
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


def pedra_papel_tesoura(energia_atual):
    """
    Jogo clássico contra o computador.
    Custo: 1 de energia | Prêmio: 2 moedas
    """
    PREMIO = 2
    CUSTO_ENERGIA = 1
    opcoes = ["pedra", "papel", "tesoura"]

    print("\n✊ 📄 ✂️  PEDRA, PAPEL, TESOURA!")
    print("Escolha: pedra, papel ou tesoura")
    # complete: use input() para ler a jogada da jogadora
    jogada = {COMPLETE AQUI!!}

    if jogada not in opcoes:
        print("Jogada inválida! Você perdeu a vez.")
        return 0, energia_atual

    # o computador escolhe aleatoriamente uma das opções
    # a função random.choice() sorteia um item de uma lista — complete com a lista "opcoes"
    computador = random.choice({COMPLETE AQUI!!})
    print(f"\n{nome} escolheu: {jogada}")
    print(f"Computador escolheu: {computador}")

    # desconta a energia independente do resultado
    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    # verifica empate: se a jogada for igual à do computador
    if {COMPLETE AQUI!!}:
        print("Empate! Ninguém ganhou moedas dessa vez.")
        return 0, nova_energia

    vence = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}

    # verifica se a jogadora venceu
    if vence[jogada] == computador:
        # complete o print com o prêmio ganho
        print(f"🏆 {nome} venceu! +{COMPLETE AQUI!!} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Computador venceu! Mais sorte na próxima.")
        # complete: a jogadora não ganhou nada, então retorna 0 e a nova energia
        return {COMPLETE AQUI!!}


# =============================================================
# TESTE — rode o arquivo e jogue algumas rodadas!
# =============================================================
print("=" * 42)
print("  TESTANDO pedra_papel_tesoura()!")
print("  Dica: tente ganhar, perder e empatar :)")
print("=" * 42)

energia_teste = 10
ganhou, energia_final = pedra_papel_tesoura(energia_teste)

print()
print("=" * 42)
print(f"  moedas ganhas:    {ganhou}")
print(f"  energia restante: {energia_final}")
print("=" * 42)
