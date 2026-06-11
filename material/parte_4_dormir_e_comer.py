import animais
import emojis

# =============================================================
# PARTE 4 — FUNÇÕES: dormir e comer
# Complete as funções abaixo e rode o arquivo para testar!
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome            = "Caramelo"
cor             = animais.AMARELO
animal_dormindo = animais.gato_dormindo
emoji_energia   = emojis.fogo
emoji_dinheiro  = emojis.diamante
emoji_fome      = emojis.cupcake
# -------------------------------------------------------------------


def dormir(energia_atual):
    energia_maxima = 10

    # pergunta para a jogadora se o tamagotchi vai dormir
    # a função input() exibe uma mensagem e espera a jogadora digitar algo
    # complete a mensagem entre aspas com uma pergunta para o tamagotchi
    vai_dormir = input({COMPLETE AQUI!!})

    # verifica se a resposta foi "sim"
    if vai_dormir == "sim":

        # pergunta quantas horas vai dormir — cada hora = 1 de energia
        # complete a mensagem do input abaixo
        horas = int(input({COMPLETE AQUI!!}))

        # printa o bichinho dormindo
        print(f"\n{cor}{animal_dormindo}{animais.RESET}")
        # complete o print abaixo com a variável que armazena o tempo de sono
        print(f"{emojis.zzz} {nome} dormiu {COMPLETE AQUI!!} hora(s)!\n")

        # calcula nova energia: energia atual + horas dormidas
        # complete a soma abaixo
        nova_energia = {COMPLETE AQUI!!}

        # verifica se ultrapassou o limite máximo
        if nova_energia >= energia_maxima:
            nova_energia = energia_maxima
            print(f"{emoji_energia} {nome} acordou com energia máxima!")

        # monta e printa a barra de energia atualizada
        barra = "minha energia: "
        # complete o range() com a variável correta para criar a barra
        for i in range({COMPLETE AQUI!!}):
            barra += emoji_energia
        print(barra)

    else:
        # complete a mensagem dizendo que o tamagotchi não foi dormir
        print({COMPLETE AQUI!!})
        nova_energia = energia_atual  # energia não muda

    # devolve a energia depois de dormir — não mexa nessa linha!
    return nova_energia


def comer(fome_atual, dinheiro_atual):
    fome_maxima  = 10
    dinheiro_minimo = 0

    # cardápio: cada comida tem seu preço e quanto recupera de fome
    cardapio = {
        "1": {"nome": "biscoito",   "emoji": emojis.cupcake,   "preco": 1, "fome": 2},
        "2": {"nome": "chocolate",  "emoji": emojis.chocolate, "preco": 2, "fome": 4},
        "3": {"nome": "bolo",       "emoji": emojis.pizza,   "preco": 3, "fome": 6},
    }

    print("\n" + "=" * 40)
    # complete o print abaixo com um emoji de comida e o nome do tamagotchi 
    print(f"  {COMPLETE AQUI!!} O QUE {COMPLETE AQUI!!} VAI COMER?")
    print("=" * 40)

    # printa o cardápio com preço e quanto recupera
    for numero, item in cardapio.items():
        print(f"  {numero}. {item['emoji']} {item['nome']:<12} "
              f"custa {item['preco']} {emoji_dinheiro}  "
              f"+{item['fome']} de fome")

    print(f"  0. Voltar")
    print("=" * 40)
    print(f"  dinheiro atual: {dinheiro_atual} {emoji_dinheiro}")

    escolha = input("O que vai comer? ").strip()

    # opção de voltar sem comer
    if escolha == "0":
        # complete a mensagem dizendo que o tamagotchi não comeu nada
        print({COMPLETE AQUI!!})
        return fome_atual, dinheiro_atual

    # verifica se a escolha existe no cardápio
    if escolha not in cardapio:
        print("Opção inválida!")
        return fome_atual, dinheiro_atual

    item_escolhido = cardapio[escolha]

    # verifica se tem dinheiro suficiente para comprar
    # complete a condição: se dinheiro_atual for MENOR QUE o preço do item escolhido...
    # note que para acessar o valor de uma característica de um item do dicionario usamos
    # item_escolido["caracteristica"]

    if {COMPLETE AQUI!!}:
        print(f"\n{emoji_dinheiro} {nome} não tem dinheiro suficiente para comprar {item_escolhido['nome']}!")
        return fome_atual, dinheiro_atual

    # desconta o preço do dinheiro: dinheiro atual MENOS o preço do item
    novo_dinheiro = {COMPLETE AQUI!!}
    print(f"\n{item_escolhido['emoji']} {nome} comeu {item_escolhido['nome']}! "
          f"-{item_escolhido['preco']} {emoji_dinheiro}")

    # soma a fome recuperada: fome atual MAIS a fome que o item recupera
    nova_fome = {COMPLETE AQUI!!}

    # verifica se ultrapassou o limite máximo de fome
    if nova_fome >= fome_maxima:
        nova_fome = fome_maxima
        # complete a mensagem dizendo que o tamagotchi está satisfeito
        print({COMPLETE AQUI!!})

    # monta e printa as barras atualizadas
    barra_fome     = "minha fome:   "
    barra_dinheiro = "meu dinheiro: "
    # complete os ranges abaixo com as variáveis corretas
    for i in range({COMPLETE AQUI!!}):
        barra_fome += emoji_fome
    for i in range({COMPLETE AQUI!!}):
        barra_dinheiro += emoji_dinheiro

    print(barra_fome)
    print(barra_dinheiro)

    return nova_fome, novo_dinheiro  # devolve os dois valores atualizados


# =============================================================
# TESTE — rode o arquivo e interaja com seu tamagotchi!
# =============================================================
print("=" * 40)
print("  TESTANDO dormir():")
print("  (tente responder 'sim' e depois 'não')")
print("=" * 40)
energia_inicial = 4
print(f"  energia antes de dormir: {energia_inicial}")
energia_depois = dormir(energia_inicial)
print(f"  energia depois de dormir: {energia_depois}")

print()
print("=" * 40)
print("  TESTANDO comer():")
print("  (tente comprar algo e também tentar comprar")
print("   sem dinheiro suficiente!)")
print("=" * 40)
fome_inicial    = 3
dinheiro_inicial = 2
print(f"  fome antes: {fome_inicial} | dinheiro antes: {dinheiro_inicial}")
fome_depois, dinheiro_depois = comer(fome_inicial, dinheiro_inicial)
print(f"  fome depois: {fome_depois} | dinheiro depois: {dinheiro_depois}")
