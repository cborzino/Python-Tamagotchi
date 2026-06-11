import animais
import emojis
import random

# =============================================================
# PARTE 6 — MENUS: menu_de_jogos e menu_principal
# Essa é a última parte — aqui você junta tudo!
# Complete as lacunas e rode o arquivo para testar o jogo inteiro.
# =============================================================

# -------------------------------------------------------------------
# CABEÇALHO — variáveis de exemplo para o teste funcionar
# (quando colar no arquivo principal, use as suas variáveis!)
# -------------------------------------------------------------------
nome            = "Caramelo"
meu_tamagotchi  = animais.gato
cor             = animais.AMARELO
animal_dormindo = animais.gato_dormindo
emoji_energia   = emojis.fogo
emoji_dinheiro  = emojis.diamante
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# FUNÇÕES AUXILIARES — cole aqui as suas versões completas das
# partes anteriores antes de testar!
# Por enquanto estão com implementações de exemplo para o arquivo rodar.
# -------------------------------------------------------------------

def printa_animal():
    print()
    print(nome)
    print(f"{cor}{meu_tamagotchi}{animais.RESET}")

def printa_status(energia, fome, dinheiro_atual):
    barra_energia  = "minha energia: " + emoji_energia * energia
    barra_fome     = "minha fome:    " + emojis.cupcake * fome
    barra_dinheiro = "meu dinheiro:  " + emoji_dinheiro * dinheiro_atual
    print()
    print(barra_energia)
    print(barra_fome)
    print(barra_dinheiro)
    if fome == 0:
        print(f"⚠️  {nome} está com fome! Vá comer algo.")
    print()

def barra_de_energia(energia_atual, energia_ganha):
    energia_maxima = 10
    nova_energia = energia_atual + energia_ganha
    if nova_energia > energia_maxima:
        nova_energia = energia_maxima
        print(f"{emoji_energia} {nome} já está com energia máxima!")
    barra = "minha energia: "
    for i in range(nova_energia):
        barra += emoji_energia
    print(barra)
    return nova_energia

def dinheiro(dinheiro_atual, dinheiro_ganho):
    dinheiro_maximo = 10
    novo_dinheiro = dinheiro_atual + dinheiro_ganho
    if novo_dinheiro > dinheiro_maximo:
        novo_dinheiro = dinheiro_maximo
        print(f"{emoji_dinheiro} {nome} já tem dinheiro máximo!")
    barra = "meu dinheiro:  "
    for i in range(novo_dinheiro):
        barra += emoji_dinheiro
    print(barra)
    return novo_dinheiro

def dormir(energia_atual):
    energia_maxima = 10
    vai_dormir = input(f"\n{nome} vai dormir? (sim/não) ")
    if vai_dormir == "sim":
        horas = int(input(f"Quantas horas {nome} vai dormir? "))
        print(f"\n{cor}{animal_dormindo}{animais.RESET}")
        print(f"{emojis.zzz} {nome} dormiu {horas} hora(s)!\n")
        nova_energia = energia_atual + horas
        if nova_energia >= energia_maxima:
            nova_energia = energia_maxima
            print(f"{emoji_energia} {nome} acordou com energia máxima!")
        barra = "minha energia: "
        for i in range(nova_energia):
            barra += emoji_energia
        print(barra)
    else:
        print(f"\n{nome} não foi dormir.")
        nova_energia = energia_atual
    return nova_energia

def comer(fome_atual, dinheiro_atual):
    fome_maxima = 10
    cardapio = {
        "1": {"nome": "biscoito",  "emoji": emojis.cupcake,   "preco": 1, "fome": 2},
        "2": {"nome": "chocolate", "emoji": emojis.chocolate, "preco": 2, "fome": 4},
        "3": {"nome": "bolo",      "emoji": emojis.cupcake,   "preco": 3, "fome": 6},
    }
    print("\n" + "=" * 40)
    print(f"  {emojis.cupcake} O QUE {nome} VAI COMER?")
    print("=" * 40)
    for numero, item in cardapio.items():
        print(f"  {numero}. {item['emoji']} {item['nome']:<12} custa {item['preco']} {emoji_dinheiro}  +{item['fome']} de fome")
    print(f"  0. Voltar")
    print("=" * 40)
    print(f"  dinheiro atual: {dinheiro_atual} {emoji_dinheiro}")
    escolha = input("O que vai comer? ").strip()
    if escolha == "0":
        print(f"Tudo bem, {nome} não comeu nada.")
        return fome_atual, dinheiro_atual
    if escolha not in cardapio:
        print("Opção inválida!")
        return fome_atual, dinheiro_atual
    item_escolhido = cardapio[escolha]
    if dinheiro_atual < item_escolhido["preco"]:
        print(f"\n{emoji_dinheiro} {nome} não tem dinheiro suficiente!")
        return fome_atual, dinheiro_atual
    novo_dinheiro = dinheiro_atual - item_escolhido["preco"]
    nova_fome = fome_atual + item_escolhido["fome"]
    if nova_fome >= fome_maxima:
        nova_fome = fome_maxima
        print(f"{emojis.cupcake} {nome} está satisfeito!")
    barra_fome     = "minha fome:   "
    barra_dinheiro = "meu dinheiro: "
    for i in range(nova_fome):
        barra_fome += emojis.cupcake
    for i in range(novo_dinheiro):
        barra_dinheiro += emoji_dinheiro
    print(barra_fome)
    print(barra_dinheiro)
    return nova_fome, novo_dinheiro

# -------------------------------------------------------------------
# JOGOS — cole aqui as funções dos jogos que você implementou!
# Cada jogo que você colar aqui vai aparecer automaticamente
# no menu de jogos. Veja as instruções abaixo :)
# -------------------------------------------------------------------

# (exemplo já preenchido para o arquivo rodar — substitua pela sua versão!)
def pedra_papel_tesoura(energia_atual):
    PREMIO = 2
    CUSTO_ENERGIA = 1
    opcoes = ["pedra", "papel", "tesoura"]
    print("\n✊ 📄 ✂️  PEDRA, PAPEL, TESOURA!")
    print("Escolha: pedra, papel ou tesoura")
    jogada = input("> ").strip().lower()
    if jogada not in opcoes:
        print("Jogada inválida!")
        return 0, energia_atual
    computador = random.choice(opcoes)
    print(f"\n{nome} escolheu: {jogada}\nComputador escolheu: {computador}")
    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")
    if jogada == computador:
        print("Empate!")
        return 0, nova_energia
    vence = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}
    if vence[jogada] == computador:
        print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Computador venceu!")
        return 0, nova_energia

# -------------------------------------------------------------------
# FIM DAS FUNÇÕES AUXILIARES
# -------------------------------------------------------------------


# =============================================================
# LISTA DE JOGOS DISPONÍVEIS
# =============================================================
#
# Cada jogo que você implementar deve ser adicionado nessa lista!
# O formato de cada item é:
#
#   {"nome": "Nome do jogo", "funcao": nome_da_funcao, "custo": X, "premio": Y}
#
# Onde:
#   "nome"   — o nome que vai aparecer no menu
#   "funcao" — o nome da função do jogo (sem parênteses!)
#   "custo"  — quantos pontos de energia o jogo consome
#   "premio" — quantas moedas a jogadora ganha se vencer
#
# Exemplo com dois jogos cadastrados:
#
#   jogos_disponiveis = [
#       {"nome": "Pedra, Papel, Tesoura",        "funcao": pedra_papel_tesoura,        "custo": 1, "premio": 2},
#       {"nome": "PPT Turbinado (Lagarto+Spock)", "funcao": pedra_papel_tesoura_turbinado, "custo": 1, "premio": 3},
#   ]
#
# Quando terminar um jogo novo, cole a função aqui em cima e
# adicione uma linha nova na lista abaixo!
# =============================================================

jogos_disponiveis = [
    {"nome": "Pedra, Papel, Tesoura", "funcao": pedra_papel_tesoura, "custo": 1, "premio": 2},
    # {"nome": "PPT Turbinado (Lagarto+Spock)", "funcao": pedra_papel_tesoura_turbinado, "custo": 1, "premio": 3},
    # {"nome": "Jogo de Apostas — dado",        "funcao": jogo_de_apostas,               "custo": 2, "premio": 4},
    # {"nome": "Jogo da Velha",                 "funcao": jogo_da_velha,                 "custo": 3, "premio": 5},
]
# Dica: para ativar um jogo, apague o # do início da linha dele!


def menu_de_jogos(energia_atual, fome_atual, dinheiro_atual):
    """
    Mostra o menu de jogos.
    Retorna (novo dinheiro, nova energia, nova fome) após o jogo.
    """
    print("\n" + "=" * 42)
    # complete o print com o nome do tamagotchi
    print(f"  🎮 HORA DE JOGAR, {COMPLETE AQUI!!}!")
    print("=" * 42)
    print(f"  energia atual: {energia_atual} {emoji_energia}")
    print()

    # mostra no menu apenas os jogos que estão na lista jogos_disponiveis
    # o enumerate() numera os itens automaticamente a partir de 1
    for numero, jogo in enumerate(jogos_disponiveis, start=1):
        print(f"  {numero}. {jogo['nome']:<32}"
              f"-{jogo['custo']}{emoji_energia}  +{jogo['premio']}{emoji_dinheiro}")

    print(f"  0. Voltar")
    print("=" * 42)

    escolha = input("Escolha um jogo: ").strip()

    if escolha == "0":
        print("Voltando ao menu principal...")
        return dinheiro_atual, energia_atual, fome_atual

    # verifica se a escolha é um número válido dentro da lista
    # complete a condição: se "escolha" não for um dígito OU
    # se o número digitado for menor que 1 OU maior que o total de jogos disponíveis
    if {COMPLETE AQUI COM UMA CONDIÇÃO!!}:
        print("Opção inválida!")
        return dinheiro_atual, energia_atual, fome_atual

    # converte a escolha para o índice correto da lista (lembre: listas começam em 0!)
    jogo_escolhido = jogos_disponiveis[int(escolha) - 1]

    # verifica se a energia atual é menor que o custo do jogo escolhido
    if {COMPLETE AQUI!!}:
        print(f"\n{emoji_energia} {nome} não tem energia suficiente para jogar! "
              f"Tente comer ou dormir primeiro.")
        return dinheiro_atual, energia_atual, fome_atual

    # chama a função do jogo escolhido
    # jogo_escolhido["funcao"] guarda a função — os () a executam passando a energia atual
    ganhou, nova_energia = jogo_escolhido["funcao"](energia_atual)

    # se perdeu (ganhou == 0), desconta 1 de fome
    nova_fome = fome_atual
    # complete a condição: se "ganhou" for igual a 0...
    if {COMPLETE AQUI!!}:
        nova_fome = max(0, fome_atual - 1)
        print(f"\n{emojis.cupcake} {nome} ficou com fome depois de perder... "
              f"({nova_fome} de fome restante)")

    novo_dinheiro = dinheiro(dinheiro_atual, ganhou)
    return novo_dinheiro, nova_energia, nova_fome


def menu_principal():
    """
    Menu principal do jogo — loop que mantém o jogo rodando.
    """
    # estado inicial do tamagotchi — sinta-se livre para mudar os valores!
    energia_atual  = 5
    fome_atual     = 5
    dinheiro_atual = 3

    printa_animal()
    # complete o print de boas-vindas com o nome do tamagotchi e um emoji
    print(f"\nOlá! Eu sou {COMPLETE AQUI!!}! {COMPLETE AQUI!!}")
    printa_status(energia_atual, fome_atual, dinheiro_atual)

    # loop principal — o jogo continua até a jogadora escolher sair
    while True:
        print("\n" + "=" * 40)
        # complete o print com o nome do tamagotchi
        print(f"  O que {COMPLETE AQUI!!} vai fazer?")
        print("=" * 40)

        if fome_atual == 0:
            # complete a mensagem de aviso de fome no menu
            print(f"  ⚠️  {COMPLETE AQUI!!}")

        print(f"  1. {emoji_energia}  Jogar")
        print(f"  2. {emojis.cupcake}  Comer")
        print(f"  3. {emojis.zzz}  Dormir")
        print(f"  4. Ver status")
        print(f"  0. Sair")
        print("=" * 40)

        escolha = input("> ").strip()

        if escolha == "1":
            dinheiro_atual, energia_atual, fome_atual = menu_de_jogos(energia_atual, fome_atual, dinheiro_atual)

        elif escolha == "2":
            fome_atual, dinheiro_atual = comer(fome_atual, dinheiro_atual)

        elif escolha == "3":
            energia_atual = dormir(energia_atual)

        elif escolha == "4":
            printa_animal()
            printa_status(energia_atual, fome_atual, dinheiro_atual)

        elif escolha == "0":
            # complete a mensagem de despedida com o nome do tamagotchi e um emoji
            print({COMPLETE AQUI!!})
            break  # encerra o loop e o jogo

        else:
            print("Opção inválida! Escolha entre 0 e 4.")


# =============================================================
# INÍCIO DO JOGO — rode o arquivo para jogar!
# =============================================================
menu_principal()
