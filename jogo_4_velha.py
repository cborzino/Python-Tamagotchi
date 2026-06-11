import emojis
import random

# =============================================================
# JOGO 4 — JOGO DA VELHA
# Complete a função abaixo e rode o arquivo para testar!
# Quando estiver funcionando, copie a função para o arquivo
# principal e adicione ela na lista de jogos da parte 6 :)
#
# Você é X, o computador é O.
# O tabuleiro tem posições numeradas de 1 a 9:
#
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome           = "Caramelo"
emoji_energia  = emojis.fogo
emoji_dinheiro = emojis.diamante
# -------------------------------------------------------------------


def jogo_da_velha(energia_atual):
    """
    Jogo da velha contra o computador.
    Você é X, o computador é O.
    Custo: 3 de energia | Prêmio: 5 moedas
    """
    PREMIO = 5
    CUSTO_ENERGIA = 3

    tabuleiro = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def printa_tabuleiro():
        print()
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
        print("---+---+---")
        print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
        print("---+---+---")
        print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
        print()

    def checar_vencedor():
        combinacoes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]
        for a, b, c in combinacoes:
            # verifica se as três posições têm o mesmo símbolo
            # complete a condição abaixo
            if {COMPLETE AQUI!!}:
                return tabuleiro[a]
        return None

    # desconta a energia antes de começar
    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"\n⭕ ❌ JOGO DA VELHA!")
    print(f"Você é X. (gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")
    print("Digite o número da posição onde quer jogar.")

    for rodada in range(9):
        printa_tabuleiro()

        if rodada % 2 == 0:
            # vez da jogadora: lê a posição com input()
            entrada = input({COMPLETE AQUI!!}).strip()

            if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 9:
                print("Posição inválida!")
                continue

            pos = int(entrada) - 1

            if tabuleiro[pos] in ["X", "O"]:
                print("Essa posição já está ocupada!")
                continue

            # marca a posição escolhida com "X"
            tabuleiro[pos] = {COMPLETE AQUI!!}

        else:
            posicoes_livres = [i for i in range(9) if tabuleiro[i] not in ["X", "O"]]
            # complete: o computador sorteia uma posição livre aleatória
            pos = {COMPLETE AQUI!!}
            tabuleiro[pos] = "O"
            print(f"Computador jogou na posição {pos + 1}.")

        vencedor = checar_vencedor()
        if vencedor:
            printa_tabuleiro()
            # verifica se a jogadora venceu (símbolo "X")
            if {COMPLETE AQUI!!}:
                print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
                return PREMIO, nova_energia
            else:
                print(f"😢 Computador venceu! Mais sorte na próxima.")
                return 0, nova_energia

    printa_tabuleiro()
    print("🤝 Empate! Ninguém ganhou moedas dessa vez.")
    return 0, nova_energia


# =============================================================
# TESTE — rode o arquivo e jogue uma partida!
# =============================================================
print("=" * 42)
print("  TESTANDO jogo_da_velha()!")
print("  Dica: o tabuleiro tem posições de 1 a 9 ⭕❌")
print("=" * 42)

energia_teste = 10
ganhou, energia_final = jogo_da_velha(energia_teste)

print()
print("=" * 42)
print(f"  moedas ganhas:    {ganhou}")
print(f"  energia restante: {energia_final}")
print("=" * 42)
