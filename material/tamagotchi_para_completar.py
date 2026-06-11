import animais
import emojis
import random

# crie uma variável para armazenar o nome do seu tamagotchi
{COMPLETE AQUI!!}

# acesse o arquivo "animais.py" para ver como são as opções de animais e escolha um deles ;)
# ao escrever animais. dá para acessar as variáveis criadas no arquivo "animais.py"
meu_tamagotchi = animais.{COMPLETE AQUI!!}

# também no arquivo "animais.py", veja as cores em que seu animal pode ser desenhado no terminal
# complete depois do . com a cor desejada
cor = animais.{COMPLETE AQUI!!}

# versão dormindo do seu tamagotchi (deve combinar com o animal escolhido acima!)
# como fizemos acima para poder acessar uma variável que estava no arquivo "animais.py"?
animal_dormindo = {COMPLETE AQUI!!}

# escolha o emoji que representa a ENERGIA do seu tamagotchi
# sugestões: emojis.fogo, emojis.raio, emojis.coracao_rosa, emojis.coracao_amarelo, emojis.flor
emoji_energia = emojis.{COMPLETE AQUI!!}

# escolha o emoji que representa o DINHEIRO do seu tamagotchi
# sugestões: emojis.diamante, emojis.moeda, emojis.saca_dinheiro, emojis.flor, emojis.chocolate
# como fizemos acima para poder acessar uma variável que estava no arquivo "emojis.py"?
emoji_dinheiro = {COMPLETE AQUI!!}
                  
# escolha o emoji que representa a FOME do seu tamagotchi
emoji_fome = {COMPLETE AQUI!!}

# ---------------------------------------------------------------------
# funções do tamagotchi
# ---------------------------------------------------------------------

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
        print({COMPLETE AQUI!!})  # escreva uma mensagem de aviso de fome entre aspas

    print()


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
        # complete o print abaixo com a variável "horas" para mostrar quantas horas dormiu
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
        "3": {"nome": "bolo",       "emoji": emojis.cupcake,   "preco": 3, "fome": 6},
    }

    print("\n" + "=" * 40)
    # complete o print abaixo com o nome do tamagotchi e um emoji de comida
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
# Quando terminar um jogo novo, cole a função aqui em cima e
# adicione uma linha nova na lista abaixo!
# =============================================================

jogos_disponiveis = [
    {"nome": "Pedra, Papel, Tesoura",            "funcao": pedra_papel_tesoura,           "custo": 1, "premio": 2},
    # {"nome": "PPT Turbinado (Lagarto+Spock)", "funcao": pedra_papel_tesoura_turbinado, "custo": 1, "premio": 3},
    # {"nome": "Jogo de Apostas — dado",        "funcao": jogo_de_apostas,               "custo": 2, "premio": 4},
    # {"nome": "Jogo da Velha",                 "funcao": jogo_da_velha,                 "custo": 3, "premio": 5},
]
# Dica: para ativar um jogo, apague o # do início da linha dele!


# ---------------------------------------------------------------------
# menus
# ---------------------------------------------------------------------

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


# ---------------------------------------------------------------------
# início do jogo
# ---------------------------------------------------------------------
menu_principal()