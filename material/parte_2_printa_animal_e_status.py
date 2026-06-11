import animais
import emojis

# =============================================================
# PARTE 2 — FUNÇÕES: printa_animal e printa_status
# Complete as funções abaixo e rode o arquivo para testar!
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome           = "Caramelo"
meu_tamagotchi = animais.gato
cor            = animais.AMARELO
animal_dormindo = animais.gato_dormindo
emoji_energia  = emojis.fogo
emoji_dinheiro = emojis.diamante
# -------------------------------------------------------------------


def printa_animal():
    # essa função é responsável por imprimir seu animal no terminal
    print()

    # queremos que o nome do tamagotchi apareça antes de seu desenho
    # para isso, como vc deve completar o print abaixo?
    print({COMPLETE AQUI!!})

    print(f"{cor}{meu_tamagotchi}{animais.RESET}")


def printa_status(energia, fome, dinheiro_atual):
    # mostra todos os atributos do tamagotchi de uma vez

    # complete com as variáveis que armazenam o emoji escolhido para cada caso
    barra_energia  = "minha energia: " + {COMPLETE AQUI!!} * energia
    barra_fome     = "minha fome:    " + {COMPLETE AQUI!!} * fome
    barra_dinheiro = "meu dinheiro:  " + {COMPLETE AQUI!!} * dinheiro_atual
    print()
    print(barra_energia)
    print(barra_fome)
    print(barra_dinheiro)

    # aviso de fome: aparece se a barra estiver zerada
    # crie uma condição que, se a variável "fome" for zero,
    # imprime uma mensagem avisando para comer
    {COMPLETE AQUI COM UMA CONDICIONAL!!}
        print({COMPLETE AQUI!!})  # escreva uma mensagem de aviso de fome 

    print()


# =============================================================
# TESTE — rode o arquivo e veja se as funções funcionam!
# =============================================================
print("=" * 40)
print("  TESTANDO printa_animal():")
print("=" * 40)
printa_animal()

print("=" * 40)
print("  TESTANDO printa_status() — situação normal:")
print("  (energia=7, fome=5, dinheiro=3)")
print("=" * 40)
printa_status(7, 5, 3)

print("=" * 40)
print("  TESTANDO printa_status() — com fome zerada:")
print("  (o aviso de fome deve aparecer!)")
print("=" * 40)
printa_status(7, 0, 3)
