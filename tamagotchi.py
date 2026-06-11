import animais
import emojis
import random

# crie uma variável para armazenar o nome do seu tamagotchi
nome = "AZUL"

# acesse o arquivo "animais.py" para ver como são as opções de animais ;)
meu_tamagotchi = animais.dino

# também no arquivo "animais.py", veja as cores em que seu animal pode ser desenhado no terminal
cor = animais.AZUL

# versão dormindo do seu tamagotchi (deve combinar com o animal escolhido acima!)
animal_dormindo = animais.dino_dormindo

# escolha o emoji que representa a ENERGIA do seu tamagotchi
# sugestões: emojis.fogo, emojis.raio, emojis.coracao_rosa, emojis.coracao_amarelo, emojis.flor
emoji_energia = emojis.raio

# escolha o emoji que representa o DINHEIRO do seu tamagotchi
# sugestões: emojis.diamante, emojis.moeda, emojis.saca_dinheiro, emojis.flor, emojis.chocolate
emoji_dinheiro = emojis.coracao_amarelo


# ---------------------------------------------------------------------
# funções do tamagotchi
# ---------------------------------------------------------------------

def printa_animal():
    # essa função é responsável por imprimir seu animal no terminal
    print()
    print(nome)
    #queremos que o nome do tamagotchi apareça antes de seu desenho 
    #para isso, como vc deve completar o print abaixo?
    #print(f"{animais.NEGRITO}  ~{#completar aqui!}~)
    print(f"{cor}{meu_tamagotchi}{animais.RESET}")


def printa_status(energia, fome, dinheiro_atual):
    # mostra todos os atributos do tamagotchi de uma vez
    barra_energia  = "minha energia: " + emoji_energia * energia
    barra_fome     = "minha fome:    " + emojis.cupcake * fome
    barra_dinheiro = "meu dinheiro:  " + emoji_dinheiro * dinheiro_atual
    print()
    print(barra_energia)
    print(barra_fome)
    print(barra_dinheiro)

    # aviso de fome: aparece se a barra estiver zerada
    if fome == 0:
        print(f"\n⚠️  {nome} está com MUITA FOME! Vá comer antes de continuar!")

    print()


def barra_de_energia(energia_atual, energia_ganha):
    energia_maxima = 10

    # soma a energia ganha à energia atual
    nova_energia = energia_atual + energia_ganha

    # verifica se ultrapassou o limite máximo
    if nova_energia >= energia_maxima:
        nova_energia = energia_maxima
        print(f"{emoji_energia} {nome} já está com energia máxima!")

    # monta e printa a barra de energia com emojis
    barra = "minha energia: "
    for i in range(nova_energia):
        barra += emoji_energia

    print(barra)
    return nova_energia  # devolve o novo valor para ser usado depois


def dinheiro(dinheiro_atual, dinheiro_ganho):
    dinheiro_maximo = 10

    # soma o dinheiro ganho ao dinheiro atual
    novo_dinheiro = dinheiro_atual + dinheiro_ganho

    # verifica se ultrapassou o limite máximo
    if novo_dinheiro >= dinheiro_maximo:
        novo_dinheiro = dinheiro_maximo
        print(f"{emoji_dinheiro} {nome} já tem dinheiro máximo!")

    # monta e printa a barra de dinheiro com emojis
    barra = "meu dinheiro:  "
    for i in range(novo_dinheiro):
        barra += emoji_dinheiro

    print(barra)
    return novo_dinheiro  # devolve o novo valor para ser usado depois


def dormir(energia_atual):
    energia_maxima = 10

    vai_dormir = input(f"\n{nome} vai dormir? (sim/não) ")

    if vai_dormir == "sim":

        # pergunta quantas horas vai dormir — cada hora = 1 de energia
        horas = int(input(f"Quantas horas {nome} vai dormir? "))

        # printa o bichinho dormindo
        print(f"\n{cor}{animal_dormindo}{animais.RESET}")
        print(f"{emojis.zzz} {nome} dormiu {horas} hora(s)!\n")

        # calcula nova energia
        nova_energia = energia_atual + horas

        # verifica se ultrapassou o limite máximo
        if nova_energia >= energia_maxima:
            nova_energia = energia_maxima
            print(f"{emoji_energia} {nome} acordou com energia máxima!")

        # monta e printa a barra de energia atualizada
        barra = "minha energia: "
        for i in range(nova_energia):
            barra += emoji_energia
        print(barra)

    else:
        print(f"\n{nome} não foi dormir.")
        nova_energia = energia_atual  # energia não muda

    return nova_energia  # devolve a energia depois de dormir


def comer(fome_atual, dinheiro_atual):
    fome_maxima  = 10
    dinheiro_minimo = 0

    # cardápio: cada comida tem seu preço e quanto recupera de fome
    cardapio = {
        "1": {"nome": "biscoito",   "emoji": emojis.cupcake,   "preco": 1, "fome": 2},
        "2": {"nome": "chocolate",  "emoji": emojis.chocolate, "preco": 2, "fome": 4},
        "3": {"nome": "bolo",       "emoji": emojis.cupcake,   "preco": 3, "fome": 6},
    }

    print("\n" + "=" * 40)
    print(f"  {emojis.cupcake} O QUE {nome} VAI COMER?")
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
        print("Tudo bem, {nome} não comeu nada.")
        return fome_atual, dinheiro_atual

    # verifica se a escolha existe no cardápio
    if escolha not in cardapio:
        print("Opção inválida!")
        return fome_atual, dinheiro_atual

    item_escolhido = cardapio[escolha]

    # verifica se tem dinheiro suficiente para comprar
    if dinheiro_atual < item_escolhido["preco"]:
        print(f"\n{emoji_dinheiro} {nome} não tem dinheiro suficiente para comprar {item_escolhido['nome']}!")
        return fome_atual, dinheiro_atual

    # desconta o preço do dinheiro
    novo_dinheiro = dinheiro_atual - item_escolhido["preco"]
    print(f"\n{item_escolhido['emoji']} {nome} comeu {item_escolhido['nome']}! "
          f"-{item_escolhido['preco']} {emoji_dinheiro}")

    # soma a fome recuperada
    nova_fome = fome_atual + item_escolhido["fome"]

    # verifica se ultrapassou o limite máximo de fome
    if nova_fome >= fome_maxima:
        nova_fome = fome_maxima
        print(f"{emojis.cupcake} {nome} está satisfeito!")

    # printa as barras atualizadas
    barra_fome    = "minha fome:   "
    barra_dinheiro = "meu dinheiro: "
    for i in range(nova_fome):
        barra_fome += emojis.cupcake
    for i in range(novo_dinheiro):
        barra_dinheiro += emoji_dinheiro

    print(barra_fome)
    print(barra_dinheiro)

    return nova_fome, novo_dinheiro  # devolve os dois valores atualizados


# ---------------------------------------------------------------------
# jogos — cada um recebe a energia atual e retorna (dinheiro ganho, energia gasta)
# ---------------------------------------------------------------------

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
    jogada = input("> ").strip().lower()

    if jogada not in opcoes:
        print("Jogada inválida! Você perdeu a vez.")
        return 0, energia_atual

    computador = random.choice(opcoes)
    print(f"\n{nome} escolheu: {jogada}")
    print(f"Computador escolheu: {computador}")

    # desconta a energia independente do resultado
    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    if jogada == computador:
        print("Empate! Ninguém ganhou moedas dessa vez.")
        return 0, nova_energia

    vence = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"}

    if vence[jogada] == computador:
        print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Computador venceu! Mais sorte na próxima.")
        return 0, nova_energia


def pedra_papel_tesoura_turbinado(energia_atual):
    """
    Versão com 5 opções: pedra, papel, tesoura, lagarto, Spock!
    Custo: 1 de energia | Prêmio: 3 moedas

    Regras:
    - Tesoura corta papel, decapita lagarto
    - Papel cobre pedra, derruba Spock
    - Pedra esmaga tesoura, esmaga lagarto
    - Lagarto envenena Spock, come papel
    - Spock vaporiza pedra, quebra tesoura
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
    jogada = input("> ").strip().lower()

    if jogada not in opcoes:
        print("Jogada inválida! Você perdeu a vez.")
        return 0, energia_atual

    computador = random.choice(opcoes)
    print(f"\n{nome} escolheu: {jogada}")
    print(f"Computador escolheu: {computador}")

    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    if jogada == computador:
        print("Empate! Ninguém ganhou moedas dessa vez.")
        return 0, nova_energia

    if computador in vence[jogada]:
        print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Computador venceu! Mais sorte na próxima.")
        return 0, nova_energia


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

    aposta = int(entrada)
    dado = random.randint(1, 6)

    nova_energia = max(0, energia_atual - CUSTO_ENERGIA)
    print(f"\n{nome} apostou em: {aposta}")
    print(f"O dado caiu em: {dado}")
    print(f"(gastou {CUSTO_ENERGIA} {emoji_energia} de energia)")

    if aposta == dado:
        print(f"🏆 Acertou! +{PREMIO} {emoji_dinheiro}")
        return PREMIO, nova_energia
    else:
        print(f"😢 Não foi dessa vez! Mais sorte na próxima.")
        return 0, nova_energia


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
            if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
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
            entrada = input("Sua jogada (1-9): ").strip()

            if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 9:
                print("Posição inválida!")
                continue

            pos = int(entrada) - 1

            if tabuleiro[pos] in ["X", "O"]:
                print("Essa posição já está ocupada!")
                continue

            tabuleiro[pos] = "X"

        else:
            posicoes_livres = [i for i in range(9) if tabuleiro[i] not in ["X", "O"]]
            pos = random.choice(posicoes_livres)
            tabuleiro[pos] = "O"
            print(f"Computador jogou na posição {pos + 1}.")

        vencedor = checar_vencedor()
        if vencedor:
            printa_tabuleiro()
            if vencedor == "X":
                print(f"🏆 {nome} venceu! +{PREMIO} {emoji_dinheiro}")
                return PREMIO, nova_energia
            else:
                print(f"😢 Computador venceu! Mais sorte na próxima.")
                return 0, nova_energia

    printa_tabuleiro()
    print("🤝 Empate! Ninguém ganhou moedas dessa vez.")
    return 0, nova_energia


# ---------------------------------------------------------------------
# menus
# ---------------------------------------------------------------------

def menu_de_jogos(energia_atual, fome_atual, dinheiro_atual):
    """
    Mostra o menu de jogos.
    Retorna (novo dinheiro, nova energia, nova fome) após o jogo.
    """
    print("\n" + "=" * 42)
    print(f"  🎮 HORA DE JOGAR, {nome}!")
    print("=" * 42)
    print(f"  energia atual: {energia_atual} {emoji_energia}")
    print()
    print(f"  1. Pedra, Papel, Tesoura         "
          f"-1{emoji_energia}  +2{emoji_dinheiro}")
    print(f"  2. PPT Turbinado (Lagarto+Spock)  "
          f"-1{emoji_energia}  +3{emoji_dinheiro}")
    print(f"  3. Jogo de Apostas — dado         "
          f"-2{emoji_energia}  +4{emoji_dinheiro}")
    print(f"  4. Jogo da Velha                  "
          f"-3{emoji_energia}  +5{emoji_dinheiro}")
    print(f"  0. Voltar")
    print("=" * 42)

    escolha = input("Escolha um jogo: ").strip()

    if escolha == "0":
        print("Voltando ao menu principal...")
        return dinheiro_atual, energia_atual, fome_atual

    # verifica se tem energia suficiente antes de jogar
    custos = {"1": 1, "2": 1, "3": 2, "4": 3}

    if escolha not in custos:
        print("Opção inválida!")
        return dinheiro_atual, energia_atual, fome_atual

    if energia_atual < custos[escolha]:
        print(f"\n{emoji_energia} {nome} não tem energia suficiente para jogar! "
              f"Tente comer ou dormir primeiro.")
        return dinheiro_atual, energia_atual, fome_atual

    if escolha == "1":
        ganhou, nova_energia = pedra_papel_tesoura(energia_atual)
    elif escolha == "2":
        ganhou, nova_energia = pedra_papel_tesoura_turbinado(energia_atual)
    elif escolha == "3":
        ganhou, nova_energia = jogo_de_apostas(energia_atual)
    elif escolha == "4":
        ganhou, nova_energia = jogo_da_velha(energia_atual)

    # se perdeu (ganhou == 0), desconta 1 de fome
    nova_fome = fome_atual
    if ganhou == 0:
        nova_fome = max(0, fome_atual - 1)  # fome não vai abaixo de 0
        print(f"\n{emojis.cupcake} {nome} ficou com fome depois de perder... "
              f"({nova_fome} de fome restante)")

    novo_dinheiro = dinheiro(dinheiro_atual, ganhou)
    return novo_dinheiro, nova_energia, nova_fome


def menu_principal():
    """
    Menu principal do jogo — loop que mantém o jogo rodando.
    """
    # estado inicial do tamagotchi
    energia_atual  = 5
    fome_atual     = 5
    dinheiro_atual = 3

    printa_animal()
    print(f"\nOlá! Eu sou {nome}! {emojis.coracao_rosa}")
    printa_status(energia_atual, fome_atual, dinheiro_atual)

    # loop principal — o jogo continua até a jogadora escolher sair
    while True:
        print("\n" + "=" * 40)
        print(f"  O que {nome} vai fazer?")
        print("=" * 40)

        # aviso de fome aparece no cabeçalho do menu quando a barra está zerada
        if fome_atual == 0:
            print(f"  ⚠️  {nome} está com MUITA FOME!")

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
            print(f"\nAté logo, {nome}! {emojis.coracao_rosa}\n")
            break  # encerra o loop e o jogo

        else:
            print("Opção inválida! Escolha entre 0 e 4.")


# ---------------------------------------------------------------------
# início do jogo
# ---------------------------------------------------------------------
menu_principal()