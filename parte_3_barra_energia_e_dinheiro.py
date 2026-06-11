import animais
import emojis

# =============================================================
# PARTE 3 — FUNÇÕES: barra_de_energia e dinheiro
# Complete as funções abaixo e rode o arquivo para testar!
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome           = "Caramelo"
emoji_energia  = emojis.fogo
emoji_dinheiro = emojis.diamante
# -------------------------------------------------------------------


def barra_de_energia(energia_atual, energia_ganha):
    energia_maxima = 10

    # soma a energia ganha à energia atual
    # some as variáveis que armazenam essas energias que são passadas como argumentos da função
    nova_energia = {COMPLETE AQUI!!}

    # verifica se ultrapassou o limite máximo
    # queremos uma CONDICIONAL que, se a nova energia ficar maior que a máxima, força a nova energia
    # a parar no valor máximo
    {COMPLETE AQUI COM UMA CONDICIONAL!!}
        nova_energia = energia_maxima  # faz a nova energia parar no máximo
        print(f"{emoji_energia} {nome} já está com energia máxima!")

    # monta e printa a barra de energia com emojis
    barra = "minha energia: "

    # vamos fazer um LOOP que se repita o número de vezes correspondente a nossa energia atual
    # esse loop cria a barra de energia com emojis adicionando um emoji para cada unidade de energia que temos
    # vc lembra como criar loops for e while?
    {COMPLETE AQUI COM UM LOOP!!}
        barra += emoji_energia

    print(barra)
    return nova_energia  # devolve o novo valor para ser usado depois


def dinheiro(dinheiro_atual, dinheiro_ganho):
    dinheiro_maximo = 10

    # soma o dinheiro ganho ao dinheiro atual
    # muito semelhante à soma feita na função de barra de energia!!
    novo_dinheiro = {COMPLETE AQUI!!}

    # verifica se ultrapassou o limite máximo
    # a CONDICIONAL força o novo dinheiro a parar no dinheiro máximo
    {COMPLETE AQUI COM UMA CONDICIONAL!!}
        {COMPLETE AQUI!!}  # semelhante ao feito na barra de energia
        print(f"{emoji_dinheiro} {nome} já tem dinheiro máximo!")

    # monta e printa a barra de dinheiro com emojis
    barra = "meu dinheiro:  "

    # mais um LOOP, dessa vez que se repete tantas vezes quanto a quantidade de novo_dinheiro
    {COMPLETE AQUI COM UM LOOP!!}
        barra += {COMPLETE AQUI!!}  # qual a variável que armazena seu emoji escolhido para dinheiro?

    print(barra)
    return novo_dinheiro  # devolve o novo valor para ser usado depois


# =============================================================
# TESTE — rode o arquivo e veja se as funções funcionam!
# =============================================================
print("=" * 40)
print("  TESTANDO barra_de_energia():")
print("=" * 40)

print("  caso 1 — ganhando 3 de energia a partir de 4:")
print("  (resultado esperado: barra com 7 emojis)")
resultado = barra_de_energia(4, 3)
print(f"  nova energia retornada: {resultado}")
print()

print("  caso 2 — tentando passar do máximo (energia=8, ganha=5):")
print("  (resultado esperado: barra com 10 emojis + aviso de máximo)")
resultado = barra_de_energia(8, 5)
print(f"  nova energia retornada: {resultado}")

print()
print("=" * 40)
print("  TESTANDO dinheiro():")
print("=" * 40)

print("  caso 1 — ganhando 2 moedas a partir de 3:")
print("  (resultado esperado: barra com 5 emojis)")
resultado = dinheiro(3, 2)
print(f"  novo dinheiro retornado: {resultado}")
print()

print("  caso 2 — tentando passar do máximo (dinheiro=9, ganha=4):")
print("  (resultado esperado: barra com 10 emojis + aviso de máximo)")
resultado = dinheiro(9, 4)
print(f"  novo dinheiro retornado: {resultado}")
